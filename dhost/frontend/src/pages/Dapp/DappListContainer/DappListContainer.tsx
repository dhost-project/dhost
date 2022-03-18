import { useTranslation } from "react-i18next"
import { ListDapp } from "components/ListDapp"
import {
  BrowserRouter as Router,
  Switch,
  Route,
  useRouteMatch,
} from "react-router-dom"
import { Dappbar } from "components/Dappbar"
import { NotFound } from "pages/NotFound"
import {
  DappDeploy as IPFSDappDeploy,
  DappDetails as IPFSDappDetails,
  DappSettings as IPFSDappEdit,
  DappSource as IPFSDappSource,
  DappLogs as IPFSDappLogs,
} from ".."
import { useEffect, useState } from "react"
import { IDapp, useDapp } from "contexts/DappContext/DappContext"
import { DappDetails } from "../DappDetails"
import { listIPFSDapps } from "api/IPFSDapps"
import { listDapps, retrieveDapp } from "api/Dapps"
import { Dapp } from "models/api/Dapp"
import { retrieveGithubOptions } from "api/GithubOptions"
import { retrieveBuildOptions } from "api/BuildOptions"

const dapps = [
  {
    slug: "dhost_v2",
    owner: "dumbo",
  },
  {
    slug: "dhost_v3",
    owner: "dumbo",
  },
  {
    slug: "dhost_v4",
    owner: "dumbo",
  },
]

function DappDetail(): React.ReactElement {
  const { path } = useRouteMatch()
  const { dapp, setDapp } = useDapp()
  const slug = window.location.pathname.split("/")[2];

  const fetchDapp = async () => {
    try {
      console.log(slug)
      let basic = retrieveDapp(slug)
      let github = retrieveGithubOptions(slug)
      let build = retrieveBuildOptions(slug)
      // let envs = retr
      console.log(basic, github, build)
    }
    catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    fetchDapp()
  }, [path])

  return (
    <Router>
      <Dappbar dapp={dapp} />
      <div className="container mx-auto">
        <Switch>
          <Route exact path={`${path}/`} component={IPFSDappDetails} />
          <Route path={`${path}/deploy`} component={IPFSDappDeploy} />
          <Route path={`${path}/logs`} component={IPFSDappLogs} />
          <Route path={`${path}/settings`} component={IPFSDappEdit} />
          <Route path={`${path}/source`} component={IPFSDappSource} />
          <Route path="*" component={NotFound} />
        </Switch>
      </div>
    </Router>
  )
}

export function DappListContainer(): React.ReactElement {
  const { t } = useTranslation()

  const { path } = useRouteMatch()

  const [dapp, setDapp] = useState<Dapp>({
    slug: "",
    url: "",
    owner: "",
    status: "",
    created_at: ""
  })

  const [dapps, setDapps] = useState<Dapp[]>([{
    slug: "",
    url: "",
    owner: "",
    status: "",
    created_at: ""
  }])
  let dataLoaded = false;

  const fetchDapps = async () => {
    try {
      const response = await listDapps()
      const data = response.data
      console.log(data)
      setDapps(data)
      dataLoaded = true;
    } catch (error) {
      console.log("error", error)
    }
  }

  useEffect(() => {
    if (!dataLoaded) {
      fetchDapps();
    }
  }, [])

  return (
    <Router>
      <Switch>
        <Route exact path={`${path}/`}
          component={() => <ListDapp dapps={dapps} setDapps={setDapps} />} />
        <Route path={`${path}/:dapp_slug`} component={() => <DappDetail />} />
        <Route path="*" component={NotFound} />
      </Switch>
    </Router>
  )
}
