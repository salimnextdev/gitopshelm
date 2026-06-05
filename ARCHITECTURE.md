# VProfile GitOps CI/CD Architecture

## Overview
This architecture implements a complete GitOps workflow using three separate repositories for source code, Helm charts, and infrastructure as code.

---

## Repository Structure

### 1. **vprofile-app** (Source Code Repository)
- **Technology**: Java application with Docker
- **CI/CD**: GitHub Actions
- **Components**:
  - Application source code (Java/Maven)
  - Dockerfiles for app, db, web components
  - SonarQube configuration (sonar-project.properties)

**Pipeline Stages**:
1. Code checkout
2. SonarQube code analysis on EC2 (Quality Gates)
3. Docker image build
4. Push image to AWS ECR
5. Update image tag in vprofile-helm repository

---

### 2. **vprofile-helm** (Helm Charts & GitOps Repository)
- **Technology**: Helm, ArgoCD, Kubernetes manifests
- **Components**:
  - `helm/vprofile/` - Helm chart for application
  - `argocd/apps/` - ArgoCD application definitions
  - `argocd/projects/` - ArgoCD project configurations
  - `kubedefs/` - Raw Kubernetes manifests (deployments, services, ingress, PVCs, secrets)

**Update Mechanism**:
- Updated via Pull Request approval from vprofile-app
- Triggers ArgoCD sync on merge
- Watched continuously by EKS cluster via ArgoCD

---

### 3. **vprofile-infra** (Infrastructure as Code Repository)
- **Technology**: Terraform, GitHub Actions
- **Components**:
  - EKS cluster configuration
  - VPC, IAM, and networking resources
  - ArgoCD ingress configuration

**Pipeline Stages**:
1. **Validate** - Terraform syntax validation
2. **Plan** - Preview infrastructure changes
3. **Apply** - Deploy/update infrastructure
4. **Drift Detection** - Detect configuration drift
5. **Notify** - Send updates to Slack
6. **Destroy** - Manual trigger to teardown cluster

---

## AWS Cloud Services

### **EC2 Instance**
- Hosts SonarQube Server
- Performs static code analysis
- Enforces quality gates before build

### **Amazon ECR (Elastic Container Registry)**
- Stores Docker container images
- Integrated with CI/CD pipeline
- Pulled by EKS cluster during deployment

### **Amazon EKS (Elastic Kubernetes Service)**
- Managed Kubernetes cluster
- Provisioned by Terraform (vprofile-infra)
- Integrated with ArgoCD for GitOps deployments
- Watches vprofile-helm repository for changes

---

## GitOps Workflow

### CI/CD Flow:
```
vprofile-app (Code Push)
    ↓
SonarQube Analysis (EC2)
    ↓
Docker Build
    ↓
Push to ECR
    ↓
Update Image Tag in vprofile-helm (PR)
    ↓
PR Approval & Merge
    ↓
ArgoCD Detects Change
    ↓
Deploy to EKS Cluster
    ↓
EKS Pulls Image from ECR
```

### Infrastructure Flow:
```
vprofile-infra (Terraform Code)
    ↓
GitHub Actions (Validate → Plan → Apply)
    ↓
Create/Update EKS Cluster
    ↓
Notify Slack
    ↓
(Manual) Destroy Stage (separate workflow)
```

---

## Key Integration Points

1. **vprofile-app ↔ vprofile-helm**
   - Connection: Image tag updates via automated PR
   - Trigger: Successful ECR push

2. **vprofile-helm ↔ EKS**
   - Connection: ArgoCD watches helm repository
   - Trigger: Git commit to main branch

3. **vprofile-infra → EKS**
   - Connection: Terraform provisions cluster
   - Trigger: Manual pipeline execution

4. **EKS → ECR**
   - Connection: Image pull during pod creation
   - Trigger: Kubernetes deployment

---

## Tools & Technologies

| Component | Technology |
|-----------|-----------|
| Source Control | GitHub |
| CI/CD | GitHub Actions |
| Code Quality | SonarQube (EC2) |
| Container Registry | AWS ECR |
| Container Orchestration | AWS EKS (Kubernetes) |
| GitOps | ArgoCD |
| Package Manager | Helm |
| Infrastructure as Code | Terraform |
| Notifications | Slack |

---

## Security & Best Practices

- **Quality Gates**: SonarQube enforces code quality before build
- **Pull Request Workflow**: Helm chart changes require approval
- **Drift Detection**: Continuous monitoring of infrastructure state
- **Separate Destroy Stage**: Prevents accidental cluster deletion
- **GitOps**: All changes tracked in Git with audit trail
- **Immutable Infrastructure**: Container-based deployments

---

## Deployment Stages

### Stage 1: Infrastructure Setup
1. Run vprofile-infra Terraform pipeline
2. EKS cluster provisioned
3. ArgoCD installed on cluster

### Stage 2: Application Deployment
1. Push code to vprofile-app
2. CI pipeline builds and pushes image
3. Helm chart updated automatically
4. ArgoCD syncs changes to EKS

### Stage 3: Continuous Delivery
1. All subsequent changes follow GitOps workflow
2. Helm repository is source of truth
3. EKS cluster stays in sync automatically

---

## Notifications
- Terraform pipeline status → Slack
- Drift detection alerts → Slack
- Infrastructure changes → Slack

---

**Created**: 2024
**Architecture Type**: Three-Tier GitOps Repository Structure
