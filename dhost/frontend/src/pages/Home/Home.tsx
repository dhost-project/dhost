import Container from "react-bootstrap/Container"
import { useTranslation } from "react-i18next"

import "./styles.scss"

function Home(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <Container>
      <h2>{t("HOME_TITLE")}</h2>
    </Container>
  )
}

export default Home
