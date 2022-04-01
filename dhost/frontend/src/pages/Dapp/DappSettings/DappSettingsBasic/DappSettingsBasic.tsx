import React, { Dispatch, SetStateAction } from "react"
import { IDapp } from "contexts/DappContext/DappContext"

function DappSettingsBasic({
  dapp,
  setDapp,
}: {
  dapp: IDapp
  setDapp: Dispatch<SetStateAction<IDapp>>
}): React.ReactElement {
  const gateways = [
    "https://toto.com",
    "https://wshwsh.ipfs",
    "https://gateway.com",
    "https://blblblb.io",
  ]

  const changeIPFSGateway = (e: React.ChangeEvent<HTMLSelectElement>) => {
    var _dapp = dapp
    _dapp.basic.ipfs_gateway = e.target.value
    setDapp({ ..._dapp })
  }

  return (
    <div className="md:w-75 md:ml-2">
      <label
        className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2"
        htmlFor="grid-state"
      >
        IPFSGateway
      </label>
      <div className="relative">
        <select
          className="block appearance-none w-100 bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
          id="grid-state"
          value={dapp.basic.ipfs_gateway}
          onChange={(e) => {
            changeIPFSGateway(e)
          }}
        >
          {gateways.map((_gateway, i) => (
            <option key={`${_gateway}-${i}`}>{_gateway}</option>
          ))}
        </select>
        <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
          <svg
            className="fill-current h-4 w-4"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
          >
            <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
          </svg>
        </div>
      </div>
    </div>
  )
}

export default DappSettingsBasic
