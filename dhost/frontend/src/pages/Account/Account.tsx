import {
  BrowserRouter as Router,
  Switch,
  Route,
  useRouteMatch,
} from "react-router-dom"

import { AccountSettings, AccountDeleteConfirm } from "."
import NotFound from "./../NotFound"

export default function Account(): React.ReactElement {
  const { path } = useRouteMatch()

  return (
    <Router>
      <Switch>
        <Route path={`${path}/settings`} component={AccountSettings} />
        <Route
          path={`${path}/delete-confirm`}
          component={AccountDeleteConfirm}
        />
        <Route path="*" component={NotFound} />
      </Switch>
    </Router>
  )
}
