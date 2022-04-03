import { env } from "environment"
import { Dapp } from "models/api/Dapp"
import { http, HttpResponse } from "utils/http"

/**
 * Get users dapp list
 */
export function listDapps(): HttpResponse<Dapp[]> {
  return http.get(`${env.API_URL}/api/dapps/`)
}

/**
 * Retrieve list of every dapps, regardless of wich type they are
 * @param slug A unique value identifying dapp
 */
export function retrieveDapp(slug: string): HttpResponse<Dapp> {
  return http.get(`${env.API_URL}/api/dapps/${slug}/`)
}
