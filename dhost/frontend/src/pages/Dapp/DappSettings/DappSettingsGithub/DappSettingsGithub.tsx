import { DappContextType } from "contexts/DappContext/DappContext"
import React from "react";



function DappSettingsGithub({ dapp, setDapp }: DappContextType): React.ReactElement {

  // var _dapp = dapp;

  function changeRepo(e: React.ChangeEvent<HTMLInputElement>) {
    var _dapp = dapp
    _dapp.github.repo = e.target.value
    setDapp({ ..._dapp })

  }

  function changeBranch(e: React.ChangeEvent<HTMLInputElement>) {
    var _dapp = dapp
    _dapp.github.branch = parseInt(e.target.value, 10)
    setDapp({ ..._dapp })
  }

  function changeAutodep(e: React.MouseEvent<HTMLInputElement, MouseEvent>) {
    var _dapp = dapp
    //_dapp.github.auto_deploy = (e.target. === 'true')
    setDapp({ ..._dapp })
  }

  function changeConfirmCI() {
    dapp.github.confirm_ci = !dapp.github.confirm_ci;
    setDapp({ ...dapp })
  }

  function WithoutRepo() {
    return <h2>Connection to Gihub</h2>;
  }

  function WithRepo() {
    return <div>
      <div className="pb-4 w-1/2">
        <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">Repository</h2>

        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          value={dapp.github.repo}
          onChange={changeRepo} />
      </div>

      <div className="pb-4 w-1/2">
        <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">Branch</h2>

        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          value={dapp.github.branch}
          onChange={changeBranch} />
      </div>
      <div>
        <label className="inline-flex items-center">
          <span className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2 mr-2 w-2/3">Auto deploy</span>
          <input type="checkbox" className="form-checkbox mb-2" onClick={(e) => changeAutodep(e)} />
        </label>
      </div>
      <div>
        <label className="inline-flex items-center">
          <span className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2 mr-2 w-4/3">Confirm CI</span>
          <input type="checkbox" className="form-checkbox mb-2" onClick={changeConfirmCI} />
        </label>
      </div>
    </div>;
  }

  function Core() {
    if (dapp.github.repo == "N/A") {
      return <WithoutRepo />;
    } else {
      return <WithRepo />;
    }
  }


  return (
    <div>
      <Core />
    </div>
  )
}

export default DappSettingsGithub
