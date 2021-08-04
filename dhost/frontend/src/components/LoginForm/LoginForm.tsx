import axios from 'axios';
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

  async login() {
    const loginUrl = `/api/login/`
    const username = encodeURIComponent(this.state.username)
    const password = encodeURIComponent(this.state.password)
    const next = encodeURIComponent("/")

    const data = `username=${username}&password=${password}&next=${next}`
    const headers = { "Content-Type": "application/x-www-form-urlencoded" }

    const http = axios.create({
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken',
    })

    await http.get(loginUrl, { headers })
    const response = await http.post(loginUrl, data, { headers })

    return response
  }

  handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    this.login()
    event.preventDefault()
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Username:
          <input
            type="text"
            name="username"
            value={this.state.username}
            onChange={this.handleUsernameChange}
          />
        </label>
        <label>
          Password:
          <input
            type="password"
            name="password"
            value={this.state.password}
            onChange={this.handlePasswordChange}
          />
        </label>
        <input className="p-1 bg-gray-100" type="submit" value="Submit" />
      </form>
    )
  }
}
