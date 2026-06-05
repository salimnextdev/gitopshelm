# vprofile-infra

Terraform infrastructure for the VProfile EKS environment and Argo CD ingress.

## What this repo creates

- AWS VPC
- Public subnets
- Internet gateway and route table
- EKS cluster
- EKS managed node group
- IAM roles and policies
- EBS CSI driver add-on
- Argo CD ingress manifest

## Files

- `main.tf` - core AWS and EKS infrastructure
- `backend.tf` - Terraform remote state backend
- `variables.tf` - configurable inputs
- `outputs.tf` - useful Terraform outputs
- `argocd-ingress.yaml` - Kubernetes ingress for Argo CD

## Argo CD access

After the ingress is deployed, Argo CD is reachable through the ALB DNS name shown in the ingress status, for example:

```bash
kubectl describe ingress argocd-ingress -n argocd
```

### Argo CD login

- Username: `admin`
- Password: get it from the cluster secret:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d; echo
```

### Argo CD CLI

If you are using the Argo CD CLI through the ingress, use `--grpc-web`:

```bash
argocd login argocd.salimnextdev.site --username admin --grpc-web
argocd repo add git@github.com:salimnextdev/vprofile-helm.git --ssh-private-key-path ~/.ssh/salimnextdev --grpc-web
```

## DNS setup

For `argocd.salimnextdev.site`, create a `CNAME` record in your DNS provider that points to the ALB endpoint from the ingress.

Example:

- Host: `argocd`
- Value: `k8s-argocd-argocdin-d3e7e0dbcd-267213850.us-east-1.elb.amazonaws.com`

## Terraform notes

This repo uses Terraform state and provider files locally, so `.terraform/` and other generated Terraform artifacts are ignored via `.gitignore`.

## Apply

```bash
terraform init
terraform plan
terraform apply
```
