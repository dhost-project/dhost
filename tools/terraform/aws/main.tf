terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  region                  = "us-west-2"
  shared_credentials_file = "aws_credentials.key"
  profile                 = "default"
}

resource "aws_instance" "api" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = var.api_instance_name
  }
}
