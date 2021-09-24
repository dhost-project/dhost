import { env } from "environment"
import { IPFSDapp, IPFSDappParams } from "models/api/IPFSDapp"
import { http, HttpResponse } from "utils/http"

/**
 * Get list of IPFS Dapps
 */
export function listIPFSDapps(): HttpResponse<IPFSDapp[]> {
  return http.get(`${env.API_URL}/api/ipfs/`)
}

/**
 * Create IPFS Dapp
 */
export function createIPFSDapp(
  dappParams: IPFSDappParams
): HttpResponse<IPFSDappParams> {
  return http.post(`${env.API_URL}/api/ipfs/`, dappParams)
}

/**
 *
 * @param slug A unique value identifying this IPFS Dapp
 */
export function retrieveIPFSDapp(slug: string): HttpResponse<IPFSDapp> {
  return http.get(`${env.API_URL}/api/ipfs/${slug}/`)
}

/**
 *
 * @param slug A unique value identifying this IPFS Dapp
 * @param dappParams IPFSDappParams
 */
export function updateIPFSDapp(
  slug: string,
  dappParams: IPFSDappParams
): HttpResponse<IPFSDappParams> {
  return http.put(`${env.API_URL}/api/ipfs/${slug}/`, dappParams)
}

/**
 *
 * @param slug A unique value identifying this IPFS Dapp
 * @param dappParams IPFSDappParams
 */
export function partialUpdateIPFSDapp(
  slug: string,
  dappParams: IPFSDappParams
): HttpResponse<IPFSDappParams> {
  return http.patch(`${env.API_URL}/api/ipfs/${slug}/`, dappParams)
}

/**
 * Delete IPFS Dapp
 * @param slug A unique value identifying this IPFS Dapp
 */
export function destroyIPFSDapp(slug: string): HttpResponse<void> {
  return http.delete(`${env.API_URL}/api/ipfs/${slug}/`)
}

/**
 * Deploy IPFS Dapp
 * @param slug A unique value identifying this IPFS Dapp
 */
export function deployIPFSDapp(slug: string): HttpResponse<IPFSDapp> {
  return http.get(`${env.API_URL}/api/ipfs/${slug}/deploy/`)
}
