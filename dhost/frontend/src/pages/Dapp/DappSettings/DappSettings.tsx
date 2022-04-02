import { useEffect } from "react"
import { RouteComponentProps } from "react-router-dom"
import { toast } from "react-toastify"
import { updateBuildOptions } from "api/BuildOptions"
import { updateIPFSDapp } from "api/IPFSDapps"
import { useDapp } from "contexts/DappContext/DappContext"
import { useModals } from "../../../contexts/ModalsContext/ModalsDappDestroyContext"
import DappSettingsBasic from "./DappSettingsBasic/DappSettingsBasic"
import DappSettingsBuild from "./DappSettingsBuild/DappSettingsBuild"
import DappSettingsEnvVar from "./DappSettingsEnvVar/DappSettingsEnvVar"
import DappSettingsSectionTitle from "./DappSettingsSectionTitle/DappSettingsSectionTitle"

type TParams = { dapp_slug: string }

export function DappSettings({
  match,
}: RouteComponentProps<TParams>): React.ReactElement {
  const { dapp, setDapp } = useDapp()
  const { setShowDestroyDappModal } = useModals()

  function displayData(e: React.MouseEvent<HTMLButtonElement>) {
    toast.info("Change done.", { position: toast.POSITION.BOTTOM_RIGHT })
  }

  const updateDapp = () => {
    updateBuildOptions(dapp.basic.slug, dapp.build)
    updateIPFSDapp(dapp.basic.slug, {
      slug: dapp.basic.slug,
      ipfs_gateway: dapp.basic.ipfs_gateway,
    })
    // updateDapp()
    toast.success("Settings changed.")
    setDapp((_dapp) => ({ ..._dapp, ...dapp }))
  }

  const settings_sections = [
    {
      name: "Basic",
      short: "basic",
      description: "Change major informations of your application.",
      component: (
        <DappSettingsBasic dapp={dapp} setDapp={setDapp}></DappSettingsBasic>
      ), // <DappSettingsBasic dapp={dapp} setDapp={setDapp}></DappSettingsBasic>
    },
    {
      name: "Build",
      short: "build",
      description: "Adapt your build options to your needs.",
      component: (
        <DappSettingsBuild dapp={dapp} setDapp={setDapp}></DappSettingsBuild>
      ),
    },
    // {
    //   name: "Github",
    //   short: "github",
    //   description: "Connect to your repository.",
    //   component: (
    //     <DappSettingsGithub dapp={dapp} setDapp={setDapp}></DappSettingsGithub>
    //   ),
    // },
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
      <div className="flex justify-end">
        <div className="flex items-center">
          <button
            id="build"
            className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
            type="submit"
            name="build"
            onClick={updateDapp}
          >
            Validate
          </button>
        </div>
      </div>
      <div className="flex justify-end">
        <div className="flex items-center">
          <button
            id="build"
            className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
            type="submit"
            name="build"
            onClick={() => {
              setShowDestroyDappModal(true)
            }}
          >
            Delete Dapp
          </button>
        </div>
      </div>
    </div>
  )
}
