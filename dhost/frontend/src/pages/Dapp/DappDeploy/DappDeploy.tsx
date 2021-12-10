import { Dispatch, SetStateAction, useState } from "react"
import { GithubDeploy, HerokuDeploy } from "components/DappDeploy";
import { useTranslation } from "react-i18next"
import { RouteComponentProps } from "react-router-dom"

export enum EDeployMethodIds {
  Heroku = "heroku",
  Github = "github",
}

export type TParams = { dapp_slug: string }

export type TListDeploymethodsParams = {
  setSelectedDeployMethod: Dispatch<SetStateAction<string>>
  isDeployMethod: (i: string) => boolean
}

export type TDeployMethods = {
  id: EDeployMethodIds | string
  title: string
  description: string
}

export type TDeploymentProcesses = {
  [deployMethodsId: string]: {
    component: JSX.Element
  }
}

const deployMethods: TDeployMethods[] = [
  {
    id: "heroku",
    title: "Heroku Git",
    description: "Use Heroku CLI",
  },
  {
    id: "github",
    title: "Github",
    description: "Connect to Github",
  },
]

const deploymentProcessMap: TDeploymentProcesses = {
  github: {
    component: <GithubDeploy />
  },
  heroku: {
    component: <HerokuDeploy />
  },
}

export function ListDeploymethods({
  setSelectedDeployMethod,
  isDeployMethod,
}: TListDeploymethodsParams) {
  return (
    <>
      {deployMethods.map((item, i) => (
        <div
          key={`${item.title}-${i}`}
          className={`mr-4 pb-3 pt-3 pl-4 pr-4 cursor-pointer rounded ${
            isDeployMethod(item.id) ? "border-1 shadow-sm" : ""
          }`}
          onClick={() => setSelectedDeployMethod(item.id)}
        >
          <h3 className="text-sm font-medium">{item.title}</h3>
          <p className="text-xs">{item.description}</p>
        </div>
      ))}
    </>
  )
}

export function DappDeploy({
  match,
}: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()
  const [selectedDeployMethod, setSelectedDeployMethod] = useState<string>(
    deployMethods[0].id   // default to heroku
    // ""                 // no default selection
  )

  function isDeployMethod(i: string) {
    return selectedDeployMethod === i
  }

  return (
    <div className="container mx-auto">
      <section className="grid-5-10 p-4 border-b-1 border-gray-200">
        <div className="pr-10">
          <h2 className="font-normal text-green-500">{t("DEPLOY_METHOD")}</h2>
        </div>
        <div className="flex">
          <ListDeploymethods
            setSelectedDeployMethod={setSelectedDeployMethod}
            isDeployMethod={isDeployMethod}
          />
        </div>
      </section>

      {deploymentProcessMap[selectedDeployMethod]?.component}
    </div>
  )
}
