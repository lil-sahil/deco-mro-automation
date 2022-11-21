import React from 'react'

// Icons
import {FaFileCsv} from 'react-icons/fa'
import {AiOutlineFilePdf} from 'react-icons/ai'
import {GoArrowRight} from 'react-icons/go'
import {AiFillGithub} from 'react-icons/ai'

// Styles
import styles from "./Header.module.css"

const Header = () => {
  return (
    <div className={styles.header}>
        <div>
            <div className={styles.title}>PDF to CSV</div>
            <div className={styles.icons}>
              <AiOutlineFilePdf className={styles.pdf}></AiOutlineFilePdf>
              <GoArrowRight></GoArrowRight>
              <FaFileCsv className={styles.csv}></FaFileCsv>
            </div>
        </div>

        <div className = {`${styles.github} ${styles.icons}`}>
            <a href="https://github.com/lil-sahil/deco-mro-automation/tree/main/app"><AiFillGithub></AiFillGithub></a>
        </div>
    </div>
  )
}

export default Header