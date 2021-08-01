import { useTranslation } from "react-i18next"

export default function Home(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div className="container mx-auto">
      <h2>{t("HOME_TITLE")}</h2>
    </div>
  )
}
