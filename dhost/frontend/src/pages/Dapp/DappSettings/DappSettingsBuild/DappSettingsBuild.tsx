import { Dispatch, SetStateAction, useEffect, useState } from "react"
import { IDapp } from "contexts/DappContext/DappContext"
import { createBuildOptions } from "api/BuildOptions"

function DappSettingsBuild({
  dapp,
  setDapp,
}: {
  dapp: IDapp
  setDapp: Dispatch<SetStateAction<IDapp>>
}): React.ReactElement {

  const [timer, setTimer] = useState<any>(null);

  function changeCommand(e: React.ChangeEvent<HTMLInputElement>) {
    var _dapp = dapp
    _dapp.build.command = e.target.value
    setDapp({ ..._dapp })
  }

  function changeDocker(e: React.ChangeEvent<HTMLInputElement>) {
    var _dapp = dapp
    _dapp.build.docker = e.target.value
    console.log(_dapp)
    setDapp({ ..._dapp })
  }

  return (
    <div>
      <div className="w-1/3">
        <div className="pb-4 w-1/2">
          <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">
            Command
          </h2>

          <input
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            type="text"
            value={dapp.build.command}
            onChange={(e) => {
              changeCommand(e)
            }}
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
            onChange={(e) => {
              changeDocker(e)
            }}
          />
        </div>
      </div>
    </div>

  )
}

export default DappSettingsBuild
