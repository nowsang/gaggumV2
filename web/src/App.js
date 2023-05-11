import './App.css';
import logo from "./assets/logo/logo.png"
import Download from './components/download/Download';

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
    </div>
  );
}

export default App;
