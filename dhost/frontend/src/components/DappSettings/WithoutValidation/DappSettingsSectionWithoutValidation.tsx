import { ButtonHTMLAttributes, ReactEventHandler } from "react"
import { toast } from "react-toastify"
import { DappProvider, useDapp } from "contexts/DappContext/DappContext"

type TParams = { dapp_slug: string }

export function DappSettingsSectionWithoutValidation(props: {
  component: React.ReactElement
  short: string
  name: string
}): React.ReactElement {
  const { dapp, setDapp } = useDapp()

  return (
    <div>
      <div className="w-1/3">{props.component}</div>
    </div>
  )
}
