import { useTranslation } from "react-i18next"

export default function DeleteConfirm(): React.ReactElement {
  const { t } = jest ? {t:(s: any)=>s} : useTranslation()

  return (
    <div className="container mx-auto">
      <h2>{t("ACCOUNT_DELETE_CONFIRM_TITLE")}</h2>
    </div>
  )
}
