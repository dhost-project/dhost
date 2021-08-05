import axios from "axios"
import React from "react"

export default class LoginForm extends React.Component<
  {},
  { username: string; password: string }
> {
  constructor(props: any) {
    super(props)
    this.state = { username: "", password: "" }

    this.handleUsernameChange = this.handleUsernameChange.bind(this)
    this.handlePasswordChange = this.handlePasswordChange.bind(this)
    this.login = this.login.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleUsernameChange(event: React.ChangeEvent<HTMLInputElement>) {
    this.setState({ username: event.target.value })
  }

  handlePasswordChange(event: React.ChangeEvent<HTMLInputElement>) {
    this.setState({ password: event.target.value })
  }

  handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    this.login()
    event.preventDefault()
  }

  async login() {
    const loginUrl = `/api/login/`
    const username = encodeURIComponent(this.state.username)
    const password = encodeURIComponent(this.state.password)
    const next = encodeURIComponent("/")

    const data = `username=${username}&password=${password}&next=${next}`
    const headers = { "Content-Type": "application/x-www-form-urlencoded" }

    const http = axios.create({
      xsrfCookieName: "csrftoken",
      xsrfHeaderName: "X-CSRFToken",
    })

    await http.get(loginUrl, { headers })
    const response = await http.post(loginUrl, data, { headers })

    return response
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <div className="relative">
          <input
            id="username"
            type="text"
            name="username"
            value={this.state.username}
            onChange={this.handleUsernameChange}
            placeholder="Username"
            className="peer h-10 w-full border-b-2 border-gray-300 text-gray-900 placeholder-transparent focus:outline-none focus:border-green-500"
          />
          <label
            htmlFor="username"
            className="absolute left-0 -top-3.5 text-gray-600 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm"
          >
            Username
          </label>
        </div>
        <div className="relative mt-8">
          <input
            id="pasword"
            type="password"
            name="password"
            value={this.state.password}
            onChange={this.handlePasswordChange}
            placeholder="Password"
            className="peer h-10 w-full border-b-2 border-gray-300 text-gray-900 placeholder-transparent focus:outline-none focus:border-green-500"
          />
          <label
            htmlFor="password"
            className="absolute left-0 -top-3.5 text-gray-600 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm"
          >
            Password
          </label>
        </div>
        <input
          className="px-4 py-1 mt-12 rounded bg-green-200 w-full hover:bg-gray-200 cursor-pointer focus:outline-none focus:ring-2 focus:ring-green-500"
          type="submit"
          value="Login"
        />
        <a
          href="/"
          className="mt-4 block text-sm text-center font-medium text-green-700 hover:underline focus:outline-none focus:ring-2 focus:ring-green-500 rounded"
        >
          Forgot your password?
        </a>
      </form>
    )
  }
}
