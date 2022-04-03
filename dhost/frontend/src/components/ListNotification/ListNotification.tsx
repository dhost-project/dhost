import { useUserContext } from "contexts/UserContext/UserContext"
import { List } from "./List"
import { ListItem } from "./ListItem"

export function ListNotification(): React.ReactElement {
  const { userInfo } = useUserContext()
  return (
    <List>
      {userInfo.notifications.map((notification, i) => (
        <ListItem
          key={`${notification.id}-${i}`}
          notification={notification}
        />
      ))}
    </List>
  )
}
