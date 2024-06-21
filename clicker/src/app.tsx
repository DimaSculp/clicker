import './app.css';
import bike from './ace/bike.png';
import { useState, useEffect, useRef } from 'react';

export function App() {
  const maxF = 30;
  const [counter, setCounter] = useState(0);
  const [flag, setFlag] = useState(maxF);
  const [nowCpm, setNowCpm] = useState(0);
  const [maxCpm, setMaxCpm] = useState(0);
  const lastMinuteClicksRef = useRef(0);

  function clickCount() {
    if (flag > 0) {
      setCounter(prev => prev + 1);
      setFlag(prev => prev - 1);
      localStorage.setItem('counter',counter.toString())
    }
  }

  function increaseFlag() {
    setFlag(prevFlag => {
      const newFlag = prevFlag + 2;
      return newFlag <= maxF ? newFlag : maxF;
    });
  }

  useEffect(() => {
    const interval = setInterval(() => {
      increaseFlag();
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      const clicksThisMinute = counter - lastMinuteClicksRef.current;
      setNowCpm(clicksThisMinute);
      lastMinuteClicksRef.current = counter;
  
      if (clicksThisMinute > maxCpm) {
        setMaxCpm(clicksThisMinute);
      }
    }, 60000);
  
    return () => clearInterval(interval);
  }, [counter, maxCpm]);

  return (
    <div className="box">
      <span>{counter} m</span>
      <span style={{ top: '43%', left:'18%', color: 'white', fontSize: '1.5em' }}>
        max CPM: {maxCpm} 
      </span>
      <span style={{ top: '43%', left:'80%', color: 'white', fontSize: '1.5em' }}>
         CPM: {nowCpm} 
      </span>
      <span style={{ top: '77%', left: '23%', color: 'white', fontSize: '2em' }}>
        {flag} / {maxF}
      </span>
      <div className="tap">
        <img src={bike} alt="bike" width={256} height={256} size={0.5} style={{ position: 'absolute', zIndex: '50' }} onClick={clickCount} />
        <img
          src={bike}
          alt="bike"
          width={256}
          height={256}
          size={1}
          style={{ filter: 'blur(10px)', position: 'absolute', zIndex: '-5' }}
        />
      </div>
    </div>
  );
};
