import axios, { AxiosResponse } from "axios"

export interface HttpResponse<T> extends Promise<AxiosResponse<T>> {}

const http = axios.create({
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken",
})

// response interceptor
http.interceptors.request.use(
  function (config) {
    return config
  },
  function (error) {
    return Promise.reject(error)
  }
)

// response interceptor
http.interceptors.response.use(
  function (response) {
    // For every status code == 2xx

    return response
  },
  function (error) {
    // For every status code != 4xx
    console.log("window.location", window.location)
    console.log("HTTP ERROR", error.response.status)
    if (
      error.response.status === 401 &&
      window.location.pathname !== "/login"
    ) {
      window.location.href = "/login"
    }
    return Promise.reject(error)
  }
)

export { http }
