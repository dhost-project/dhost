import { env } from "environment"
import { BuildOptions } from "models/api/BuildOptions"
import { http, HttpResponse } from "utils/http"

/**
 *
 * @param dapp_slug string
 */
export function listBuildOptions(dapp_slug: string): HttpResponse<BuildOptions[]> {
  return http.get(`${env.API_URL}/api/ipfs/${dapp_slug}/buildoptions/`)
}

/**
 *
 * @param dapp_slug string
 * @param buildOptions BuildOptions
 */
export function createBuildOptions(
  dapp_slug: string,
  buildOptions: BuildOptions
): HttpResponse<BuildOptions> {
  return http.post(
    `${env.API_URL}/api/ipfs/${dapp_slug}/buildoptions/`,
    buildOptions
  )
}

/**
 *
 * @param dapp_slug A unique value identifying this build options
 */
export function retrieveBuildOptions(dapp_slug: string): HttpResponse<BuildOptions> {
  return http.get(`${env.API_URL}/api/ipfs/${dapp_slug}/buildoptions/${dapp_slug}/`)
}

/**
 *
 * @param dapp_slug A unique value identifying this build options
 * @param buildOptions BuildOptions
 */
export function updateBuildOptions(
  dapp_slug: string,
  buildOptions: BuildOptions
): HttpResponse<BuildOptions> {
  return http.put(
    `${env.API_URL}/api/ipfs/${dapp_slug}/buildoptions/${dapp_slug}/`,
    buildOptions
  )
}

/**
 *
 * @param dapp_slug A unique value identifying this build options
 * @param buildOptions BuildOptions
 */
export function partialUpdateBuildOptions(
  dapp_slug: string,
  buildOptions: BuildOptions
): HttpResponse<BuildOptions> {
  return http.patch(
    `${env.API_URL}/api/ipfs/${dapp_slug}/buildoptions/${dapp_slug}/`,
    buildOptions
  )
}

/**
 *
 * @param dapp_slug A unique value identifying this build options
 */
export function destroyBuildOptions(dapp_slug: string): HttpResponse<void> {
  return http.delete(`${env.API_URL}/api/ipfs/${dapp_slug}/buildoptions/${dapp_slug}/`)
}

/**
 *
 * @param dapp_slug A unique value identifying this build options
 */
export function buildBuildOptions(dapp_slug: string):HttpResponse<BuildOptions> {
  return http.get(`${env.API_URL}/api/ipfs/${dapp_slug}/buildoptions/${dapp_slug}/build/`)
}