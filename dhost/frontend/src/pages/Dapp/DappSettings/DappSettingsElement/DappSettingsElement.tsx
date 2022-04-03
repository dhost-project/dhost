import { useDapp } from "contexts/DappContext/DappContext"

function DappSettingsElement({ desc }: any): React.ReactElement {
  // const [{slug, setSlug}] = useDapp();

  function increment() {
    // setSlug((current: string) => current + 1);
  }
  // const title : string = '';
  return (
    <div>
      <label className="col-sm-2 col-form-label">slug {desc}</label>
      <button onClick={() => increment()}>Increment</button>
      <input></input>
    </div>
  )
}

export default DappSettingsElement
