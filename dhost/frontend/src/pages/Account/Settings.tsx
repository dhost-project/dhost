import { useTranslation } from "react-i18next"

export default function AccountSettings(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div className="container mx-auto">
      <h2>{t("ACCOUNT_SETTINGS_TITLE")}</h2>
      <a className="btn btn-danger" href="/account/delete-confirm">
        Delete account
      </a>
    </div>
  )
}
