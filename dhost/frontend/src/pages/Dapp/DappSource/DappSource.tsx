import { retrieveIPFSDapp } from "api/IPFSDapps"
import { useDapp } from "contexts/DappContext/DappContext"
import { useEffect } from "react"
import { useTranslation } from "react-i18next"
import { RouteComponentProps } from "react-router-dom"

type TParams = { dapp_slug: string }

export function DappSource({
  match,
}: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()
  const { dapp } = useDapp()

  const fetchData = async () => {
    try {
      let res = await retrieveIPFSDapp(dapp.basic.slug)
      console.log(res)
    }
    catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    fetchData()
  }, [])

  return (
    <div className="container mx-auto">
      <h2>
        {t("FILES_TITLE")} {match.params.dapp_slug}
      </h2>
    </div>
  )
}
