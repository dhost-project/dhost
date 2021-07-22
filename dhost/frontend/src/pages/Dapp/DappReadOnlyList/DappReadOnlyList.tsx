import Container from "react-bootstrap/Container"
import ListGroup from "react-bootstrap/ListGroup"
import { useTranslation } from "react-i18next"

function DappReadOnlyList(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <Container>
      <h2>{t("DAPP_READ_ONLY_LIST_TITLE")}</h2>
      <ListGroup variant="flush">
        <ListGroup.Item action href="/ipfs/dhost_v2">
          Dhost_v2
        </ListGroup.Item>
        <ListGroup.Item action href="/ipfs/dhost_v3">
          Dhost_v3
        </ListGroup.Item>
        <ListGroup.Item action href="/ipfs/dhost_v4">
          Dhost_v4
        </ListGroup.Item>
      </ListGroup>
    </Container>
  )
}

export default DappReadOnlyList
