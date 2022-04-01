import { env } from "environment"
import { Subscription as SubscriptionType } from "models/api/Subscription"
import { useState } from "react"
import { http } from "utils/http"
import { Subscription } from "./Subscription"


export const subscriptions = [
    {
        name: "Discovery",
        description: "entièrement gratuite et sans engagement, vous permet de créer un site de 5 pages et de réserver en option un nom de domaine pour votre site.",
        price: "Free",
        savings: ""
    },
    {
        name: "Blog",
        description: " vous permet de créer un site avec un nombre de pages illimité, un accès illimité au module Blog, et un nom de domaine inclus.",
        price: "5.99€TTC/Mois",
        savings: "47.50€/2ans"
    },
    {
        name: "Premium",
        description: "vous permet de créer un site illimité (avec modules blog, formulaires, commentaires, forum, newsletter, réseaux sociaux, etc.) et de réserver gratuitement votre nom de domaine.",
        price: "11.99€TTC/Mois",
        savings: "95.90€/2ans"
    }
]

export function ThreeSubscriptions() {

    return (
        <>
            <div className="mt-3 block">
                <hr className="mt-4 mb-3" />
                <div className="mx-5">
                    {subscriptions.map((subscription) => (
                        <Subscription subscription={subscription}></Subscription>
                    ))}
                </div>
            </div>
        </>

    )
}
