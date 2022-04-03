import React from "react"
import { Switch, Route } from "react-router-dom"
import { About } from "pages/About"
import { Account } from "pages/Account"
import { DappDetails, DappListContainer } from "pages/Dapp"
import { Home } from "pages/Home"
import { Login } from "pages/Login"
import { NotFound } from "pages/NotFound"
import { Notification } from "pages/Notification"
import { SubscriptionListContainer } from "pages/Subscription/SubscriptionListContainer"
import { SignUp } from "pages/SignUp"

export function RouterOutlet(): React.ReactElement {
  return (
    <Switch>
      <Route path="/" exact component={Home} />
      <Route path="/about" exact component={About} />
      <Route path="/account" component={Account} />
      <Route path="/dapps" component={DappListContainer} />
      {/* <Route path="/dapp" component={IPFSDapp} /> */}
      {/* <Route path="/ipfs" component={IPFSDapp} /> */}
      <Route path="/notifications" component={Notification} />
      <Route path="/login" component={Login} />
      <Route path="/signup" component={SignUp} />
      <Route path="/pricing" component={SubscriptionListContainer} />
      <Route path="*" component={NotFound} />
    </Switch>
  )
}
