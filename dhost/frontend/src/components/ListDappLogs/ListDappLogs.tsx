import { useEffect } from "react"
import { useDapp } from "contexts/DappContext/DappContext"
import { DappLogs } from "models/api/DappLogs"
import { List } from "./List"
import { ListItem } from "./ListItem"
import { User } from "models/api/User"

export function ListDappLogs({
    dappLogsList,
    viewAllLogs
}: {
    dappLogsList: DappLogs[],
    viewAllLogs: boolean
}): React.ReactElement {

    let { dapp } = useDapp()
    let dappLogsListOverview = dappLogsList.slice(0, 10)

    // let users: User[] = [];

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
            {viewAllLogs ?
                dappLogsList.map((dappLogs, i) => (
                    <ListItem
                        key={i}
                        dappLogs={dappLogs}
                    />
                ))
                :
                dappLogsListOverview.map((dappLogs, i) => (
                    <ListItem
                        key={i}
                        dappLogs={dappLogs}
                    />
                ))

            }
        </List>
    )
}
