import { DappProvider, useDapp } from "contexts/DappContext/DappContext";
import { ButtonHTMLAttributes, ReactEventHandler } from "react";
import { ButtonProps } from "components/Button";
import { toast } from "react-toastify";
import { ValidationButton } from "./ValidationButton";
import DappSettingsSectionTitle from "pages/Dapp/DappSettings/DappSettingsSectionTitle/DappSettingsSectionTitle";

type TParams = { dapp_slug: string }

export function DappSettingsSectionWithValidation(/*{ _component: React.ReactElement, _short: string, _name: string, _description: string }*/): React.ReactElement {

    const { dapp, setDapp } = useDapp();


    function displayData(e: React.MouseEvent<HTMLButtonElement>) {
        console.log(e.target);
        console.log(dapp);
        toast.info("Change done.", { position: toast.POSITION.BOTTOM_RIGHT })
    }

    return (<div></div>/*
        <div>
            <DappSettingsSectionTitle _name={props.name} _description={props.description}></DappSettingsSectionTitle>
            <div className="w-1/3">
                {props.component}
            </div>
            <div className="flex justify-center w-1/3">
                <ValidationButton dapp={dapp} setDapp={setDapp} short={props.short}></ValidationButton>
            </div>
        </div>*/
    )
}
