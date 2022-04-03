import { env } from "environment"
import { User } from "models/api/User"
import { UserSettings } from "models/UserSettings"
import { http, HttpResponse } from "utils/http"

export function meUser(): HttpResponse<User> {
  return http.get(`${env.API_URL}/api/users/me/`)
}

/**
 *
 * @param userSettingsParams IPFSDappParams
 */
export function updateUserSettings(userSettingsParams: UserSettings): HttpResponse<UserSettings> {
  return http.post(`${env.API_URL}/api/settings/`, userSettingsParams)
}

export function getUserSettings(): HttpResponse<string> {
  return http.get(`${env.API_URL}/api/settings/`)
}
