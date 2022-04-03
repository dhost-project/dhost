import { useTranslation } from "react-i18next"

export function GetStarted(): React.ReactElement {
    const { t } = useTranslation()

    return (
        <div className="container mx-auto">
            <h1 className="text-2xl text-center" style={{ color: "rgb(0,120,80)" }}>Get Started</h1>
            <p className="italic">
                It will take less than five minutes to deploy your decentralized application (Dapp).
            </p>
            <p className="mt-3">
                First, click on <b style={{ color: "rgb(0,120,80)" }}>Create Dapp</b>, you have to choose a name and select the gateway you want to use.
            </p>
            <p className="mt-3">
                Then, you can upload and deploy the bundle ziped of your project, in the <b style={{ color: "rgb(0,120,80)" }}>Deploy tab</b>.
            </p>
            <p className="mt-3">
                In less than five minutes your app will be accessible on the ipfs. Check the <b style={{ color: "rgb(0,120,80)" }}>Overview</b> to get the link and a preview.
            </p>
            <p className="mt-3">
                You can change the gateway in the <b style={{ color: "rgb(0,120,80)" }}>Settings</b>, and deploy it again.
            </p>
        </div>
    )
}
