import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'

import Home from './pages/Home'
import { DappReadOnlyList } from './pages/Dapp'
import { IPFSDapp } from './pages/IPFSDapp'
import NotFound from './pages/NotFound'

import Header from './components/Header'
import Dappbar from './components/Dappbar'
import Navbar from './components/Navbar'
import Footer from './components/Footer'

function RouterOutlet(): React.ReactElement {
  return (
    <BrowserRouter>
      <Header />
      <Dappbar />
      <Navbar />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/dapps" component={DappReadOnlyList} />
        <Route path="/ipfs" component={IPFSDapp} />
        <Route path="*" component={NotFound} />
      </Switch>
      <Footer />
    </BrowserRouter>
  )
}

export default RouterOutlet
