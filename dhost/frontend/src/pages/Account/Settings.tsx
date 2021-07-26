import Container from "react-bootstrap/Container"
import { useTranslation } from "react-i18next"

function AccountSettings(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <Container>
      <h2>{t("ACCOUNT_SETTINGS_TITLE")}</h2>
      <a className="btn btn-danger" href="/account/delete-confirm">
        Delete account
      </a>
    </Container>
  )
}

export default AccountSettings
