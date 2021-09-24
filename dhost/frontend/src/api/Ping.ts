import { env } from "environment"
import { ApiPing } from "models/api/ApiPing"
import { http, HttpResponse } from "utils/http"

/**
 * Get API version
 */
export function listAPIPings(): HttpResponse<ApiPing> {
  return http.get(`${env.API_URL}/api/ping/`)
}
