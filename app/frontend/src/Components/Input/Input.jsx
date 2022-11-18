import React, {useState, useRef} from 'react'

const Input = (props) => {
    const [validFile, setValidFile] = useState(false)

    const inputRef = useRef(null)

    const handleUpload = async (e) => {
        e.preventDefault()
        const url = new URL("http://localhost:5000")
        let form = new FormData();
        form.append("file", inputRef.current.files[0]);
        let response = await fetch(`${url}upload`, {
            method: 'POST',
            body: form
            });

        let result = await response.json();
        console.log(result)
    }

    const validateUpload = (e) => {
        if (e.target.files[0].type === "application/pdf"){
            setValidFile(true)
            props.setFile(e.target.files[0])
        }
    }

  return (
    <div>
        <form action="submit" onSubmit={handleUpload}>
            <input type="file" name="upload" accept="application/pdf" ref={inputRef} onChange={validateUpload}/>
            
            {validFile === true && <button type='submit'>Submit</button>}
        </form>
    </div>
  )
}

export default Input