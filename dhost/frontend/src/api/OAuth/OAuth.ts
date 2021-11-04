import { env } from "environment"
import { OAuthApplication } from "models/api/OAuthApplication"
import { http, HttpResponse } from "utils/http"

/**
 *
 */
export function listOAuth2Applications(): HttpResponse<OAuthApplication[]> {
  return http.get(`${env.API_URL}/api/oauth2/applications/`)
}

/**
 *
 * @param id A unique integer value identifying this o auth2 application
 */
export function retrieveOAuth2Application(
  id: string
): HttpResponse<OAuthApplication> {
  return http.get(`${env.API_URL}/api/oauth2/applications/${id}/`)
}
