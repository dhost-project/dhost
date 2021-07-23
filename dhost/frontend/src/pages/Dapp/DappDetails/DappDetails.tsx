import { useTranslation } from "react-i18next"
import { RouteComponentProps } from "react-router-dom"

type TParams = { dapp_slug: string }

function DappDetails({ match }: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div>
      <h2>
        {t("DAPP_DETAILS_TITLE")} {match.params.dapp_slug}
      </h2>
    </div>
  )
}

export default DappDetails
