import { useTranslation } from "react-i18next"
import { ListDapp } from "components/ListDapp"
import {
  BrowserRouter as Router,
  Switch,
  Route,
  useRouteMatch,
} from "react-router-dom"
import { Dappbar } from "components/Dappbar"
import { NotFound } from "pages/NotFound"
import {
  DappDeploy as IPFSDappDeploy,
  DappDetails as IPFSDappDetails,
  DappSettings as IPFSDappEdit,
  DappSource as IPFSDappSource,
  DappLogs as IPFSDappLogs,
} from ".."
import { useState } from "react"
import { IDapp } from "contexts/DappContext/DappContext"
import { DappDetails } from "../DappDetails"

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

function DappDetail(dapp: any): React.ReactElement {
  const { path } = useRouteMatch()



  return (
    <Router>
      <Dappbar dapp={dapp} />
      <div className="container mx-auto">
        <Switch>
          <Route exact path={`${path}/`} component={IPFSDappDetails} />
          <Route path={`${path}/deploy`} component={IPFSDappDeploy} />
          <Route path={`${path}/logs`} component={IPFSDappLogs} />
          <Route path={`${path}/settings`} component={IPFSDappEdit} />
          <Route path={`${path}/source`} component={IPFSDappSource} />
          <Route path="*" component={NotFound} />
        </Switch>
      </div>
    </Router>
  )
}

export function DappListContainer(): React.ReactElement {
  const { t } = useTranslation()

  const { path } = useRouteMatch()

  const [dapps, setDapps] = useState<IDapp[]>([{
    basic: {
      slug: "dapp_1",
      url: "gateway.com",
      owner: "filipo",
      status: "down",
      created_at: "08/08/08",
    },
    build: {
      command: "npm install",
      docker: "Dockerfile",
    },
    github: {
      repo: "best_repo",
      branch: 2,
      auto_deploy: false,
      confirm_ci: false,
    },
    env_vars: [
      {
        variable: "first_var",
        value: "val_var",
        sensitive: false,
      },
      {
        variable: "sec_var",
        value: "val_var",
        sensitive: true,
      },
    ],
  }])

  const [currentDapp, setCurrentDapp] = useState<IDapp>({
    basic: {
      slug: "dapp_1",
      url: "gateway.com",
      owner: "filipo",
      status: "down",
      created_at: "08/08/08",
    },
    build: {
      command: "npm install",
      docker: "Dockerfile",
    },
    github: {
      repo: "best_repo",
      branch: 2,
      auto_deploy: false,
      confirm_ci: false,
    },
    env_vars: [
      {
        variable: "first_var",
        value: "val_var",
        sensitive: false,
      },
      {
        variable: "sec_var",
        value: "val_var",
        sensitive: true,
      },
    ],
  })

  return (
    <Router>
      <Switch>
        <Route exact path={`${path}/`}
          component={() => <ListDapp dapps={dapps} setDapps={setDapps} setDapp={setCurrentDapp} />} />
        <Route path={`${path}/:dapp_slug`} component={() => <DappDetail dapp={currentDapp} />} />
        <Route path="*" component={NotFound} />
      </Switch>
    </Router>
  )
  // return (
  //   <div className="container mx-auto">
  //     <h2>{t("DAPP_READ_ONLY_LIST_TITLE")}</h2>
  //     <ListDapp dapps={dapps} />
  //   </div>
  // )
}
