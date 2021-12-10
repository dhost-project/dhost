import {
  BrowserRouter as Router,
  Switch,
  Route,
  useRouteMatch,
} from "react-router-dom"
import { Dappbar } from "components/Dappbar"
import { DappProvider } from "contexts/DappContext/DappContext"
import { NotFound } from "pages/NotFound"
import {
  DappDeploy as IPFSDappDeploy,
  DappDetails as IPFSDappDetails,
  DappSettings as IPFSDappEdit,
  DappSource as IPFSDappSource,
  DappList as IPFSDappList,
  DappLogs as IPFSDappLogs,
} from "."

const dapp = {
  slug: "dhost_v2",
  owner: "john",
}

// TODO : check if dapp slug actually exist & prevent access to other people dapps
function IPFSDappDetail(): React.ReactElement {
  const { path } = useRouteMatch()

  return (
    <Router>
      <Dappbar dapp={dapp} />
      <div className="container mx-auto">
        <Switch>
          <Route exact path={`${path}/`} component={IPFSDappDetails} />
          <Route path={`${path}/deploy`} component={IPFSDappDeploy} />
          <Route path={`${path}/logs`} component={IPFSDappLogs} />
          <DappProvider>
            <Route path={`${path}/settings`} component={IPFSDappEdit} />
          </DappProvider>
          <Route path={`${path}/source`} component={IPFSDappSource} />
          <Route path="*" component={NotFound} />
        </Switch>
      </div>
    </Router>
  )
}

export function IPFSDapp(): React.ReactElement {
  const { path } = useRouteMatch()

  return (
    <Router>
      <Switch>
        <Route exact path={`${path}/`} component={IPFSDappList} />
        <Route path={`${path}/:dapp_slug`} component={IPFSDappDetail} />
        <Route path="*" component={NotFound} />
      </Switch>
    </Router>
  )
}
