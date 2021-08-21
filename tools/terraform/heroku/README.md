# Terraform

## Requirements

* Terraform CLI
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

## Configure Heroku CLI

```shell
heroku whoami
```

Login.

```shell
heroku login
```

Create an OAuth API key.

```shell
heroku authorizations:create --description terraform-dhost
```

Set the key and email has environment variables for Terraform.

```shell
export HEROKU_API_KEY=<TOKEN> HEROKU_EMAIL=<EMAIL>
```

## Create the infrastructure

Initialize the configuration.

```shell
terraform init
```

Apply the configuration to Heroku.

```shell
terraform apply
```

The instance should be running, you can check it on your heroku dashboard.

## Inspect state

You can inspect the state.

```shell
terraform show
```

List states.

```shell
terraform state list
```

## Destroy

You can stop all instances using the destroy command.

```shell
terraform destroy
```

## Output

Outputs are used to query informations about the infrastructure.

```shell
$ terraform output

dhost-api_url = "https://dhost-api.herokuapp.com"
```

You can also specify keywords defined in the outputs file to query specific informations.

```shell
$ terraform output dhost-api_url

"42.42.42.42"
```

## Other terraform command

### format

Terraform has a built-in tool to check format.

```shell
terraform fmt
```

### Validate

```shell
terraform validate
```
