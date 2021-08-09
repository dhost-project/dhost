import { useCounter } from "../../contexts/DappContext/DappContext";


function DappSettingsElement({title, desc}: any): React.ReactElement {
  const {counter, setCounter} = useCounter();

  function increment() {
    setCounter((current: number) => current + 1);
  }
  // const title : string = '';
  return (
    <div>
      <label className="col-sm-2 col-form-label">{counter} {title} {desc}</label>
      <button onClick={() => increment()}>Increment</button>
      <input></input>
    </div>
  )
}

export default DappSettingsElement