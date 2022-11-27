// Components
import { useState } from "react";
import Header from "./Components/Header/Header";
import Input from "./Components/Input/Input";
// import Viewer from "./Components/Viewer/Viewer";

// CSS
import styles from "./App.module.css"


function App() {


  const [file, setFile] = useState(null)
  const [isLoading, setIsLoading] = useState(false)

  return (
    <div className={styles}>
      <Header/>
      <Input setFile={setFile} setIsLoading = {setIsLoading}/>

      {/* {file != null && <Viewer pdfFileName={file}/>} */}
      {isLoading === true && <p>"File is being loaded"</p>}
    </div>
  );
}

export default App;
