import { Dispatch, SetStateAction, useEffect, useState } from "react"
import { createBuildOptions } from "api/BuildOptions"
import { IDapp } from "contexts/DappContext/DappContext"

function DappSettingsBuild({
  dapp,
  setDapp,
}: {
  dapp: IDapp
  setDapp: Dispatch<SetStateAction<IDapp>>
}): React.ReactElement {
  function changeCommand(e: React.ChangeEvent<HTMLInputElement>) {
    var _dapp = dapp
    _dapp.build.command = e.target.value
    setDapp(dapp => ({ ...dapp, ..._dapp }))
  }

  function changeDocker(e: React.ChangeEvent<HTMLInputElement>) {
    var _dapp = dapp
    _dapp.build.docker = e.target.value
    console.log(_dapp)
    setDapp(dapp => ({ ...dapp, ..._dapp }))
  }

  return (
    <div className="md:w-75 md:ml-2">
      <div className="pb-4">
        <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">
          Command
        </h2>

        <input
          className="appearance-none border rounded w-100 py-2 px-3 text-gray-700 focus:outline-none"
          type="text"
          value={dapp.build.command}
          onChange={(e) => {
            changeCommand(e)
          }}
        />
      </div>
      <div className="pb-4">
        <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">
          Docker
        </h2>

        <input
          className="appearance-none border rounded w-100 py-2 px-3 text-gray-700 focus:outline-none"
          type="text"
          value={dapp.build.docker}
          onChange={(e) => {
            changeDocker(e)
          }}
        />
      </div>
    </div>
  )
}

export default DappSettingsBuild
