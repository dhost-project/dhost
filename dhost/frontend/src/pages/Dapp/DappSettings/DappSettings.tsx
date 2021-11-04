import { useTranslation } from "react-i18next"
import { RouteComponentProps } from "react-router-dom"
import { DappProvider, useDapp } from "contexts/DappContext/DappContext";
import DappSettingsElement from "./DappSettingsElement/DappSettingsElement";
import DappSettingsBasic from "./DappSettingsBasic/DappSettingsBasic";
import DappSettingsGithub from "./DappSettingsGithub/DappSettingsGithub";
import DappSettingsBuild from "./DappSettingsBuild/DappSettingsBuild";
import DappSettingsEnvVar from "./DappSettingsEnvVar/DappSettingsEnvVar";
import { ButtonHTMLAttributes, ReactEventHandler } from "react";
import { ButtonProps } from "components/Button";
import { toast } from "react-toastify";

type TParams = { dapp_slug: string }

export function DappSettings({
  match,
}: RouteComponentProps<TParams>): React.ReactElement {
  const { t } = useTranslation()

  const informations = {
    name: match.params.dapp_slug,
    gateway: "gateway.com",
    command: "npm install",
    docker: "none",
    github_username: "patrick",
    github_repo: "cabane",
    github_auto_deploy: false,
    env_vars: ["toto", "tata"]
  }

  const {dapp, setDapp} = useDapp();


  function displayData(e: React.MouseEvent<HTMLButtonElement>) {
    console.log(e.target);
    console.log(dapp);
    toast.info("Change done.", { position: toast.POSITION.BOTTOM_RIGHT })
  }

  const settings_sections = [
    {
      name: "Basic",
      short: "basic",
      description: "Change major informations of your application.",
      component: <DappSettingsBasic dapp={dapp} setDapp={setDapp}></DappSettingsBasic>
    },
    {
      name: "Build",
      short: "build",
      description: "Adapt your build options to your needs.",
      component: <DappSettingsBuild dapp={dapp} setDapp={setDapp}></DappSettingsBuild>
    },
    {
      name: "Github",
      short: "github",
      description: "Connect to your repository.",
      component: <DappSettingsGithub dapp={dapp} setDapp={setDapp}></DappSettingsGithub>
    },
    {
      name: "Environment variables",
      short: "var",
      description: "Add, modify and delete your environment variables.",
      component: <DappSettingsEnvVar dapp={dapp} setDapp={setDapp}></DappSettingsEnvVar>
    }
  ]

  return (
    <div className="container mx-auto">
      <div>
        <div className="content-center divide-y">
          {settings_sections.map((_section) => (
            <div className="md:flex p-8">
              <div className="ml-0 w-1/3">
                <h1 className="text-lg">{_section.name}</h1>
                <a className="text-gray-500">{_section.description}</a>
              </div>
              <div className="w-1/3">
                {_section.component}
              </div>
              <div className="flex justify-center w-1/3">
                <div className="flex items-center">
                  <button 
                  id={_section.short}
                  className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" 
                  type="submit"
                  name={_section.name}
                  onClick={displayData}>
                    Validate
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
