import {
  BrowserRouter as Router,
  Switch,
  Route,
  useRouteMatch,
} from "react-router-dom"

import { NotFound } from "pages/NotFound"

import { NotificationList, NotificationDetail } from "."

const notifications = [
  {
    id: "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    subject: "Auto build started",
    content: "Auto build started",
    read: false,
    level: "info",
    url: "/",
    timestamp: "2019-08-24T14:15:22Z",
  },
  {
    id: "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    subject: "Build failed.",
    content: "Build failed.",
    read: true,
    level: "error",
    url: "/",
    timestamp: "2019-08-24T14:15:22Z",
  },
  {
    id: "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    subject: "Options needed.",
    content: "Options needed.",
    read: true,
    level: "warning",
    url: "/",
    timestamp: "2019-08-24T14:15:22Z",
  },
  {
    id: "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    subject: "Auto build successful",
    content: "Auto build successful",
    read: false,
    level: "success",
    url: "/",
    timestamp: "2019-08-24T14:15:22Z",
  },
]

export function Notification(): React.ReactElement {
  const { path } = useRouteMatch()

  return (
    <Router>
      <Switch>
        <Route exact path={`${path}`}>
          <NotificationList notifications={notifications} />
        </Route>
        <Route path={`${path}/:notification_id`}>
          <NotificationDetail notification={notifications[0]} />
        </Route>
        <Route path="*" component={NotFound} />
      </Switch>
    </Router>
  )
}
