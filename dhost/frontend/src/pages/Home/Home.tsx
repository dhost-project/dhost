import { useTranslation } from "react-i18next"

import "./styles.scss"

function Home(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div>
      <h2>{t("HOME_TITLE")}</h2>
    </div>
  )
}

export default Home
