import { FormEvent, useState } from "react"
import { Form } from "react-bootstrap"
import { useHistory } from "react-router-dom"
import { createIPFSDapp } from "api/IPFSDapps"
import { Button } from "components/Button"
import { IPFSDappParams } from "models/api/IPFSDapp"
import { useModals } from "contexts/ModalsContext/ModalsContext";
import { EnvVar } from "models/api/EnvVar"
import { useEnvVarModals } from "contexts/EnvVarModalsContext/EnvVarModalsContext"

const initialEnvVar: EnvVar = {
    variable: "",
    value: "",
    sensitive: false
}

export function EnvVarCreateForm() {
    const { setShowCreateEnvVarModal } = useEnvVarModals()
    const [envVarForm, setEnvVarForm] = useState<EnvVar>({ ...initialEnvVar })

    async function handleSubmit(e: FormEvent) {
        e.preventDefault()
        try {
            // const res = await createEnvVar(dappForm)
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
                <Form.Control
                    type="text"
                    placeholder=""
                    value={"titi"}
                    onChange={(e) =>
                        setEnvVarForm({ ...envVarForm, sensitive: true })
                    }
                />
            </Form.Group>

            <Button type="submit">Submit</Button>
        </Form>
    )
}
