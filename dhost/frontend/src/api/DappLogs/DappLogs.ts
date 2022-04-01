import { env } from "environment"
import { DappLogs } from "models/api/DappLogs"
import { IPFSDapp, IPFSDappParams } from "models/api/IPFSDapp"
import { http, HttpResponse } from "utils/http"

/**
 * Get list of IPFS Dapps
 * @param slug A unique value identifying this IPFS Dapp
 */
export function listDappsLogs(slug: string): HttpResponse<DappLogs[]> {
    return http.get(`${env.API_URL}/api/ipfs/${slug}/logs/`)
}

/**
 *
 * @param slug A unique value identifying this IPFS Dapp
 * @param id
 */
export function retrieveIPFSDapp(slug: string, id: string): HttpResponse<DappLogs> {
    return http.get(`${env.API_URL}/api/ipfs/${slug}/logs/${id}/`)
}
