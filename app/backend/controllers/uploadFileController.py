import pandas as pd
import tabula


def clean_file(file_object):
    df = tabula.read_pdf(file_object, pages='all', multiple_tables=False)
    print(df)