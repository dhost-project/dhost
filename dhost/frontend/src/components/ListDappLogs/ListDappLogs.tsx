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
  let dappLogsListOverview = dappLogsList.slice(0, logsCount)

  return (
    <List>
      {!logsCount
        ? dappLogsList.map((dappLog, i) => (
            <ListItem key={i} dappLog={dappLog} gap={gap} />
          ))
        : dappLogsListOverview.map((dappLog, i) => (
            <ListItem key={i} dappLog={dappLog} gap={gap} />
          ))}
    </List>
  )
}
