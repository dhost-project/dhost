import { useEffect, useState } from "react"
import {
  BrowserRouter as Router,
  Switch,
  Route,
  useRouteMatch,
} from "react-router-dom"
import { useDapp } from "contexts/DappContext/DappContext"
import { NotFound } from "pages/NotFound"
import { DappLogsList } from "./DappLogsList"

export function DappLogs(): React.ReactElement {
  const { path } = useRouteMatch()
  const { dapp } = useDapp()

  return (
    <div className="container mx-auto">
      <Router>
        <Switch>
          <Route exact path={`${path}`}>
            <DappLogsList dappLogs={dapp.dappLogsList} />
          </Route>
          {/* <Route path={`${path}/:notification_id`}>
              <NotificationDetail notification={notifications[0]} />
            </Route> */}
          <Route path="*" component={NotFound} />
        </Switch>
      </Router>
    </div>
  )
}
