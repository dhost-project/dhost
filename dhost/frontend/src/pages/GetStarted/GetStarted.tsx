import { useTranslation } from "react-i18next"
import change_gateway from '../../assets/gs_change_gateway.png'
import toast_bundle from '../../assets/gs_toast_bundle.png'
import create_dapp from '../../assets/gs_change_gateway.png'


export function GetStarted(): React.ReactElement {
    const { t } = useTranslation()

    return (
        <div className="container mx-auto mt-5">
            <p className="text-4xl" style={{ color: "rgb(0,120,80)" }}>Get Started</p>

            <p className="text-xl italic">
                (less than five minutes)
            </p>
            <ul className="mt-8 list-disc">
                <li style={{ color: "rgb(0,120,80)" }}>
                    <span className="text-black">First, click on <b style={{ color: "rgb(0,120,80)" }}>Create Dapp</b>, you have to choose a name and select the gateway you want to use.</span>
                    <img className="border-2 mt-4 ml-8 mb-4" src={create_dapp} />
                </li>
                <li className="mt-3" style={{ color: "rgb(0,120,80)" }}>
                    <span className="text-black">Then, you can upload and deploy the bundle ziped of your project, in the <b style={{ color: "rgb(0,120,80)" }}>Deploy tab</b>.</span>
                    <img className="border-2 mt-4 ml-8 mb-4 " src={toast_bundle} />
                </li>
                <li className="mt-3" style={{ color: "rgb(0,120,80)" }}>
                    <span className="text-black">In less than five minutes your app will be accessible on the ipfs. Check the <b style={{ color: "rgb(0,120,80)" }}>Overview</b> to get the link and a preview.</span>
                </li>
                <li className="mt-3" style={{ color: "rgb(0,120,80)" }}>
                    <span className="text-black">You can change the gateway in the <b style={{ color: "rgb(0,120,80)" }}>Settings</b>, and deploy it again.</span>
                    <img className="border-2 mt-4 ml-8" src={change_gateway} />
                </li>
            </ul>
        </div>
    )
}
