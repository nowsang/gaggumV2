import "./Download.css"

const Download = () => {
  const fileURL = ""

  return (
    <div className="download">
      <a href={fileURL} download>
        <button className="download__btn">가꿈</button>
      </a>
    </div>
  )
};

export default Download;