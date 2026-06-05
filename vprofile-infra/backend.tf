terraform {
  backend "s3" {
    bucket = "gitops-terraformcode6202"
    key    = "terraform.tfstate"
    region = "us-east-1"
  }
}
