import { env } from "environment"
import { Dapp } from "models/api/Dapp"
import { Subscription as SubscriptionType } from "models/api/Subscription"
import { useState } from "react"
import { useHistory } from "react-router-dom"
import { http } from "utils/http"

export function Subscription({ subscription }: { subscription: SubscriptionType }) {

    let history = useHistory()

    const handleSubscription = (_subscription: SubscriptionType) => {
        history.push(`/preview/${_subscription.name}`)
    }

    return (
        <>
            <button
                key={subscription.name}
                className="w-1/3 mb-3 mt-2 px-4 py-4 border-2 text-base text-gray-700 font-medium rounded-lg bg-white hover:bg-green-50 hover:border-green-400 focus:bg-green-50 focus:border-green-400 focus:ring-offset-0 focus:ring-green-400 focus:outline-none focus:ring-1 transition cursor-pointer"
                onClick={() => handleSubscription(subscription)}
            >
                <p className="uppercase">
                    <h3 style={{ textAlign: "left" }}>{subscription.name}</h3>
                </p>
                <hr className="mt-4 mb-3" />

                <p className="lower text-gray-500" style={{ textAlign: "left" }}>{subscription.price}</p>

                <p className="lowercase text-gray-500" style={{ textAlign: "left" }}>
                    {subscription.description}
                </p>
            </button>
        </>
    )
}
