import { useTranslation } from "react-i18next"

export default function DappList(): React.ReactElement {
  const { t } = useTranslation()

  return (
    <div className="container mx-auto">
      <h2>{t("DAPP_LIST_TITLE")}</h2>
      <ul>
        <li>
          <a href="/ipfs/dhost_v2">Dhost_v2</a>
        </li>
        <li>
          <a href="/ipfs/dhost_v3">Dhost_v3</a>
        </li>
        <li>
          <a href="/ipfs/dhost_v4">Dhost_v4</a>
        </li>
      </ul>
    </div>
  )
}
