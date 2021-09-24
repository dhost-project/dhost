import { env } from "environment"
import { User } from "models/api/User"
import { http, HttpResponse } from "utils/http"

export function meUser(): HttpResponse<User> {
  return http.get(`${env.API_URL}/api/users/me/`)
}
