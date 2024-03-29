import { Dispatch, SetStateAction } from "react"
import { IDapp } from "contexts/DappContext/DappContext"

export function DappSettingsGithub({
  dapp,
  setDapp,
}: {
  dapp: IDapp
  setDapp: Dispatch<SetStateAction<IDapp>>
}): React.ReactElement {
  function changeRepo(e: React.ChangeEvent<HTMLInputElement>) {
    dapp.github.repo = e.target.value
    setDapp((_dapp) => ({ ..._dapp, ...dapp }))
  }

  function changeBranch(e: React.ChangeEvent<HTMLInputElement>) {
    dapp.github.branch = parseInt(e.target.value, 10)
    setDapp((_dapp) => ({ ..._dapp, ...dapp }))
  }

  function changeAutodep(e: React.ChangeEvent<HTMLInputElement>) {
    dapp.github.auto_deploy = e.target.checked
    setDapp((_dapp) => ({ ..._dapp, ...dapp }))
  }

  function changeConfirmCI(e: React.ChangeEvent<HTMLInputElement>) {
    dapp.github.confirm_ci = e.target.checked
    setDapp((_dapp) => ({ ..._dapp, ...dapp }))
  }

  function WithoutRepo() {
    return <h2>Connection to Gihub</h2>
  }

  function WithRepo() {
    return (
      <div>
        <div className="pb-4 w-1/2">
          <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">
            Repository
          </h2>

          <input
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            type="text"
            value={dapp.github.repo}
            onChange={changeRepo}
          />
        </div>

        <div className="pb-4 w-1/2">
          <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">
            Branch
          </h2>

          <input
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            type="text"
            value={dapp.github.branch}
            onChange={changeBranch}
          />
        </div>
        <div>
          <label className="inline-flex items-center">
            <span className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2 mr-2 w-2/3">
              Auto deploy
            </span>
            <input
              type="checkbox"
              className="form-checkbox mb-2"
              onChange={changeAutodep}
              checked={dapp.github.auto_deploy}
            />
          </label>
        </div>
        <div>
          <label className="inline-flex items-center">
            <span className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2 mr-2 w-4/3">
              Confirm CI
            </span>
            <input
              type="checkbox"
              className="form-checkbox mb-2"
              onChange={changeConfirmCI}
              checked={dapp.github.confirm_ci}
            />
          </label>
        </div>
      </div>
    )
  }

  // return (dapp.github.repo === "N/A") ? <WithoutRepo /> : <WithRepo />
  return dapp.github.repo === "N/A" ? (
    <h2>Connection to Gihub</h2>
  ) : (
    <div>
      <div className="pb-4 w-1/2">
        <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">
          Repository
        </h2>

        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          value={dapp.github.repo}
          onChange={changeRepo}
        />
      </div>

      <div className="pb-4 w-1/2">
        <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">
          Branch
        </h2>

        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          value={dapp.github.branch}
          onChange={changeBranch}
        />
      </div>
      <div>
        <label className="inline-flex items-center">
          <span className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2 mr-2 w-2/3">
            Auto deploy
          </span>
          <input
            type="checkbox"
            className="form-checkbox mb-2"
            onChange={changeAutodep}
            checked={dapp.github.auto_deploy}
          />
        </label>
      </div>
      <div>
        <label className="inline-flex items-center">
          <span className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2 mr-2 w-4/3">
            Confirm CI
          </span>
          <input
            type="checkbox"
            className="form-checkbox mb-2"
            onChange={changeConfirmCI}
            checked={dapp.github.confirm_ci}
          />
        </label>
      </div>
    </div>
  )
}

export default DappSettingsGithub
