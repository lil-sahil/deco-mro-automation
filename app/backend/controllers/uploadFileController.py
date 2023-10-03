import pandas as pd
import numpy as np
import tabula
from difflib import SequenceMatcher


class Clean_File:
    def __init__(self, file_name):
        self.file_name = file_name
        print(self.file_name)
        self.df = self.load_pdf_file()
        # self.part_number_df = pd.read_csv("./srPartNumbers.csv")
        self.part_number_and_description_df = pd.read_csv(
            "./dwAndSrPartnumbers.csv")

        # Combine the part number and description 1 into a single column

        self.part_number_and_description_df['combined'] = self.part_number_and_description_df[[
            'PartNumber', 'Desc1']].apply(lambda x: (x[0] + x[1]).replace(" ", "").lower(), axis=1)

    def column_names(self):
        return [
            "Quantity on Hand",
            "Quantity Allocated",
            "Quantity on Order",
            "Quantity on P.O",
            "Minimum Quantity",
            "Maximum Quantity",
            "Part #",
            "Description",
            "Quantity Type",
            "Net Quantity"
        ]

    def load_pdf_file(self):
        return tabula.read_pdf(self.file_name, pages='all', multiple_tables=False)[0]

    def format_vals(self, val_array):
        formatted_vals_arr = []

        for val in val_array:
            # Check if a string contains two decimal points,
            # if so, split the string into two, everything before and after the second decimal point.
            if (str(val).count(".") > 1):
                formatted_vals_arr.append(".".join(val.split(".", 2)[:-1]))

            # Turn the unnamed value into a nan.
            elif ("unnamed" in str(val).lower()):
                formatted_vals_arr.append(np.nan)

            else:
                formatted_vals_arr.append(val)

        return formatted_vals_arr

    def extract_description(self, x1, x2):
        # Check if the description already exists in the x2 column.
        # If it does then return it.
        # If it does not then the description is in the x1 col.
        # Return the x1 col minus the description.

        if type(x2) == str:
            return x2

        else:
            return x1[7:]

    def check_if_part_number_exists(self, part_number):
        return True if self.part_number_df[self.part_number_df['LQPART'] == part_number].shape[0] == 1 else False

    def check_sr_number(self, x1, x2):
        # Combine the partNUmber and description.
        combined = (x1 + x2).replace(" ", "").lower()

        # Check if the string matches the combined column of the fact table.

        partFound = self.part_number_and_description_df[
            self.part_number_and_description_df["combined"] == combined]
        if (partFound.shape[0] == 1):
            return partFound['PartNumber'].values[0], partFound['Desc1'].values[0]

        if(self.part_number_and_description_df[self.part_number_and_description_df['PartNumber']== x1].shape[0] == 1):
            s = SequenceMatcher(
                None, combined, self.part_number_and_description_df[self.part_number_and_description_df['PartNumber'] == x1]['combined'].values[0])

            if (s.ratio() >= 0.90):
                return x1, x2
        return x1, "****NOT FOUND****"

        # If it matches then return the part number column and the description column.

        if (self.check_if_part_number_exists(x1)):
            return x1, x2

        # If the last character is a letter is a sr number
        if (x1[-1].isalpha()):

            if (self.check_if_part_number_exists(x1[:-1])):
                return x1[:-1], x1[-1] + x2

        # If the sr number starts with RSR
        if (x1[0] == "R"):
            if (self.check_if_part_number_exists(x1 + x2[0])):
                return x1 + x2[0], x2[1:]

        else:
            # Start to delete the last character and reference the db
            for i in range(1, 3):
                if (self.check_if_part_number_exists(x1[:i*-1])):
                    return x1[:i*-1], x1[i*-1:] + x2

            # Start to add the number from the description and reference the db
            for i in range(0, 3):
                if (self.check_if_part_number_exists(x1+x2[i])):
                    return x1+x2[i], x2[i+1:]

        return x1, x2

    def clean_df(self):
        print("I am here")
        # Make column_name into a row at the very end of the df.
        self.df.loc[-1] = self.df.columns
        self.df.loc[-1, 2] = np.nan

        # Clean the last row to format values such as .00.2
        print(self.df.iloc[-1].values)
        self.df.loc[-1] = self.format_vals(self.df.iloc[-1].values)

        # Rename column names.
        self.df.columns = [i for i in range(1, len(self.df.columns) + 1)]

        # Make "Part #" column
        # example "DW24824668KF50HD183 #3 STEEL STAMP" => "DW24824"
        self.df['Part #'] = self.df[1].apply(lambda x: x[0:7])

        # Make "Description Column"
        self.df['Description'] = self.df[[1, 2]].apply(
            lambda x: self.extract_description(x[1], x[2]), axis=1)

        # Drop columns 1 and 2.
        self.df.drop(axis=1, columns=[1, 2], inplace=True)

        # Make "Quantity Type" column
        # example "1.00 EA" => "EA"
        self.df['Quantity Type'] = self.df[9].apply(
            lambda x: str(x).split(" ")[-1])

        # Make "Net Quantity" column
        # example "1.00 EA" => "1.00"
        self.df['Net Quantity'] = self.df[9].apply(
            lambda x: str(x).split(" ")[0])

        # Drop columns 9 and 10
        self.df.drop(axis=1, columns=[9, 10], inplace=True)

        # Rename columns to final names
        self.df.columns = self.column_names()

        # Reorder columns
        self.df = self.df.loc[:, ["Part #",
                                  "Description",
                                  "Quantity on Hand",
                                  "Quantity Allocated",
                                  "Quantity on Order",
                                  "Quantity on P.O",
                                  "Minimum Quantity",
                                  "Maximum Quantity",
                                  "Net Quantity",
                                  "Quantity Type"]]

        # Drop rows with nan values for the "Quantity on hand" column
        self.df.dropna(subset=["Quantity on Hand"], inplace=True)

        # Reorder the rows so -1 index comes to the top.
        self.df = pd.concat([self.df[self.df.index == -1],
                            self.df[self.df.index != -1]])

        # Reset the index, so it start from 0.
        self.df.reset_index(drop=True, inplace=True)

        self.df[["Part #", "Description"]] = self.df[["Part #", "Description"]].apply(
            lambda x: pd.Series(self.check_sr_number(x[0], x[1])), axis=1)

        print("Finished!")

        return self.df


def clean_file(file_object):
    df = tabula.read_pdf(file_object, pages='all', multiple_tables=False)
    print(df)
