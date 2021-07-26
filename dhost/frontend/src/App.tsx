import Footer from "./components/Footer"
import Header from "./components/Header"
import Navbar from "./components/Navbar"

import "./App.css"
import RouterOutlet from "./Router"

function App(): React.ReactElement {
  return (
    <div id="footer-flex-wrapper">
      <div>
        <Header />
        <Navbar />
        <RouterOutlet />
      </div>
      <Footer />
    </div>
  )
}

export default App
