import "./Download.css"

const Download = () => {
  const fileURL = "https://drive.google.com/file/d/1Ls0A04spChEz6BHQGAE5yEAmRkgFUYpd/view?usp=share_link"

  return (
    <div className="download">
      <a href={fileURL} download>
        <button className="download__btn">가꿈</button>
      </a>
    </div>
  )
};

export default Download;