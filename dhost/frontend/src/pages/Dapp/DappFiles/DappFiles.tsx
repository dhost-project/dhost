import { useTranslation } from "react-i18next"
import { RouteComponentProps } from "react-router-dom"

import "./styles.scss"

type TParams = { dapp_slug: string }

function Files({ match }: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div>
      <h2>
        {t("FILES_TITLE")} {match.params.dapp_slug}
      </h2>
    </div>
  )
}

export default Files
