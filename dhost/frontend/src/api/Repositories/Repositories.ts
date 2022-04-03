import { env } from "environment"
import { Repository } from "models/api/Repository"
import { http, HttpResponse } from "utils/http"

/**
 *
 */
export function listRepositorys(): HttpResponse<Repository[]> {
  return http.get(`${env.API_URL}/api/github/repositories/`)
}

/**
 * Update every Github repos for user from the Github API
 */
export function fetchAllRepository(): HttpResponse<Repository[]> {
  return http.get(`${env.API_URL}/api/github/repositories/fetch_all/`)
}

/**
 * Retrieve repository by id (from dabatase)
 * @param id Github repository unique ID
 */
export function retrieveRepository(id: number): HttpResponse<Repository> {
  return http.get(`${env.API_URL}/api/github/repositories/${id}/`)
}

/**
 * Update a single repo from Github API
 * @param id Github repository unique ID
 */
export function fetchRepository(id: number): HttpResponse<Repository> {
  return http.get(`${env.API_URL}/api/github/repositories/${id}/fetch/`)
}

/**
 * Update a single repo branches from the Github API
 * @param id Github repository unique ID
 */
export function fetchBranchesRepository(id: number): HttpResponse<Repository> {
  return http.get(
    `${env.API_URL}/api/github/repositories/${id}/fetch_branches/`
  )
}
