export interface Repository {
  id: number
  github_owner: string
  github_repo: string
  branches: [
    {
      name: string
    }
  ]
  added_at: string
  updated_at: string
}
