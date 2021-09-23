import { DappContextType } from "contexts/DappContext/DappContext"



function DappSettingsGithub({ dapp, setDapp }: DappContextType): React.ReactElement {

  function changeRepo() {

  }

  function changeBranch() {

  }

  function changeAutodep() {
    dapp.github.auto_deploy = !dapp.github.auto_deploy;
  }

  function changeConfirmCI() {
    dapp.github.confirm_ci = !dapp.github.confirm_ci;
    console.log(dapp.github.confirm_ci);
  }


  return (
    <div>
      <h2>Connection to Gihub</h2>

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
          <span className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2 mr-2">Auto deploy</span>
          <input type="checkbox" className="form-checkbox mb-2" onClick={changeAutodep} />
        </label>
      </div>
      <div>
        <label className="inline-flex items-center">
          <span className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2 mr-2">Confirm CI</span>
          <input type="checkbox" className="form-checkbox mb-2" onClick={changeConfirmCI} />
        </label>
      </div>
    </div>
  )
}

export default DappSettingsGithub
