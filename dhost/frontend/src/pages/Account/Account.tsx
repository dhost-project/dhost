import {
  BrowserRouter as Router,
  Switch,
  Route,
  useRouteMatch,
} from "react-router-dom"

import NotFound from "pages/NotFound"

import { AccountSettings, AccountDeleteConfirm } from "."

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
