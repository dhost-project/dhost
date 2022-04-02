import { env } from "environment"
import { OAuthApplication } from "models/api/OAuthApplication"
import { http, HttpResponse } from "utils/http"

/**
 *
 */
export function logout(): HttpResponse<any> {
    return http.get(`${env.API_URL}/api/logout/`)
}