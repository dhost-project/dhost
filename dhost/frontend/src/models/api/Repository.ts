export interface Repository {
  id: number
  github_owner: string
  github_repo: string
  branches: [
    {
      id: number
      name: string
    }
  ]
  added_at: string
  updated_at: string
}
