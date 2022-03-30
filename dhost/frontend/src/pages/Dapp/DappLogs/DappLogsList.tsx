import { SearchIcon } from "@heroicons/react/outline"
import { useTranslation } from "react-i18next"
import { Button } from "components/Button"
import { ListDappLogs } from "components/ListDappLogs"
import { DappLogs } from "models/api/DappLogs"
import { useEffect } from "react"

export function DappLogsList({
    dappLogs,
}: {
    dappLogs: DappLogs[]
}): React.ReactElement {
    const { t } = useTranslation()

    return (
        <div className="container mx-auto py-4">
            <ListDappLogs dappLogsList={dappLogs} viewAllLogs={true} />
        </div>
    )
}
