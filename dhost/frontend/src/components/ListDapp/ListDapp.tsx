import { DappContext, DappContextType, IDapp, useDapp } from "contexts/DappContext/DappContext"
import { Dapp } from "models/api/Dapp"
import { List } from "./List"
import { ListItem } from "./ListItem"
import { useHistory } from "react-router-dom"
import { Dispatch, SetStateAction, useEffect, useState } from "react"
import { listIPFSDapps } from "api/IPFSDapps"
import { render } from "@headlessui/react/dist/utils/render"
import { useTranslation } from "react-i18next"



export function ListDapp({ dapps }: { dapps: Dapp[] }): React.ReactElement {

  let history = useHistory()
  const { t } = useTranslation()


  const handleDapp = (dapp: Dapp) => {
    history.push(`/dapps/${dapp.slug}`)
  }

  // const displayDate = (date: string | undefined) => {
  //   if (date === undefined) {
  //     console.log(dapps)
  //     return ""
  //   } else {
  //     let res = new Date(date).toLocaleDateString()
  //     console.log(res)
  //     return res
  //   }
  // }

  function renderWells() {
    return (<div className="mt-3 block">
      <hr className="mt-4 mb-3" />
      <div className="mx-5">
        {dapps.map((dapp, i) => (
          <button
            key={i}
            className="w-1/3 mb-3 mt-2 px-4 py-4 border-2 text-base text-gray-800 font-medium rounded-lg bg-white hover:bg-green-50 hover:border-green-400 focus:bg-green-50 focus:border-green-400 focus:ring-offset-0 focus:ring-green-400 focus:outline-none focus:ring-1 transition cursor-pointer"
            onClick={() => handleDapp(dapp)}
          >
            <p className="uppercase" style={{ textAlign: "left" }}>
              {dapp.slug}
            </p>
            <p className="uppercase" style={{ textAlign: "right" }}>
              {t("status")} {dapp.status}
            </p>

          </button>
        ))}
      </div>
    </div>)
  }

  return (
    dapps.length > 0 ?
      renderWells() : <span>Data loading...</span>
  )
}