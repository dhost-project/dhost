import { DappContextType } from "contexts/DappContext/DappContext"

function DappSettingsBuild({
  dapp,
  setDapp,
}: DappContextType): React.ReactElement {
  function changeCommand(e: React.ChangeEvent<HTMLInputElement>) {
    var _dapp = dapp
    _dapp.build.command = e.target.value
    setDapp({ ..._dapp })
  }

  function changeDocker(e: React.ChangeEvent<HTMLInputElement>) {
    var _dapp = dapp
    _dapp.build.docker = e.target.value
    setDapp({ ..._dapp })
  }

  return (
    <div>
      <div className="pb-4 w-1/2">
        <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">
          Command
        </h2>

        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          value={dapp.build.command}
          onChange={changeCommand}
        />
      </div>
      <div className="pb-4 w-1/2">
        <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">
          Docker
        </h2>

        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          value={dapp.build.docker}
          onChange={changeDocker}
        />
      </div>
    </div>
  )
}

export default DappSettingsBuild
