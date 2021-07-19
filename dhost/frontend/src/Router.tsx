import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'

import Home from './pages/Home'
import { DappReadOnlyList } from './pages/Dapp'
import {
  IPFSDappIndex,
  IPFSDappDeploy,
  IPFSDappFiles,
  IPFSDappLogs,
  IPFSDappEdit,
} from './pages/IPFSDapp'
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
        <Route path="/dapps/" exact component={DappReadOnlyList} />
        <Route path="/ipfs/:slug/" exact component={IPFSDappIndex} />
        <Route path="/ipfs/:slug/deploy" exact component={IPFSDappDeploy} />
        <Route path="/ipfs/:slug/files" exact component={IPFSDappFiles} />
        <Route path="/ipfs/:slug/logs" exact component={IPFSDappLogs} />
        <Route path="/ipfs/:slug/settings" exact component={IPFSDappEdit} />
        <Route path="*" component={NotFound} />
      </Switch>
      <Footer />
    </BrowserRouter>
  )
}

export default RouterOutlet
