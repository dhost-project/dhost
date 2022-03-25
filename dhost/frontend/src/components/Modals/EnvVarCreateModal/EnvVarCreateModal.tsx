import { EnvVarCreateForm } from "components/Forms/EnvVarForms"
import { useEnvVarModals } from "contexts/EnvVarModalsContext/EnvVarModalsContext"

export function EnvVarCreateModal() {
    const { setShowCreateEnvVarModal } = useEnvVarModals()

    return (
        <div
            className="absolute z-50 top-0 left-0 w-full h-full flex justify-center items-center bg-gray-800 bg-opacity-50"
            onClick={() => setShowCreateEnvVarModal(false)}
        >
            <EnvVarCreateForm />
        </div>
    )
}
