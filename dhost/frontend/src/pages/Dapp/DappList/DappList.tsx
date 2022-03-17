import { useTranslation } from "react-i18next"
import { ListDapp } from "components/ListDapp"
import { useDapp } from "contexts/DappContext/DappContext"
import { useEffect } from "react"
import { listDapps } from "api/Dapps"
import { listIPFSDapps } from "api/IPFSDapps"


export function DappList(): React.ReactElement {
  const { t } = useTranslation()
  return (
    <div className="mx-auto">
      <h2>{t("DAPP_LIST_TITLE")}</h2>
      {/* <ListDapp/> */}
    </div>
  )
}
