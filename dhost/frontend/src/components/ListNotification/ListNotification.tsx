import Notification from "models/Notification"

import List from "./List"
import ListItem from "./ListItem"

export default function ListNotification({
  notifications,
}: {
  notifications: Notification[]
}): React.ReactElement {
  return (
    <List>
      {notifications.map((notification) => (
        <ListItem notification={notification} />
      ))}
    </List>
  )
}
