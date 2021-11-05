import { BrowserRouter } from "react-router-dom"
import { ToastContainer } from "react-toastify"
import "react-toastify/dist/ReactToastify.min.css"

import { Footer } from "components/Footer"
import { Header } from "components/Header"
import { Navbar } from "components/Navbar"

import { RouterOutlet } from "./Router"

export default function App(): React.ReactElement {
  return (
    <BrowserRouter>
      <div className="flex flex-col min-h-screen justify-between">
        <div>
          <Header />
          <Navbar />
          <RouterOutlet />
          <ToastContainer />
        </div>
        <Footer />
      </div>
    </BrowserRouter>
  )
}
