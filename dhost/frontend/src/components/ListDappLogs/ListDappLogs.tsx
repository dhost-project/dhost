import { useEffect } from "react"
import { useDapp } from "contexts/DappContext/DappContext"
import { DappLogs } from "models/api/DappLogs"
import { List } from "./List"
import { ListItem } from "./ListItem"
import { User } from "models/api/User"

export function ListDappLogs({
    dappLogsList,
}: {
    dappLogsList: DappLogs[]
}): React.ReactElement {

    let { dapp } = useDapp()

    // let users: User[] = [];
    let messages = [];

    // const fetchData = () => {
    //     try {
    //         dappLogsList.map((dappLogs) => {
    //             let retrieveUser_resp = await retrieveUser(dappLogs.id: String)
    //             let user = retrieveUser_resp.data;
    //             dappLogs.user = user.name
    //         })
    //     }
    //     catch (error) {
    //         console.log(error)
    //     }
    // }

    // useEffect(() => {
    //     fetchData();
    // }, [dapp]);

    return (
        <List>
            {dappLogsList.map((dappLogs) => (
                <ListItem
                    // key={`${dapp.basic.slug}-${dappLogs.id}`}
                    dappLogs={dappLogs}
                />
            ))}
        </List>
    )
}
