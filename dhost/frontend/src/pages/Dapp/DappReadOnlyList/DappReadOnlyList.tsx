import { useTranslation } from "react-i18next"

import ListDapp from "components/ListDapp"

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

export default function DappReadOnlyList(): React.ReactElement {
  const { t } = jest ? {t:(s: any)=>s} : useTranslation()

  return (
    <div className="container mx-auto">
      <h2>{t("DAPP_READ_ONLY_LIST_TITLE")}</h2>
      <ListDapp dapps={dapps} />
    </div>
  )
}
