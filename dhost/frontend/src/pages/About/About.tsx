import Container from "react-bootstrap/Container"
import { useTranslation } from "react-i18next"

function About(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <Container>
      <h2>{t("ABOUT_TITLE")}</h2>
    </Container>
  )
}

export default About
