import {
    createContext,
    Dispatch,
    FC,
    SetStateAction,
    useContext,
    useState,
} from "react"
import { EnvVarCreateModal } from "components/Modals"

interface EnvVarModalsContextType {
    showCreateDappModal: boolean
    setShowCreateEnvVarModal: Dispatch<SetStateAction<boolean>>
}

export const EnvVarModalsContext = createContext({})

export const EnvVarModalsProvider: FC = ({ children }) => {
    const [showCreateEnvVarModal, setShowCreateEnvVarModal] = useState(false)

    return (
        <EnvVarModalsContext.Provider
            value={{ showCreateEnvVarModal, setShowCreateEnvVarModal }}
        >
            {children}
            {showCreateEnvVarModal && <EnvVarCreateModal />}
        </EnvVarModalsContext.Provider>
    )
}

export const useEnvVarModals = () => useContext(EnvVarModalsContext) as EnvVarModalsContextType
