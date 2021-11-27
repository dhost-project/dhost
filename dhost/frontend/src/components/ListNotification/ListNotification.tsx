import { Notification } from "models/api/Notification"
import { List } from "./List"
import { ListItem } from "./ListItem"

export function ListNotification({
  notifications,
}: {
  notifications: Notification[]
}): React.ReactElement {
  return (
    <List>
      {notifications.map((notification) => (
        <ListItem
          key={`${notification.id}-${notification.url}`}
          notification={notification}
        />
      ))}
    </List>
  )
}
