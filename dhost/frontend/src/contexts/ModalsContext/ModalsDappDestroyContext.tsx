import {
    createContext,
    Dispatch,
    FC,
    SetStateAction,
    useContext,
    useState,
} from "react"
import { DappDestroyModal } from "components/Modals"

interface ModalsContextType {
    showDestroyDappModal: boolean
    setShowDestroyDappModal: Dispatch<SetStateAction<boolean>>
}

export const ModalsDestroyDappContext = createContext({})

export const ModalsDestroyDappProvider: FC = ({ children }) => {
    const [showDestroyDappModal, setShowDestroyDappModal] = useState(false)

    return (
        <ModalsDestroyDappContext.Provider
            value={{ showDestroyDappModal, setShowDestroyDappModal }}
        >
            {children}
            {showDestroyDappModal && <DappDestroyModal />}
        </ModalsDestroyDappContext.Provider>
    )
}

export const useModals = () => useContext(ModalsDestroyDappContext) as ModalsContextType
