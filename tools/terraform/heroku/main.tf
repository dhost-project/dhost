terraform {
  required_providers {
    heroku = {
      source  = "heroku/heroku"
      version = "~> 4.0"
    }
  }
}

variable "dhost-api" {
  description = "Value of the Name for the DHost API Heroku instance"
  type        = string
  default     = "dhost-api"
}

resource "heroku_app" "dhost-api" {
  name   = var.dhost-api
  region = "us"

  config_vars = {
    DJANGO_ENV    = "production"
    ALLOWED_HOSTS = "dhost-api.herokuapp.com"
  }

  sensitive_config_vars = {
    DJANGO_SECRET_KEY         = "change_me"
    # SENTRY_DSN                = "add_me"
    # SOCIAL_AUTH_GITHUB_KEY    = "add_me"
    # SOCIAL_AUTH_GITHUB_SECRET = "add_me"
  }
}

# Create a postgresql database, and configure the app to use it
resource "heroku_addon" "database" {
  app  = heroku_app.dhost-api.name
  plan = "heroku-postgresql:hobby-dev"
}

# Build code & release to the app
resource "heroku_build" "dhost-api" {
  app        = heroku_app.dhost-api.name
  buildpacks = ["https://github.com/heroku/heroku-buildpack-python.git"]

  source {
    # Local directory, if content change it will force a new build
    path = "../../../../dhost"
  }
}

output "dhost-api_url" {
  value = "https://${heroku_app.dhost-api.name}.herokuapp.com"
}
