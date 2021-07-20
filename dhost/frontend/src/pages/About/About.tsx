import { useTranslation } from "react-i18next"

import "./styles.scss"

function About(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div>
      <h2>{t("ABOUT_TITLE")}</h2>
    </div>
  )
}

export default About
