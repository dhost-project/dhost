import { useState, useEffect } from "react"
import { useTranslation } from "react-i18next"
import { RouteComponentProps } from "react-router-dom"
import { toast } from "react-toastify"
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

  const saveToClipboard = () => {
    navigator.clipboard.writeText(dapp.basic.url ?? "")
    toast.info("Dapp's url saved to clipboard.")
  }

  return (
    <div className="overview">
      <div className="container mx-auto md:flex mt-4">
        <div className="md:flex w-100">
          {url ? (
            <a href={dapp.basic.url} target="_blank">
              <div
                className="thumbnail mr-2 border-2 rounded"
                title="Go to site"
              >
                <iframe
                  src={url}
                  frameBorder="0"
                  onLoad={() => setIframeOpacity(true)}
                  style={
                    iframeOpacity
                      ? {
                          opacity: "1",
                          width: "384px !important",
                          height: "auto",
                        }
                      : {
                          opacity: "0",
                          width: "384px !important",
                          height: "auto",
                        }
                  }
                />
              </div>
            </a>
          ) : (
            <div className="thumbnail mr-2" title="no preview available">
              <img
                src="https://admin.amslaw.ph/uploads/misc/noImagePreview.jpg"
                alt="preview site"
                onLoad={() => setIframeOpacity(true)}
                width="384"
                height="216"
                style={
                  iframeOpacity
                    ? {
                        opacity: "1",
                        width: "384px !important",
                        height: "auto",
                      }
                    : {
                        opacity: "0",
                        width: "384px !important",
                        height: "auto",
                      }
                }
              ></img>
            </div>
          )}
          <div
            id="dappData"
            className="ml-2 mt-3 mr-4 w-100 md:w-50"
            style={{ maxWidth: "200px", wordWrap: "break-word" }}
          >
            <span
              className="py-2 px-3 rounded text-white"
              style={{ backgroundColor: status.color }}
            >
              {status.name}
            </span>
            <p className="mt-2">
              {dapp.basic.url ? (
                <a
                  className="mt-2 cursor-pointer text-blue-500"
                  onClick={saveToClipboard}
                >
                  Share Link
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
