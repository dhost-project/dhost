import Container from "react-bootstrap/Container"
import { useTranslation } from "react-i18next"

function DeleteConfirm(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <Container>
      <h2>{t("ACCOUNT_DELETE_CONFIRM_TITLE")}</h2>
    </Container>
  )
}

export default DeleteConfirm
