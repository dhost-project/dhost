export interface OAuthApplication {
    id: number
    user: string
    name: string
    description: string
    logo: string
    client_id: string
    client_secret: string
    client_type: "confidential"
    authorization_grant_type: "authorization-code"
    skip_authorization: boolean
    created: string
    updated: string
}