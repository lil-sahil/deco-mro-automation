import React from 'react'
import { Document, Page, pdfjs } from 'react-pdf'
import 'react-pdf/dist/esm/Page/TextLayer.css';
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

const options = {
    cMapUrl: 'cmaps/',
    cMapPacked: true,
    standardFontDataUrl: 'standard_fonts/',
  };


const Viewer = (props) => {
  return (
    <Document file={props.pdfFileName} options={options}>
        <Page key={`page_1`} pageNumber={1}/>
    </Document>
  )
}

export default Viewer