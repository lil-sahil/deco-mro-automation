import React, {useState, useRef} from 'react'

// Styles
import styles from "./Input.module.css"

const Input = (props) => {
    const [validFile, setValidFile] = useState(false)

    const inputRef = useRef(null)

    const handleUpload = (e) => {

        // Refer to this stackoverflow post:
        // https://stackoverflow.com/questions/71191662/how-do-i-download-a-file-from-fastapi-backend-using-fetch-api-in-the-frontend
        e.preventDefault()
        // http://localhost:5000
        // http://172.19.10.67:8000
        const url = new URL("http://localhost:5000")
        let form = new FormData();
        form.append("file", inputRef.current.files[0]);
        let params = {
                    method: 'POST',
                    body: form
                    }
        fetch(`${url}upload`, params)
            .then(res => {
                // const disposition = res.headers.get('Content-Disposition');
                return res.blob();
            })
            .then(blob => {
                let url = window.URL.createObjectURL(blob);
                let a = document.createElement('a');
                a.href = url;
                a.download = "data";
                document.body.appendChild(a); // append the element to the dom
                a.click();
                a.remove(); // afterwards, remove the element  
            });
    }

    const validateUpload = (e) => {
        if (e.target.files[0].type === "application/pdf"){
            setValidFile(true)
            props.setFile(e.target.files[0])
        }
    }

  return (
    <div className={styles["input-main"]}>
        <form action="submit" onSubmit={handleUpload}>
            <input type="file" name="upload" accept="application/pdf" ref={inputRef} onChange={validateUpload}/>
            
            {validFile === true && <button type='submit'>Convert!</button>}
        </form>
    </div>
  )
}

export default Input