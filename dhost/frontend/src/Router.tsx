import React from "react"
import { BrowserRouter, Switch, Route } from "react-router-dom"

import About from "pages/About"
import Account from "pages/Account"
import { DappReadOnlyList } from "pages/Dapp"
import Home from "pages/Home"
import IPFSDapp from "pages/IPFSDapp"
import NotFound from "pages/NotFound"

function RouterOutlet(): React.ReactElement {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/about" exact component={About} />
        <Route path="/account" component={Account} />
        <Route path="/dapps" component={DappReadOnlyList} />
        <Route path="/ipfs" component={IPFSDapp} />
        <Route path="*" component={NotFound} />
      </Switch>
    </BrowserRouter>
  )
}

export default RouterOutlet
