import { env } from "environment"
import { EnvVar } from "models/api/EnvVar"
import { http, HttpResponse } from "utils/http"

/**
 * Get users dapp list
 *  
 * @param slug A unique value identifying dapp
 */
export function createEnvVar(slug: string, envVar: EnvVar): HttpResponse<EnvVar> {
    return http.post(`${env.API_URL}/api/ipfs/${slug}/buildoptions/${slug}/envvars/`, envVar)
}

/**
 * Get list of every env vars, regardless of wich type they are
 * @param slug A unique value identifying dapp
 */
export function retrieveEnvVars(slug: string): HttpResponse<EnvVar[]> {
    return http.get(`${env.API_URL}/api/ipfs/${slug}/buildoptions/${slug}/envvars/`)
}
