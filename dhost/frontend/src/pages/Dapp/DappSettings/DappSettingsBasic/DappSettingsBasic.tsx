import React, { Dispatch, SetStateAction, useState } from "react"
import {
  DappContextType,
  DappContext,
  useDapp,
  IDapp,
} from "contexts/DappContext/DappContext"
import { Dapp } from "models/api/Dapp"

type State = {
  text: string
}

function DappSettingsBasic({
  dapp,
  setDapp,
}: { dapp: IDapp, setDapp: Dispatch<SetStateAction<IDapp>> }): React.ReactElement {
  // const [_name, setName] = useState(name);
  // const [_gateway, setGateway] = useState(gateway);
  // const [{slug, setSlug}] = useDapp();

  const gateways = ["toto.com", "wshwsh.ipfs", "gateway.com", "blblblb.io"]

  // typing on RIGHT hand side of =
  //   const onChange = (e: React.ChangeEvent<HTMLInputElement>)=> {
  //     state.text += e.currentTarget.
  //  }

  function changeName(e: React.ChangeEvent<HTMLInputElement>) {
    var _dapp = dapp
    _dapp.basic.slug = e.target.value
    setDapp({ ..._dapp })
  }

  function changeGateway(e: React.ChangeEvent<HTMLSelectElement>) {
    // setGateway(e.target.value);
    var _dapp = dapp
    _dapp.basic.url = e.target.value
    setDapp({ ..._dapp })
  }
  return (
    <div>
      <div className="pb-4 w-1/2">
        <h2 className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2">
          Name
        </h2>

        <input
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          type="text"
          value={dapp.basic.slug}
          onChange={changeName}
        />
      </div>

      <div className="w-full md:w-1/2  mb-6 md:mb-0">
        <label
          className="block uppercase tracking-wide text-gray-700 text-xs font-medium mb-2"
          htmlFor="grid-state"
        >
          Gateway
        </label>
        <div className="relative">
          <select
            className="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
            id="grid-state"
            value={dapp.basic.url}
            onChange={changeGateway}
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
    </div>
  )
}

export default DappSettingsBasic
