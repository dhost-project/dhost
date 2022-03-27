import { DappLogs } from "models/api/DappLogs"
import { useEffect } from "react"
import { useTranslation } from "react-i18next"


export function ListItem({
    dappLogs,
}: {
    dappLogs: DappLogs,
}): React.ReactElement {
    const { t } = useTranslation()
    var colors;

    useEffect(() => {
        console.log("dappLogs", dappLogs)
    })

    switch (true) {
        case /success/.test(dappLogs.action_flag):
            colors =
                "bg-green-100 text-green-600 hover:bg-green-200 hover:text-green-700"
            break;
        case /error/.test(dappLogs.action_flag):
            colors = "bg-red-100 text-red-600 hover:bg-red-200 hover:text-red-700"
            break;
        default:
            colors = "bg-gray-100 text-gray-600 hover:bg-gray-200 hover:text-gray-700"
            break;
    }

    return (
        <a
            className={`${colors} px-4 py-2`}
            href={`/dappLogs/${dappLogs.id}/`}
        >
            {/* {dappLogs.user} */}
            {t(dappLogs.action_flag)}
            {dappLogs.change_message}
            <br />
            {new Date(dappLogs.action_time).toLocaleDateString()}
        </a>
    )
}
