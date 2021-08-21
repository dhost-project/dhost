import { useTranslation } from "react-i18next"

export function About(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div className="container mx-auto">
      <h2>{t("ABOUT_TITLE")}</h2>
    </div>
  )
}
