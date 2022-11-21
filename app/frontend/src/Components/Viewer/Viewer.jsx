import React from 'react'
import { Document, Page, pdfjs} from 'react-pdf'
import 'react-pdf/dist/esm/Page/TextLayer.css';
// Styles
import styles from "./Viewer.module.css"



pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;



const options = {
    cMapUrl: 'cmaps/',
    cMapPacked: true,
    standardFontDataUrl: 'standard_fonts/',
  };


const Viewer = (props) => {
  return (
    <div className={styles.viewer}>
      <Document className ={styles.document} file={props.pdfFileName} options={options}>
        <Page key={`page_1`} pageNumber={1} scale={0.8} className={styles.page}/>
      </Document>

    </div>
    
  )
}

export default Viewer