import { FormEvent, useState } from "react"
import { Form } from "react-bootstrap"
import { useHistory, useParams } from "react-router-dom"
import { destroyIPFSDapp } from "api/IPFSDapps"
import { Button } from "components/Button"
import { useModals } from "contexts/ModalsContext/ModalsContext"
import { DappDestroyParams } from "models/api/DappDestroyParams"
import { useUserContext } from "contexts/UserContext/UserContext"
import { TParams } from "pages/Dapp"
import { toast } from "react-toastify"

const initialDapp: DappDestroyParams = {
    slugConfirmation: ""
}

export function DappDestroyForm() {
    const history = useHistory()
    const { setShowDestroyDappModal } = useModals()
    const [dappForm, setDappForm] = useState<DappDestroyParams>({ ...initialDapp })

    async function handleSubmit(e: FormEvent) {
        e.preventDefault()
        try {
            const dapp_slug = window.location.pathname.split("/")[2]
            console.log(dappForm.slugConfirmation, dapp_slug)
            if (dappForm.slugConfirmation === dapp_slug) {
                await destroyIPFSDapp(dapp_slug)
                history.push(`/`)
                setShowDestroyDappModal(false)
                window.location.reload()
            }
            else {
                toast.error("You mistyped the slug.")
            }
        } catch (error) {
            console.warn(error)
            toast.error("Server error.")
        }
    }

    return (
        <Form
            onSubmit={handleSubmit}
            onClick={(e) => e.stopPropagation()}
            className="bg-white p-4 rounded shadow"
        >
            <Form.Label className="flex"><p className="flex-auto text-lg text-center">Confirm deletion</p></Form.Label>
            <hr className="mb-4" />
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Type the Dapp Slug</Form.Label>
                <Form.Control
                    type="text"
                    placeholder="Enter the Dapp slug"
                    value={dappForm.slugConfirmation}
                    onChange={(e) => setDappForm({ ...dappForm, slugConfirmation: e.target.value })}
                />
            </Form.Group>
            <Button type="submit">Destroy</Button>
        </Form>
    )
}
