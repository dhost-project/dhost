import {
  BrowserRouter as Router,
  Switch,
  Route,
  useRouteMatch,
} from "react-router-dom"

import {
  DappDeploy as IPFSDappDeploy,
  DappFiles as IPFSDappFiles,
  DappLogs as IPFSDappLogs,
  DappIndex as IPFSDappIndex,
  DappEdit as IPFSDappEdit,
} from "../Dapp"

function IPFSDapp(): React.ReactElement {
  const { path } = useRouteMatch()

  return (
    <Router>
      <Switch>
        <Route exact path={path}>
          <h2>Dapp home.</h2>
        </Route>
        <Route exact path={`${path}/:dapp_slug/`} component={IPFSDappIndex} />
        <Route path={`${path}/:dapp_slug/deploy`} component={IPFSDappDeploy} />
        <Route path={`${path}/:dapp_slug/logs`} component={IPFSDappLogs} />
        <Route path={`${path}/:dapp_slug/settings`} component={IPFSDappEdit} />
        <Route path={`${path}/:dapp_slug/files`} component={IPFSDappFiles} />
        <Route path="*">
          <h2>Dapp not found</h2>
        </Route>
      </Switch>
    </Router>
  )
}

export default IPFSDapp
