import { ListDappLogs } from "components/ListDappLogs"
import { ThreeSubscriptions } from "components/Subscription/ThreeSubscriptions"
import { useDapp } from "contexts/DappContext/DappContext"
import { useTranslation } from "react-i18next"
import { RouteComponentProps } from "react-router-dom"

type TParams = { dapp_slug: string }

export function DappDetails({
  match,
}: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()
  const { dapp } = useDapp()

  return (
    <div className="container mx-auto">
      <h2 className="text-3xl pt-2">
        {t("DAPP_DETAILS_TITLE")} {match.params.dapp_slug}
      </h2>
      {dapp.basic.status}
      <ListDappLogs dappLogsList={dapp.dappLogsList} viewAllLogs={false} />
      <ThreeSubscriptions></ThreeSubscriptions>

    </div>
  )
}
