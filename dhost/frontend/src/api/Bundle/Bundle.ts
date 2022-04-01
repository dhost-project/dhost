import { env } from "environment"
import { Bundle } from "models/api/Bundle"
import { http, HttpResponse } from "utils/http"

/**
 *
 * @param dapp_slug string
 */
export function listBundles(dapp_slug: string): HttpResponse<Bundle[]> {
  return http.get(`${env.API_URL}/api/ipfs/${dapp_slug}/bundles/`)
}

/**
 *
 * @param dapp_slug string
 * @param media string or null <binary>
 */
export function createBundle(
  dapp_slug: string,
  bundle: File,
  media?: string
): HttpResponse<Bundle[]> {
  const formData = new FormData()
  formData.append('file', bundle)
  formData.append('media', media || 'null')

  return http.post(`${env.API_URL}/api/ipfs/${dapp_slug}/bundles/`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
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
): HttpResponse<Bundle[]> {
  return http.get(`${env.API_URL}/api/ipfs/${dapp_slug}/bundles/${id}/`)
}
