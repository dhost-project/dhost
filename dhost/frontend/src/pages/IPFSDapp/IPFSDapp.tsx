import Container from "react-bootstrap/Container"
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
import Dappbar from "./../../components/Dappbar"
import NotFound from "./../NotFound"

function IPFSDappDetail(): React.ReactElement {
  const { path } = useRouteMatch()

  return (
    <Router>
      <Dappbar />
      <Container>
        <Switch>
          <Route exact path={`${path}/`} component={IPFSDappIndex} />
          <Route path={`${path}/deploy`} component={IPFSDappDeploy} />
          <Route path={`${path}/logs`} component={IPFSDappLogs} />
          <Route path={`${path}/settings`} component={IPFSDappEdit} />
          <Route path={`${path}/files`} component={IPFSDappFiles} />
          <Route path="*" component={NotFound} />
        </Switch>
      </Container>
    </Router>
  )
}

function IPFSDapp(): React.ReactElement {
  const { path } = useRouteMatch()

  return (
    <Router>
      <Switch>
        <Route exact path={`${path}/`} component={IPFSDappIndex} />
        <Route path={`${path}/:dapp_slug`} component={IPFSDappDetail} />
        <Route path="*" component={NotFound} />
      </Switch>
    </Router>
  )
}

export default IPFSDapp