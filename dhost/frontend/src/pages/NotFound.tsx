import Container from "react-bootstrap/Container"
import { useTranslation } from "react-i18next"

function NotFound(): React.ReactElement {
  const { t } = useTranslation()

  const style404 = {
    fontSize: "10rem",
  }

  const style404Text = {
    fontSize: "3rem",
  }

  return (
    <Container>
      <div className="text-center">
        <h1 style={style404}>404</h1>
        <h2 style={style404Text}>{t("Page not found.")}</h2>
      </div>
    </Container>
  )
}

export default NotFound
