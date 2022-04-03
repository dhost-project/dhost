import { render } from "@headlessui/react/dist/utils/render"
import { Dispatch, SetStateAction, useEffect, useState } from "react"
import { useTranslation } from "react-i18next"
import { useHistory } from "react-router-dom"
import { listIPFSDapps } from "api/IPFSDapps"
import {
  DappContext,
  DappContextType,
  IDapp,
  useDapp,
} from "contexts/DappContext/DappContext"
import { Dapp } from "models/api/Dapp"
import { List } from "./List"
import { ListItem } from "./ListItem"

export function ListDapp({ dapps }: { dapps: Dapp[] }): React.ReactElement {
  let history = useHistory()
  const { t } = useTranslation()

  const handleDapp = (dapp: Dapp) => {
    history.push(`/dapps/${dapp.slug}`)
  }

  const [status, setStatus] = useState({
    name: "Loading",
    shortName: "LO",
    color: "#999",
  })

  const allStatus = [
    { name: "Stoped", shortName: "SO", color: "#B33" },
    { name: "Building", shortName: "BA", color: "#660" },
    { name: "Built", shortName: "BT", color: "#660" },
    { name: "Deploying", shortName: "DP", color: "#660" },
    { name: "Starting", shortName: "SA", color: "#660" },
    { name: "Up", shortName: "UP", color: "#3B3" },
    { name: "Unavailable", shortName: "UA", color: "#660" },
    { name: "Error", shortName: "ER", color: "#660" },
  ]

  function renderDapps() {
    return (
      <div className="mt-3 block">
        <div className="mx-5">
          {dapps.map((dapp, i) => {
            let currentStatus = allStatus.find(
              (s) => s.shortName === dapp.status
            )

            return (
              <button
                key={i}
                className="w-100 mb-3 mt-2 border-2 text-base text-gray-800 font-medium rounded bg-white bg-green-50 hover:border-green-400 focus:bg-green-50 focus:border-green-400 focus:ring-offset-0 focus:ring-green-400 focus:outline-none focus:ring-1 transition cursor-pointer"
                onClick={() => handleDapp(dapp)}
              >
                <div className="h-2.5 bg-green-500 rounded-tl-md rounded-tr-md" />
                <div className="px-4 py-4">
                  <h2
                    className="uppercase text-xl"
                    style={{ textAlign: "left" }}
                  >
                    {dapp.slug}
                  </h2>
                  <p className="uppercase" style={{ textAlign: "right" }}>
                    <span
                      className="py-2 px-3 rounded text-white"
                      style={{
                        backgroundColor: currentStatus
                          ? currentStatus.color
                          : "grey",
                      }}
                    >
                      {currentStatus ? currentStatus.name : "Loading"}
                    </span>
                  </p>
                </div>
              </button>
            )
          })}
        </div>
      </div>
    )
  }

  return dapps.length > 0 ? renderDapps() : <span>No dapp to show.</span>
}
