import { DappLogs } from "models/api/DappLogs"
import { List } from "./List"
import { ListItem } from "./ListItem"

export function ListDappLogs({
  dappLogsList,
  logsCount,
  gap,
}: {
  dappLogsList: DappLogs[]
  logsCount: number
  gap: boolean
}): React.ReactElement {
  let buildsLogs = dappLogsList.filter(
    (dappLog) =>
      dappLog.action_flag === "build_success" ||
      dappLog.action_flag === "build_error" ||
      dappLog.action_flag === "build_start" ||
      dappLog.action_flag === "deploy_fail" ||
      dappLog.action_flag === "deploy_success" ||
      dappLog.action_flag === "dapp_add" ||
      dappLog.action_flag === "bundle_add" ||
      dappLog.action_flag === "deploy_start"
  )
  let dappLogsListOverview = dappLogsList.slice(0, logsCount)

  return (
    <div>
      {!logsCount ? (
        dappLogsList.map((dappLog, i) => (
          <ListItem key={i} dappLog={dappLog} gap={gap} />
        ))
      ) : logsCount === 3 && buildsLogs.length ? (
        buildsLogs.map((dappLog, i) => (
          <ListItem key={i} dappLog={dappLog} gap={gap} />
        ))
      ) : logsCount === 3 ? (
        <p
          className="italic text-center bg-gray-100 py-5"
          style={{ color: "grey" }}
        >
          There is no build yet...
        </p>
      ) : (
        dappLogsListOverview.map((dappLog, i) => (
          <ListItem key={i} dappLog={dappLog} gap={gap} />
        ))
      )}
    </div>
  )
}
