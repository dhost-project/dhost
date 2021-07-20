import { useTranslation } from "react-i18next"
import { RouteComponentProps } from "react-router-dom"

import "./styles.scss"

type TParams = { dapp_slug: string }

function Deploy({ match }: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div>
      <h2>
        {t("DEPLOY_TITLE")} {match.params.dapp_slug}
      </h2>
    </div>
  )
}

export default Deploy
