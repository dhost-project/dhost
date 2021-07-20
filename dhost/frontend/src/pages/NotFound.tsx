import Container from "react-bootstrap/Container"
import { useTranslation } from "react-i18next"

function NotFound(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <Container>
      <h1 className="mx-auto">404</h1>
      <h2>{t("Page not found.")}</h2>
    </Container>
  )
}

export default NotFound
