import './App.css';
import logo from "./assets/logo/logo.png"
import Download from './components/download/Download';
import bgImg from "./assets/app/plants_background.gif"

function App() {


  return (
    <div className="App">
      <img
        className='gaggum__logo'
        src={logo}
        alt=""
      />
      <h1 className='gaggum__title'>당신의 식물을 책임져드립니다.</h1>
      <Download />
      <img 
        className="gaggum__bakcground"
        src={bgImg}
        alt=""
      />
    </div>
  );
}

export default App;
