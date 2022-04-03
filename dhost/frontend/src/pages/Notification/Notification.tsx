import {
  BrowserRouter as Router,
  Switch,
  Route,
  useRouteMatch,
} from "react-router-dom"
import { NotFound } from "pages/NotFound"
import { NotificationList, NotificationDetail } from "."
import { listNotifications } from "api/Notifications"
import { useEffect, useState } from "react"
import { useUserContext } from "contexts/UserContext/UserContext"

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
  const { userInfo, setUserInfo } = useUserContext()
  // const fetchData = async () => {
  //   try {
  //     const res = await listNotifications()
  //     let _notifications = res.data
  //     console.log(res.data)
  //     setUserInfo({n})

  //   }
  //   catch (error) {
  //     console.log(error)
  //   }
  // }

  useEffect(() => {
    console.log(userInfo)
  }, [userInfo])

  return (
    <Router>
      <Switch>
        <Route exact path={`${path}`}>
          <NotificationList />
        </Route>
        <Route path={`${path}/:notification_id`}>
          <NotificationDetail notification={userInfo.notifications[0]} />
        </Route>
        <Route path="*" component={NotFound} />
      </Switch>
    </Router>
  )
}
