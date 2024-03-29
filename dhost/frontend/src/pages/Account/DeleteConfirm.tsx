import { useTranslation } from "react-i18next"

export function DeleteConfirm(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div className="container mx-auto">
      <h2>{t("ACCOUNT_DELETE_CONFIRM_TITLE")}</h2>
    </div>
  )
}
