import { env } from "environment"
import { GithubOptions } from "models/api/GithubOptions"
import { http, HttpResponse } from "utils/http"

/**
 *
 * @param dappSlug string
 */
export function listGithubOptions(
  dappSlug: string
): HttpResponse<GithubOptions[]> {
  return http.get(`${env.API_URL}/api/ipfs/${dappSlug}/githuboptions/`)
}

/**
 *
 * @param dappSlug string
 * @param githubOptions GithubOptions
 */
export function createGithubOptions(
  dappSlug: string,
  githubOptions: GithubOptions
): HttpResponse<GithubOptions> {
  return http.post(
    `${env.API_URL}/api/ipfs/${dappSlug}/githuboptions/`,
    githubOptions
  )
}

/**
 *
 * @param dappSlug string
 */
export function retrieveGithubOptions(
  dappSlug: string
): HttpResponse<GithubOptions> {
  return http.get(
    `${env.API_URL}/api/ipfs/${dappSlug}/githuboptions/${dappSlug}/`
  )
}

/**
 *
 * @param dappSlug string
 * @param githubOptions GithubOptions
 */
export function updateGithubOptions(
  dappSlug: string,
  githubOptions: GithubOptions
): HttpResponse<GithubOptions> {
  return http.put(
    `${env.API_URL}/api/ipfs/${dappSlug}/githuboptions/${dappSlug}/`,
    githubOptions
  )
}

/**
 *
 * @param dappSlug string
 * @param githubOptions GithubOptions
 */
export function partialUpdateGithubOptions(
  dappSlug: string,
  githubOptions: GithubOptions
): HttpResponse<GithubOptions> {
  return http.patch(
    `${env.API_URL}/api/ipfs/${dappSlug}/githuboptions/${dappSlug}/`,
    githubOptions
  )
}

/**
 *
 * @param dappSlug string
 */
export function destroyGithubOptions(dappSlug: string): HttpResponse<void> {
  return http.delete(
    `${env.API_URL}/api/ipfs/${dappSlug}/githuboptions/${dappSlug}/`
  )
}
