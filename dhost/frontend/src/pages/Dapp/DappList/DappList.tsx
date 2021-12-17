import { useTranslation } from "react-i18next"
import { ListDapp } from "components/ListDapp"
import { useDapp } from "contexts/DappContext/DappContext"
import { useEffect } from "react"
import { listDapps } from "api/Dapps"
import { listIPFSDapps } from "api/IPFSDapps"

const dapps = [
  {
    slug: "dhost_v2",
    owner: "dumbo",
  },
  {
    slug: "dhost_v3",
    owner: "dumbo",
  },
  {
    slug: "dhost_v4",
    owner: "dumbo",
  },
]

var list = []

export function DappList(): React.ReactElement {
  const { t } = useTranslation()
  return (
    <div className="container mx-auto">
      <h2>{t("DAPP_LIST_TITLE")}</h2>
      <ListDapp dapps={dapps} />
    </div>
  )
}
