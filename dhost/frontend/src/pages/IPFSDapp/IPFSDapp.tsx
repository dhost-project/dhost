import {
  BrowserRouter as Router,
  Switch,
  Route,
  useRouteMatch,
} from "react-router-dom"

import Dappbar from "components/Dappbar"

import NotFound from "pages/NotFound"

import {
  IPFSDappDeploy,
  IPFSDappDetails,
  IPFSDappFiles,
  IPFSDappList,
  IPFSDappLogs,
  IPFSDappEdit,
} from "."

function IPFSDappDetail(): React.ReactElement {
  const { path } = useRouteMatch()

  return (
    <Router>
      <Dappbar />
      <div className="container mx-auto">
        <Switch>
          <Route exact path={`${path}/`} component={IPFSDappDetails} />
          <Route path={`${path}/deploy`} component={IPFSDappDeploy} />
          <Route path={`${path}/logs`} component={IPFSDappLogs} />
          <Route path={`${path}/settings`} component={IPFSDappEdit} />
          <Route path={`${path}/files`} component={IPFSDappFiles} />
          <Route path="*" component={NotFound} />
        </Switch>
      </div>
    </Router>
  )
}

function IPFSDapp(): React.ReactElement {
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

export default IPFSDapp
