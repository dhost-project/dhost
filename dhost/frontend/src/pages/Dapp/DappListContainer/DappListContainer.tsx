import { useEffect } from "react"
import { useTranslation } from "react-i18next"
import {
  BrowserRouter as Router,
  Switch,
  Route,
  useRouteMatch,
  useLocation,
  useParams,
} from "react-router-dom"
import { retrieveBuildOptions } from "api/BuildOptions"
import { listDappsLogs } from "api/DappLogs"
import { retrieveEnvVars } from "api/EnvVars"
import { retrieveIPFSDapp } from "api/IPFSDapps"
import { Dappbar } from "components/Dappbar"
import { ListDapp } from "components/ListDapp"
import { useDapp } from "contexts/DappContext/DappContext"
import { useUserContext } from "contexts/UserContext/UserContext"
import { BuildOptions } from "models/api/BuildOptions"
import { DappLogs } from "models/api/DappLogs"
import { EnvVar } from "models/api/EnvVar"
import { IPFSDapp } from "models/api/IPFSDapp"
import { NotFound } from "pages/NotFound"
import {
  DappDeploy as IPFSDappDeploy,
  DappDetails as IPFSDappDetails,
  DappSettings as IPFSDappEdit,
  DappSource as IPFSDappSource,
  DappLogs as IPFSDappLogs,
} from ".."
import { TParams } from "../DappDeploy"

function DappDetail(): React.ReactElement {
  const { path } = useRouteMatch()
  const { dapp, setDapp } = useDapp()
  const { dapp_slug } = useParams<TParams>()

  const fetchDapp = async () => {
    let envs: EnvVar[]
    try {
      let envs_resp = await retrieveEnvVars(dapp_slug)
      envs = envs_resp.data ?? []
    } catch (error) {
      envs = []
    }
    try {
      let basic_resp = await retrieveIPFSDapp(dapp_slug)
      let basic: IPFSDapp = basic_resp.data

      let build_resp = await retrieveBuildOptions(dapp_slug)
      let build: BuildOptions = build_resp.data[0]
      build = build == undefined ? { command: "", docker: "" } : build

      let dappLogsList: DappLogs[] = []
      let dappLogsList_resp = await listDappsLogs(basic.slug)

      dappLogsList = dappLogsList_resp.data

      let _dapp = {
        basic: basic,
        build: build,
        env_vars: envs,
        dappLogsList: dappLogsList,
      }

      setDapp((dapp) => ({
        ...dapp,
        basic: _dapp.basic,
        build: _dapp.build,
        env_vars: _dapp.env_vars,
        dappLogsList: _dapp.dappLogsList,
      }))
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    fetchDapp()
  }, [path])

  return (
    <Router>
      <Dappbar />
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

  const { userInfo } = useUserContext()

  return (
    <Router>
      <Switch>
        <Route
          exact
          path={`${path}/`}
          component={() => <ListDapp dapps={userInfo.dapps} />}
        />
        <Route path={`${path}/:dapp_slug`} component={() => <DappDetail />} />
        <Route path="*" component={NotFound} />
      </Switch>
    </Router>
  )
}
