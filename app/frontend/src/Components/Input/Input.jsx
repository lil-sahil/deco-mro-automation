import React, {useState, useRef} from 'react'

const Input = (props) => {
    const [validFile, setValidFile] = useState(false)

    const inputRef = useRef(null)


//     const handleUpload = (e) => {
//         e.preventDefault()
      

//         const url = new URL("http://localhost:5000")
//         let form = new FormData();
//         form.append("file", inputRef.current.files[0]);

//         let initParams = {
//             mode:"no-cors",
//             method: 'POST',
//             body: form
//         }

//         fetch(`${url}upload`, initParams)
//             .then(response => {
//                 console.log(response.headers)
//                 alert(response.headers.get("content-disposition"));
//                 return response.blob();
   
// })
// .then(blob => {
//    var url = new URL.createObjectURL(blob);
//    console.log(url)
// })     
//     }

    // const handleUpload = async (e) => {
    //     e.preventDefault()
    //     const url = new URL("http://localhost:5000")
    //     let form = new FormData();
    //     form.append("file", inputRef.current.files[0]);
    //     let response = await fetch(`${url}upload`, {
    //         mode:"no-cors",
    //         method: 'POST',
    //         body: form
    //         });
        
    //     let result = await response.blob();
        
    // }

    // const handleUpload = async (e) => {
    //     e.preventDefault()
    //     const url = new URL("http://localhost:5000")
    //     let response = await fetch(`${url}get_file`, {
    //         mode:"no-cors",
    //         method: 'get',
    //         headers: {
    //             'content-type': 'text/csv;charset=UTF-8',
    //         }
    //         });
    //     let result = await response.text();
    //     console.log(result)
    // }


    const handleUpload = (e) => {
        e.preventDefault()
        const url = new URL("http://localhost:5000")
        let form = new FormData();
        form.append("file", inputRef.current.files[0]);
        let params = {
                    mode:"no-cors",
                    method: 'POST',
                    body: form
                    }
        fetch(`${url}upload`, params)
            .then(res => {
                const disposition = res.headers.get('Content-Disposition');
                return res.blob();
            })
            .then(blob => {
                console.log(blob)
                var url = window.URL.createObjectURL(blob);
                var a = document.createElement('a');
                a.href = url;
                a.download = "test";
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
    <div>
        <form action="submit" onSubmit={handleUpload}>
            <input type="file" name="upload" accept="application/pdf" ref={inputRef} onChange={validateUpload}/>
            
            {validFile === true && <button type='submit'>Submit</button>}
        </form>
    </div>
  )
}

export default Input