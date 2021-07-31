import { useTranslation } from "react-i18next"
import { toast } from "react-toastify"

export default function Home(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div className="container mx-auto">
      <button onClick={() => toast("test")}>test</button>
      <h2>{t("HOME_TITLE")}</h2>
    </div>
  )
}
