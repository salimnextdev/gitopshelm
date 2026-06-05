# VProfile GitOps Architecture Diagrams

## 📁 Files Created

### 1. **vprofile-gitops-architecture.drawio**
   - **Format**: Draw.io XML file
   - **Usage**: Upload to [app.diagrams.net](https://app.diagrams.net) or [draw.io](https://draw.io)
   - **Features**: 
     - Fully editable diagram
     - AWS service icons (EC2, ECR, EKS)
     - Tech stack logos (GitHub, Docker, ArgoCD, Helm, Terraform, Slack)
     - Color-coded sections for Git repos and AWS services
     - Numbered workflow arrows showing CI/CD flow
     - Legend explaining different arrow types

### 2. **vprofile-gitops-architecture.pdf** 
   - **Format**: PDF visual diagram (generated via Python script)
   - **Usage**: View directly or print
   - **Features**: High-resolution diagram with all components

### 3. **ARCHITECTURE.md**
   - **Format**: Markdown documentation
   - **Usage**: Technical reference and architecture guide
   - **Contains**: Detailed explanations of each component and workflow

### 4. **generate_diagram.py**
   - **Format**: Python script
   - **Usage**: Regenerate PDF diagram with customizations
   - **Requires**: `matplotlib` library

---

## 🚀 How to Use

### Option 1: Edit in Draw.io (Recommended)
1. Go to [app.diagrams.net](https://app.diagrams.net)
2. Click **File → Open from → Device**
3. Select `vprofile-gitops-architecture.drawio`
4. Edit as needed
5. Export as PNG, PDF, SVG, or save as .drawio

### Option 2: View PDF
- Open `vprofile-gitops-architecture.pdf` directly in any PDF viewer

### Option 3: Regenerate PDF with Python
```bash
# Install matplotlib (if not already installed)
pip3 install matplotlib --break-system-packages

# Run the script
python3 generate_diagram.py
```

---

## 🎨 Architecture Components

### Git Repositories (Green Box)
- **vprofile-app**: Java application source code
- **vprofile-helm**: Helm charts and ArgoCD configurations
- **vprofile-infra**: Terraform infrastructure code

### AWS Cloud Services (Orange Box)
- **EC2 Instance**: SonarQube server with quality gates
- **AWS ECR**: Docker container registry
- **AWS EKS**: Kubernetes cluster managed by Terraform

### Integration Tools
- **GitHub Actions**: CI/CD pipelines for app and infrastructure
- **Docker**: Container image building
- **ArgoCD**: GitOps continuous delivery
- **Helm**: Kubernetes package manager
- **Terraform**: Infrastructure as Code
- **Slack**: Notifications and alerts

---

## 🔄 Workflow Summary

1. **Code Analysis**: Push to vprofile-app → SonarQube analysis on EC2
2. **Build Image**: GitHub Actions builds Docker image
3. **Push to Registry**: Docker image pushed to AWS ECR
4. **Update Helm**: Image tag updated in vprofile-helm via PR
5. **Sync**: ArgoCD detects changes in helm repo
6. **Deploy**: ArgoCD deploys to EKS cluster
7. **Pull Images**: EKS pulls container images from ECR
8. **Infrastructure**: Terraform manages EKS cluster lifecycle
9. **Watch**: EKS continuously watches helm repo for updates

---

## 📊 AWS Service Icons

The diagram uses official AWS service icons:

- **EC2**: ![EC2](https://img.shields.io/badge/AWS-EC2-FF9900?style=flat&logo=amazonec2&logoColor=white)
- **ECR**: ![ECR](https://img.shields.io/badge/AWS-ECR-FF9900?style=flat&logo=amazon&logoColor=white)
- **EKS**: ![EKS](https://img.shields.io/badge/AWS-EKS-FF9900?style=flat&logo=amazoneks&logoColor=white)

---

## 🎯 Key Features

✅ **Three-Tier Repository Architecture**
- Separation of concerns (app, config, infra)
- Independent versioning and lifecycle management

✅ **GitOps Workflow**
- Git as single source of truth
- Automated sync via ArgoCD
- Pull request approval for changes

✅ **Infrastructure as Code**
- Terraform for EKS cluster management
- Drift detection and auto-remediation
- Separate destroy workflow for safety

✅ **Quality Assurance**
- SonarQube quality gates
- Automated code analysis
- Container security scanning

✅ **Observability**
- Slack notifications for pipeline status
- Infrastructure drift alerts
- Deployment status tracking

---

## 📝 Customization

### To modify the Draw.io diagram:
1. Open in Draw.io
2. Edit text, arrows, or components
3. Add/remove services as needed
4. Change colors using the format panel
5. Export in your desired format

### To regenerate PDF:
1. Edit `generate_diagram.py`
2. Modify coordinates, colors, or text
3. Run the script to generate updated PDF

---

## 📚 Additional Resources

- [Draw.io Documentation](https://www.diagrams.net/doc/)
- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [Helm Documentation](https://helm.sh/docs/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

---

**Version**: 1.0  
**Created**: 2024  
**Architecture**: Three-Tier GitOps CI/CD Pipeline
