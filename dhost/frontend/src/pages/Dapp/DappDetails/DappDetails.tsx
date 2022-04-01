import { useState, useEffect } from "react"
import { useTranslation } from "react-i18next"
import { RouteComponentProps } from "react-router-dom"
import { ListDappLogs } from "components/ListDappLogs"
import { ThreeSubscriptions } from "components/Subscription/ThreeSubscriptions"
import { useDapp } from "contexts/DappContext/DappContext"
import "./DappDetails.css"

type TParams = { dapp_slug: string }

export function DappDetails({
  match,
}: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()
  const { dapp } = useDapp()

  const url = dapp.basic.url
  const [iframeOpacity, setIframeOpacity] = useState(false)
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

  useEffect(() => {
    if (dapp) {
      let currentStatus = allStatus.find(
        (s) => s.shortName === dapp.basic.status
      )
      if (currentStatus) setStatus(currentStatus)
    }
  }, [dapp])

  return (
    <div className="overview">
      <div className="container mx-auto md:flex mt-4">
        <div className="w-100 md:flex">
          <a href={dapp.basic.url} target="_blank">
            <div
              className="thumbnail mr-2"
              title={url ? "Go to site" : "no preview available"}
            >
              {url ? (
                <iframe
                  src={url}
                  frameBorder="0"
                  width="384"
                  height="216"
                  onLoad={() => setIframeOpacity(true)}
                  style={iframeOpacity ? { opacity: "1" } : { opacity: "0" }}
                />
              ) : (
                <img
                  src="https://admin.amslaw.ph/uploads/misc/noImagePreview.jpg"
                  alt="preview site"
                  onLoad={() => setIframeOpacity(true)}
                  style={iframeOpacity ? { opacity: "1" } : { opacity: "0" }}
                ></img>
              )}
            </div>
          </a>
          <div className="ml-2 mt-3 mr-4">
            <span
              className="py-2 px-3 rounded text-white"
              style={{ backgroundColor: status.color }}
            >
              {status.name}
            </span>
            <p className="mt-2">
              {url ? (
                <a href={dapp.basic.url} target="_blank">
                  {dapp.basic.url}
                </a>
              ) : (
                <p className="italic" style={{ color: "grey" }}>
                  no url yet
                </p>
              )}
            </p>
          </div>
        </div>
        <div className="w-100">
          <h2 className="text-3xl pb-2">
            <span className="LineThroughtBefore"></span>Builds
            <span className="LineThroughtAfter"></span>
          </h2>
          <div className="rounded overflow-hidden">
            <ListDappLogs
              dappLogsList={dapp.dappLogsList}
              logsCount={3}
              gap={true}
            />
          </div>
        </div>
      </div>
      <div className="w-100">
        <h2 className="text-3xl pt-2 pb-2">
          <span className="LineThroughtBefore"></span>Logs
          <span className="LineThroughtAfter"></span>
        </h2>
        <div className="rounded overflow-hidden mb-3">
          <ListDappLogs
            dappLogsList={dapp.dappLogsList}
            logsCount={10}
            gap={false}
          />
        </div>
      </div>
    </div>
  )
}
