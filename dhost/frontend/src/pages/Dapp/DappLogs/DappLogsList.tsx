import { ListDappLogs } from "components/ListDappLogs"
import { DappLogs } from "models/api/DappLogs"

export function DappLogsList({
  dappLogs,
}: {
  dappLogs: DappLogs[]
}): React.ReactElement {
  return (
    <div className="container mx-auto my-4">
      <ListDappLogs dappLogsList={dappLogs} logsCount={10} gap={false} />
    </div>
  )
}
