import { env } from "environment"
import { ApiRoot } from "models/api/ApiRoot"
import { http, HttpResponse } from "utils/http"

/**
 * Get list of api root paths
 */
export function listAPIRoots(): HttpResponse<ApiRoot> {
  return http.get(`${env.API_URL}/api/`)
}
