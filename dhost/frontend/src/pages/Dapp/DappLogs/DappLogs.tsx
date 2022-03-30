import { listDappsLogs } from "api/DappLogs"
import { useDapp } from "contexts/DappContext/DappContext"
import { DappLogs as DL } from "models/api/DappLogs"
import { NotFound } from "pages/NotFound"
import { useEffect, useState } from "react"
import { useTranslation } from "react-i18next"
import {
  BrowserRouter as Router,
  Switch,
  Route,
  useRouteMatch,
  RouteComponentProps,
} from "react-router-dom"
import { DappLogsList } from "./DappLogsList"
type TParams = { dapp_slug: string }

export function DappLogs({
  match,
}: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()
  const { path } = useRouteMatch()
  const { dapp, setDapp } = useDapp();

  function renderWells() {
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

  return (
    renderWells()
  )
}
