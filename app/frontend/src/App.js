// Components
import { useState } from "react";
import Header from "./Components/Header/Header";
import Input from "./Components/Input/Input";
import Viewer from "./Components/Viewer/Viewer";

// CSS


function App() {


  const [file, setFile] = useState(null)

  return (
    <div>
      <Header/>
      <Input setFile={setFile}/>

      {file != null && <Viewer pdfFileName={file}/>}
    </div>
  );
}

export default App;
