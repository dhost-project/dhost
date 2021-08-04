import Notification from "models/Notification"
import Button from "components/Button"

import List from "./List"
import ListItem from "./ListItem"

export default function ListNotification({
  notifications,
}: {
  notifications: Notification[]
}): React.ReactElement {
  return (
    <div>
      <div className="flex py-2">
        <Button size="sm">Mark all has read</Button>
        <Button size="sm">Mark all has un-read</Button>
      </div>
      <List>
        {notifications.map((notification) => (
          <ListItem notification={notification} />
        ))}
      </List>
    </div>
  )
}
