import { FormEvent, useState } from "react"
import { Form } from "react-bootstrap"
import { useHistory } from "react-router-dom"
import { createIPFSDapp } from "api/IPFSDapps"
import { Button } from "components/Button"
import { IPFSDappParams } from "models/api/IPFSDapp"
import { useModals } from "contexts/ModalsContext/ModalsContext";
import { EnvVar } from "models/api/EnvVar"
import { useEnvVarModals } from "contexts/EnvVarModalsContext/EnvVarModalsContext"
import { env } from "environment"
import { IDapp, useDapp } from "contexts/DappContext/DappContext"
import { createEnvVar } from "api/EnvVars"


const initialEnvVar: EnvVar = {
    variable: "",
    value: "",
    sensitive: false
}

export function EnvVarCreateForm() {
    const { setShowCreateEnvVarModal } = useEnvVarModals()
    const [envVarForm, setEnvVarForm] = useState<EnvVar>({ ...initialEnvVar })
    const { dapp, setDapp } = useDapp();

    async function handleSubmit(e: FormEvent) {
        e.preventDefault()
        try {
            const res = await createEnvVar(dapp.basic.slug, envVarForm)
            if (res.statusText == "Created") {
                let envVars = dapp.env_vars
                envVars.push(envVarForm)
                setDapp(dapp => ({ ...dapp, env_vars: envVars }))
            }
            setShowCreateEnvVarModal(false)
        } catch (error) {
            console.warn(error)
        }
    }

    return (
        <Form
            onSubmit={handleSubmit}
            onClick={(e) => e.stopPropagation()}
            className="bg-white p-4 rounded shadow"
        >
            <Form.Label className="flex"><p className="flex-auto text-lg text-center">Create environment variable</p></Form.Label>
            <hr className="mb-4" />
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Variable</Form.Label>
                <Form.Control
                    type="text"
                    placeholder="Enter a name"
                    value={envVarForm.variable}
                    onChange={(e) => setEnvVarForm({ ...envVarForm, variable: e.target.value })}
                />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Value</Form.Label>
                <Form.Control
                    type="text"
                    placeholder="Enter a value"
                    value={envVarForm.value}
                    onChange={(e) => setEnvVarForm({ ...envVarForm, value: e.target.value })}
                />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Sensitive</Form.Label>
                <Form.Check
                    type="checkbox"
                    // value={envVarForm.sensitive}
                    checked={envVarForm.sensitive}
                    onChange={(e) =>
                        setEnvVarForm({ ...envVarForm, sensitive: !envVarForm.sensitive })
                    }
                />
            </Form.Group>

            <Button type="submit">Submit</Button>
        </Form>
    )
}
