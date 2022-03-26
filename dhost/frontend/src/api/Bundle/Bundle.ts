import { env } from "environment"
import { Dapp } from "models/api/Dapp"
import { http, HttpResponse } from "utils/http"

/**
 *
 * @param dapp_slug string
 */
export function listBundles(dapp_slug: string): HttpResponse<Dapp[]> {
  return http.get(`${env.API_URL}/api/ipfs/${dapp_slug}/bundles/`)
}

/**
 *
 * @param dapp_slug string
 * @param media string or null <binary>
 */
export function createBundle(
  dapp_slug: string,
  media?: string
): HttpResponse<Dapp[]> {
  return http.post(`${env.API_URL}/api/ipfs/${dapp_slug}/bundles/`, {
    media: media ?? null,
  })
}

/**
 *
 * @param dapp_slug string
 * @param id A UUID string identifying this bundle.
 */
export function retrieveBundle(
  dapp_slug: string,
  id: string
): HttpResponse<Dapp[]> {
  return http.get(`${env.API_URL}/api/ipfs/${dapp_slug}/bundles/${id}/`)
}
