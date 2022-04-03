import { Button } from "react-bootstrap"
import { useHistory } from "react-router-dom"
import { useModals } from "contexts/ModalsContext/ModalsContext"
import { Dapp } from "models/api/Dapp"
import "./ListDapp.css"

export function ListDapp({ dapps }: { dapps: Dapp[] }): React.ReactElement {
  let history = useHistory()
  const { setShowCreateDappModal } = useModals()

  const handleDapp = (dapp: Dapp) => {
    history.push(`/dapps/${dapp.slug}`)
  }

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
      <div className="listDapp mt-3 block">
        <div className="mx-5">
          <h2 className="text-3xl pb-2">
            <span className="LineThroughtBefore"></span>List Dapps
            <span className="LineThroughtAfter"></span>
          </h2>
          <div className="flex grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
            {dapps.map((dapp, i) => {
              let currentStatus = allStatus.find(
                (s) => s.shortName === dapp.status
              )

              return (
                <div className="w-100 mb-3 mt-2 px-3">
                  <button
                    key={i}
                    className="w-100 text-base text-gray-800 font-medium rounded bg-white bg-green-50 shadow hover:scale-105 focus:scale-100 focus:bg-grey-100 transition cursor-pointer"
                    onClick={() => handleDapp(dapp)}
                  >
                    <div className="buttonHeader h-5 bg-green-500 rounded-tl-md rounded-tr-md" />
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
                </div>
              )
            })}
          </div>
          <div className="flex justify-center mt-4">
            <Button
              className="flex items-center h-8 mr-4 bg-green-500 hover:bg-green-600 focus:bg-green-700 border-none px-5 py-4 mb-5 text-xl"
              onClick={() => {
                setShowCreateDappModal(true)
              }}
            >
              Create Dapp
            </Button>
          </div>
        </div>
      </div>
    )
  }

  return dapps.length > 0 ? renderDapps() : <span>No dapp to show.</span>
}
