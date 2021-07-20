import 'bootstrap/dist/css/bootstrap.css'
import i18n from 'i18next'
import { StrictMode } from 'react'
import ReactDOM from 'react-dom'
import { initReactI18next } from 'react-i18next'

import App from './App'
import './index.css'
import { en, fr } from './locale/index'
import reportWebVitals from './reportWebVitals'

void i18n
  .use(initReactI18next) // passes i18n down to react-i18next
  .init({
    resources: {
      en: en,
      fr: fr,
    },
    lng: 'en',
    fallbackLng: 'en',

    interpolation: {
      escapeValue: false,
    },
  })

ReactDOM.render(
  <StrictMode>
    <App />
  </StrictMode>,
  document.getElementById('root')
)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals()
