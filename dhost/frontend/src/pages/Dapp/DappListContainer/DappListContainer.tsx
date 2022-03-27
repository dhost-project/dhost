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
import { listIPFSDapps, retrieveIPFSDapp } from "api/IPFSDapps"
import { listDapps, retrieveDapp } from "api/Dapps"
import { Dapp } from "models/api/Dapp"
import { BuildOptions } from "models/api/BuildOptions"
import { retrieveGithubOptions } from "api/GithubOptions"
import { retrieveBuildOptions } from "api/BuildOptions"
import { IPFSDapp } from "models/api/IPFSDapp"
import { retrieveEnvVars } from "api/EnvVars"
import { EnvVar } from "models/api/EnvVar"

function DappDetail(): React.ReactElement {
  const { path } = useRouteMatch()
  const { dapp, setDapp } = useDapp()
  const slug = window.location.pathname.split("/")[2];

  const fetchDapp = async () => {
    try {
      let basic_resp = await retrieveIPFSDapp(slug)
      let basic: IPFSDapp = basic_resp.data
      // let github = await retrieveGithubOptions(slug)
      let build_resp = await retrieveBuildOptions(slug)
      // console.log("build", build_resp.data[0])
      let build: BuildOptions = build_resp.data[0]
      build = (build == undefined ? { command: "", docker: "" } : build)
      let envs_resp = (await retrieveEnvVars(dapp.basic.slug))
      let envs: EnvVar[] = envs_resp.data;
      console.log("envs_resp", envs_resp.data)
      console.log("envs", envs)

      let _dapp = {
        basic: basic,
        build: build,
        github: {
          repo: "",
          branch: 0,
          auto_deploy: false,
          confirm_ci: false
        },
        env_vars: [],
        current_slug: basic.slug
      }
      setDapp(_dapp)
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
          component={() => <ListDapp dapps={dapps} />} />
        <Route path={`${path}/:dapp_slug`} component={() => <DappDetail />} />
        <Route path="*" component={NotFound} />
      </Switch>
    </Router>
  )
}
