import React from "react"
import { BrowserRouter, Switch, Route } from "react-router-dom"

import About from "./pages/About"
import { DappReadOnlyList } from "./pages/Dapp"
import Home from "./pages/Home"
import IPFSDapp from "./pages/IPFSDapp"
import NotFound from "./pages/NotFound"

import Dappbar from "./components/Dappbar"
import Footer from "./components/Footer"
import Header from "./components/Header"
import Navbar from "./components/Navbar"

function RouterOutlet(): React.ReactElement {
  return (
    <BrowserRouter>
      <Header />
      <Navbar />
      <Dappbar />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/about" exact component={About} />
        <Route path="/dapps" component={DappReadOnlyList} />
        <Route path="/ipfs" component={IPFSDapp} />
        <Route path="*" component={NotFound} />
      </Switch>
      <Footer />
    </BrowserRouter>
  )
}

export default RouterOutlet
