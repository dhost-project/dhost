import { useEffect } from "react"
import { useTranslation } from "react-i18next"
import { DappLogs } from "models/api/DappLogs"

export function ListItem({
  dappLog,
  gap,
}: {
  dappLog: DappLogs
  gap: boolean
}): React.ReactElement {
  const { t } = useTranslation()
  var colors

  let date = new Date(dappLog.action_time)

  switch (true) {
    case /success|dapp_add/.test(dappLog.action_flag):
      colors =
        "bg-green-100 text-green-600 hover:bg-green-200 hover:text-green-700"
      break
    case /error/.test(dappLog.action_flag):
      colors = "bg-red-100 text-red-600 hover:bg-red-200 hover:text-red-700"
      break
    default:
      colors = "bg-gray-100 text-gray-600 hover:bg-gray-200 hover:text-gray-700"
      break
  }

  return (
    <a
      className={`${colors} px-4 py-2`}
      href={`/dappLogs/${dappLog.id}/`}
      style={
        gap
          ? { marginBottom: "5px", border: "none", borderRadius: "5px" }
          : { marginBottom: "0" }
      }
    >
      {/* {dappLog.user} */}
      {t(dappLog.action_flag)}
      {dappLog.change_message}
      <br />
      <p className="italic text-sm" style={{ color: "grey" }}>
        {date.toLocaleString()}
      </p>
    </a>
  )
}
