import { useTranslation } from "react-i18next"
import { toast } from "react-toastify"

export default function Home(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div className="container mx-auto">
      <button
        onClick={() =>
          toast.error("Error 404", { position: toast.POSITION.BOTTOM_RIGHT })
        }
      >
        Notification test
      </button>
      <h2>{t("HOME_TITLE")}</h2>
    </div>
  )
}
