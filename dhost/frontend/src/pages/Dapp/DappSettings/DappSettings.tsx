import { RouteComponentProps } from "react-router-dom"
import { toast } from "react-toastify"
import { useDapp } from "contexts/DappContext/DappContext"
import DappSettingsBasic from "./DappSettingsBasic/DappSettingsBasic"
import DappSettingsBuild from "./DappSettingsBuild/DappSettingsBuild"
import DappSettingsEnvVar from "./DappSettingsEnvVar/DappSettingsEnvVar"
import DappSettingsGithub from "./DappSettingsGithub/DappSettingsGithub"
import DappSettingsSectionTitle from "./DappSettingsSectionTitle/DappSettingsSectionTitle"
import { retrieveBuildOptions } from "api/BuildOptions"
import { useEffect } from "react"


type TParams = { dapp_slug: string }

export function DappSettings({
  match,
}: RouteComponentProps<TParams>): React.ReactElement {
  const { dapp, setDapp } = useDapp()

  function displayData(e: React.MouseEvent<HTMLButtonElement>) {
    toast.info("Change done.", { position: toast.POSITION.BOTTOM_RIGHT })
  }

  useEffect(() => {
    fetchingData()
  })

  const fetchingData = async () => {
    try {
      const response = await retrieveBuildOptions(dapp.basic.slug)
      const json = (await response).data
      dapp.build = json

    } catch (error) {
      console.log("error", error)
    }
  }

  const settings_sections = [
    /*{
      component: <DappSettingsSectionWithValidation
        _component={<DappSettingsBasic dapp={dapp} setDapp={setDapp}
        ></DappSettingsBasic>}
        _short="basic"
        _name="Basic"
        _description="Change major informations of your application.">
      </DappSettingsSectionWithValidation>

    },*/
    {
      name: "Basic",
      short: "basic",
      description: "Change major informations of your application.",
      component: (<DappSettingsBasic dapp={dapp} setDapp={setDapp}></DappSettingsBasic>) // <DappSettingsBasic dapp={dapp} setDapp={setDapp}></DappSettingsBasic>
    },
    {
      name: "Build",
      short: "build",
      description: "Adapt your build options to your needs.",
      component: (
        <DappSettingsBuild dapp={dapp} setDapp={setDapp}></DappSettingsBuild>
      ),
    },
    {
      name: "Github",
      short: "github",
      description: "Connect to your repository.",
      component: (
        <DappSettingsGithub dapp={dapp} setDapp={setDapp}></DappSettingsGithub>
      ),
    },
    {
      name: "Environment variables",
      short: "var",
      description: "Add, modify and delete your environment variables.",
      component: (
        <DappSettingsEnvVar dapp={dapp} setDapp={setDapp}></DappSettingsEnvVar>
      ),
    },
  ]

  return (
    <div className="container mx-auto">
      <div>
        <div className="content-center divide-y">
          {settings_sections.map((_section, i) => (
            <div className="md:flex p-8" key={`${_section.name}-${i}`}>
              <DappSettingsSectionTitle
                _name={_section.name}
                _description={_section.description}
              ></DappSettingsSectionTitle>
              {_section.component}
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
