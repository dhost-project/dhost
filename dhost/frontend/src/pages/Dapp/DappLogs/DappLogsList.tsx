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

    useEffect(() => {
        console.log("CHOUILLABOUILLAA", dappLogs)
    }, [dappLogs])

    return (
        <div className="container mx-auto py-4">
            <div className="flex py-2">
                <Button size="sm">{t("Mark all as read")}</Button>
                <Button size="sm">{t("Mark all as un-read")}</Button>
            </div>
            <ListDappLogs dappLogsList={dappLogs} />
        </div>
    )
}
