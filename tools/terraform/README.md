# Terraform

## Requirements

* Terraform CLI

## AWS

### Requirements

* Terraform CLI
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

### Configure AWS CLI

Create access key [here](https://console.aws.amazon.com/iam/home?#/security_credentials).

Configure the AWS CLI.

```
aws configure
```

### Create the infrastructure

Initialize the configuration.

```
terraform init
```

Apply the configuration to AWS.

```shell
terraform apply
```

The instance should be running, you can check it on your AWS console.

Note that you may need to change the region in the top right.

### Inspect state

You can inspect the state.

```shell
terraform show
```

List states.

```shell
terraform state list
```

### Destroy

You can stop all instances using the destroy command.

```shell
terraform destroy
```

### Output

Outputs are defined in `outputs.tf` and are used to query informations about the infrastructure.

```shell
$ terraform output

instance_id = "i-42424242424242"
instance_public_ip = "42.42.42.42"
```

You can also specify keywords defined in the outputs file to query specific informations.

```shell
$ terraform output instance_public_ip

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
