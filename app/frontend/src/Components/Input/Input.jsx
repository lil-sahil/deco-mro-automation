import React, {useState, useRef} from 'react'

const Input = (props) => {
    const [validFile, setValidFile] = useState(false)

    const inputRef = useRef(null)

    const handleUpload = (e) => {
        e.preventDefault()
        console.log(inputRef.current.files[0])
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