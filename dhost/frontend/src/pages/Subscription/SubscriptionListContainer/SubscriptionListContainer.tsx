import { useTranslation } from "react-i18next"
import { ListDapp } from "components/ListDapp"
import {
    BrowserRouter as Router,
    Switch,
    Route,
    useRouteMatch,
} from "react-router-dom"

import { NotFound } from "pages/NotFound"

import { useUserContext } from "contexts/UserContext/UserContext"

import { ThreeSubscriptions } from "components/Subscription/ThreeSubscriptions"
import { useEffect } from "react"

function SubscriptionDetail(): React.ReactElement {
    const { path } = useRouteMatch()
    const name = window.location.pathname.split("/")[2];

    useEffect(() => {
        console.log(name)
    }, [])


    return (
        <></>
    )
}

export function SubscriptionListContainer(): React.ReactElement {
    const { t } = useTranslation()

    const { path } = useRouteMatch()

    const { userInfo, setUserInfo } = useUserContext()

    return (
        <Router>
            <Switch>
                <Route exact path={`${path}/`}
                    component={() => <ThreeSubscriptions />} />
                <Route path={`${path}/:subscription_name`} component={() => <SubscriptionDetail />} />
                <Route path="*" component={NotFound} />
            </Switch>
        </Router>
    )
}
