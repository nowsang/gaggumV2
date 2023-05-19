import "./Download.css"

const Download = () => {

  return (
    <div className="download">
        <button
          className="download__btn"
          onClick={() => window.open("https://drive.google.com/file/d/14SgaaEzoktlfuIVwdnoSK5JPiPKc0NIr/view?usp=share_link")}
        >Download</button>
    </div>
  )
};

export default Download;