import { RouteComponentProps } from "react-router-dom"
import { toast } from "react-toastify"
import { useDapp } from "contexts/DappContext/DappContext"
import DappSettingsBuild from "./DappSettingsBuild/DappSettingsBuild"
import DappSettingsEnvVar from "./DappSettingsEnvVar/DappSettingsEnvVar"
import DappSettingsGithub from "./DappSettingsGithub/DappSettingsGithub"
import DappSettingsSectionTitle from "./DappSettingsSectionTitle/DappSettingsSectionTitle"

type TParams = { dapp_slug: string }

export function DappSettings({
  match,
}: RouteComponentProps<TParams>): React.ReactElement {
  const { dapp, setDapp } = useDapp()

  function displayData(e: React.MouseEvent<HTMLButtonElement>) {
    console.log(e.target)
    console.log(dapp)
    toast.info("Change done.", { position: toast.POSITION.BOTTOM_RIGHT })
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
      component: <DappSettingsBasic dapp={dapp} setDapp={setDapp}></DappSettingsBasic>
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
              <div className="w-1/3">{_section.component}</div>
              <div className="flex justify-center w-1/3">
                <div className="flex items-center">
                  <button
                    id={_section.short}
                    className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
                    type="submit"
                    name={_section.name}
                    onClick={displayData}
                  >
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
