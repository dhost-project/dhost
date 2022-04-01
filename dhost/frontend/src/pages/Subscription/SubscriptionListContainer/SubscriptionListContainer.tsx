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
import { useEffect, useState } from "react"

const subscriptions = {
    "Discovery": {
        name: "Discovery",
        description: "entièrement gratuite et sans engagement, vous permet de créer un site de 5 pages et de réserver en option un nom de domaine pour votre site.",
        price: "Free",
        savings: ""
    },
    "Blog":
    {
        name: "Blog",
        description: " vous permet de créer un site avec un nombre de pages illimité, un accès illimité au module Blog, et un nom de domaine inclus.",
        price: "5.99€TTC/Mois",
        savings: "47.50€/2ans"
    },
    "Premium":
    {
        name: "Premium",
        description: "vous permet de créer un site illimité (avec modules blog, formulaires, commentaires, forum, newsletter, réseaux sociaux, etc.) et de réserver gratuitement votre nom de domaine.",
        price: "11.99€TTC/Mois",
        savings: "95.90€/2ans"
    }
}

function SubscriptionDetail(): React.ReactElement {
    const { path } = useRouteMatch()
    const name = window.location.pathname.split("/")[2];
    const [state, setState] = useState({
        name: "",
        description: "",
        price: "",
        savings: ""
    })

    useEffect(() => {
        console.log(name)
        setState(selectSubscription(name))
    }, [])

    const selectSubscription = (name: string) => {
        switch (name) {
            case "Discovery":
                return subscriptions.Discovery;
                break;
            case "Blog":
                return subscriptions.Blog;
                break;
            case "Premium":
                return subscriptions.Premium;
                break;
            default:
                return subscriptions.Discovery;
        }
    }


    return (
        <>{state.name} {state.price}</>

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
