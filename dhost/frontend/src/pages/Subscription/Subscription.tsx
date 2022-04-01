import {
    BrowserRouter as Router,
    Switch,
    Route,
    useRouteMatch,
} from "react-router-dom"
import { ThreeSubscriptions } from "components/Subscription/ThreeSubscriptions"

export function Subscription(): React.ReactElement {
    const { path } = useRouteMatch()

    return (
        <>
            <ThreeSubscriptions></ThreeSubscriptions>
        </>
    )
}
