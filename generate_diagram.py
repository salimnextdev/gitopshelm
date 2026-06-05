#!/usr/bin/env python3
"""
VProfile GitOps Architecture Diagram Generator
Generates a PDF visualization of the three-tier repository architecture
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import matplotlib.lines as mlines

# Set up the figure
fig, ax = plt.subplots(figsize=(16, 12))
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(8, 11.5, 'VProfile GitOps CI/CD Architecture', 
        ha='center', va='center', fontsize=24, fontweight='bold')

# Colors
git_color = '#E8F5E9'
git_border = '#4CAF50'
aws_color = '#FFF3E0'
aws_border = '#FF9800'
app_color = '#BBDEFB'
helm_color = '#C8E6C9'
infra_color = '#FFE0B2'
service_color = '#FFCCBC'
argocd_color = '#E1F5FE'

# Git Repositories Box
git_box = FancyBboxPatch((0.5, 1), 5, 9, 
                         boxstyle="round,pad=0.1", 
                         edgecolor=git_border, 
                         facecolor=git_color, 
                         linewidth=3)
ax.add_patch(git_box)
ax.text(3, 10.2, 'Git Repositories', fontsize=14, fontweight='bold', 
        ha='center', va='top')

# AWS Cloud Services Box
aws_box = FancyBboxPatch((6.5, 1), 9, 9, 
                         boxstyle="round,pad=0.1", 
                         edgecolor=aws_border, 
                         facecolor=aws_color, 
                         linewidth=3)
ax.add_patch(aws_box)
ax.text(11, 10.2, 'AWS Cloud Services', fontsize=14, fontweight='bold', 
        ha='center', va='top')

# Repository 1: vprofile-app
app_box = FancyBboxPatch((0.8, 8), 4.4, 1.5, 
                         boxstyle="round,pad=0.05", 
                         edgecolor='#1976D2', 
                         facecolor=app_color, 
                         linewidth=2)
ax.add_patch(app_box)
ax.text(3, 9.4, '📦 vprofile-app', fontsize=12, fontweight='bold', ha='center')
ax.text(3, 9.0, '(Source Code)', fontsize=9, ha='center')
ax.text(3, 8.7, '• Java Application', fontsize=8, ha='center')
ax.text(3, 8.4, '• Dockerfile', fontsize=8, ha='center')
ax.text(3, 8.1, '• sonar-project.properties', fontsize=8, ha='center')

# GitHub Actions for App
action_box1 = FancyBboxPatch((0.8, 7.4), 4.4, 0.4, 
                             boxstyle="round,pad=0.02", 
                             edgecolor='#7B1FA2', 
                             facecolor='#F3E5F5', 
                             linewidth=1.5)
ax.add_patch(action_box1)
ax.text(3, 7.6, '⚙️ GitHub Actions CI/CD Pipeline', fontsize=9, 
        ha='center', va='center', fontweight='bold')

# Repository 2: vprofile-helm
helm_box = FancyBboxPatch((0.8, 5), 4.4, 1.8, 
                          boxstyle="round,pad=0.05", 
                          edgecolor='#388E3C', 
                          facecolor=helm_color, 
                          linewidth=2)
ax.add_patch(helm_box)
ax.text(3, 6.6, '⎈ vprofile-helm', fontsize=12, fontweight='bold', ha='center')
ax.text(3, 6.25, '(Helm Charts + ArgoCD)', fontsize=9, ha='center')
ax.text(3, 5.95, '• helm/vprofile/', fontsize=8, ha='center')
ax.text(3, 5.65, '• argocd/apps/, argocd/projects/', fontsize=8, ha='center')
ax.text(3, 5.35, '• kubedefs/', fontsize=8, ha='center')
ax.text(3, 5.05, '📝 Updated via PR Approval', fontsize=8, ha='center', 
        style='italic', color='#D84315')

# Repository 3: vprofile-infra
infra_box = FancyBboxPatch((0.8, 2.2), 4.4, 2, 
                           boxstyle="round,pad=0.05", 
                           edgecolor='#E65100', 
                           facecolor=infra_color, 
                           linewidth=2)
ax.add_patch(infra_box)
ax.text(3, 4.0, '🏗️ vprofile-infra', fontsize=12, fontweight='bold', ha='center')
ax.text(3, 3.65, '(Terraform IaC)', fontsize=9, ha='center')
ax.text(3, 3.35, '• Validate • Plan • Apply', fontsize=8, ha='center')
ax.text(3, 3.05, '• Drift Detection', fontsize=8, ha='center')
ax.text(3, 2.75, '• Notify Slack', fontsize=8, ha='center')
ax.text(3, 2.45, '• Destroy (Manual Trigger)', fontsize=8, ha='center')

# GitHub Actions for Infra
action_box2 = FancyBboxPatch((0.8, 1.6), 4.4, 0.4, 
                             boxstyle="round,pad=0.02", 
                             edgecolor='#7B1FA2', 
                             facecolor='#F3E5F5', 
                             linewidth=1.5)
ax.add_patch(action_box2)
ax.text(3, 1.8, '⚙️ GitHub Actions Terraform Pipeline', fontsize=9, 
        ha='center', va='center', fontweight='bold')

# EC2 SonarQube
ec2_box = FancyBboxPatch((7, 8.5), 2.5, 1.2, 
                         boxstyle="round,pad=0.05", 
                         edgecolor='#E64A19', 
                         facecolor=service_color, 
                         linewidth=2)
ax.add_patch(ec2_box)
ax.text(8.25, 9.4, '🖥️ EC2 Instance', fontsize=11, fontweight='bold', ha='center')
ax.text(8.25, 9.0, 'SonarQube Server', fontsize=9, ha='center')
ax.text(8.25, 8.7, 'with Quality Gates', fontsize=8, ha='center', style='italic')

# Docker Build (icon/label)
ax.text(10.5, 9.1, '🐳', fontsize=30, ha='center', va='center')
ax.text(10.5, 8.6, 'Docker Build', fontsize=9, ha='center', fontweight='bold')

# AWS ECR
ecr_box = FancyBboxPatch((7, 6.8), 2.5, 1.2, 
                         boxstyle="round,pad=0.05", 
                         edgecolor='#E64A19', 
                         facecolor=service_color, 
                         linewidth=2)
ax.add_patch(ecr_box)
ax.text(8.25, 7.7, '📦 AWS ECR', fontsize=11, fontweight='bold', ha='center')
ax.text(8.25, 7.3, 'Docker Registry', fontsize=9, ha='center')
ax.text(8.25, 6.95, '(Container Images)', fontsize=8, ha='center')

# ArgoCD
argocd_box = FancyBboxPatch((7, 4.5), 2.5, 1.2, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#0277BD', 
                            facecolor=argocd_color, 
                            linewidth=2.5)
ax.add_patch(argocd_box)
ax.text(8.25, 5.4, '🔄 ArgoCD', fontsize=11, fontweight='bold', ha='center')
ax.text(8.25, 5.0, 'GitOps Controller', fontsize=9, ha='center')
ax.text(8.25, 4.7, 'Sync & Deploy', fontsize=8, ha='center', style='italic')

# AWS EKS
eks_box = FancyBboxPatch((10.5, 3.5), 3.5, 2.5, 
                         boxstyle="round,pad=0.05", 
                         edgecolor='#E64A19', 
                         facecolor=service_color, 
                         linewidth=3)
ax.add_patch(eks_box)
ax.text(12.25, 5.6, '☸️ AWS EKS Cluster', fontsize=12, fontweight='bold', ha='center')
ax.text(12.25, 5.2, '(Kubernetes)', fontsize=10, ha='center')
ax.text(12.25, 4.8, 'Watches vprofile-helm', fontsize=9, ha='center', 
        style='italic', color='#1B5E20')
ax.text(12.25, 4.3, 'Managed by Terraform', fontsize=8, ha='center')
ax.text(12.25, 3.9, 'Integrated with ArgoCD', fontsize=8, ha='center')

# Slack Notification
ax.text(13, 2, '💬', fontsize=30, ha='center', va='center')
ax.text(13, 1.5, 'Slack', fontsize=9, ha='center', fontweight='bold')
ax.text(13, 1.2, 'Notifications', fontsize=8, ha='center')

# Terraform Icon
ax.text(10, 2, '🔧', fontsize=30, ha='center', va='center')
ax.text(10, 1.5, 'Terraform', fontsize=9, ha='center', fontweight='bold')

# Arrows and Flow

# 1. App to SonarQube
arrow1 = FancyArrowPatch((5.3, 8.75), (7, 9.1),
                         arrowstyle='->', mutation_scale=20, 
                         linewidth=2, color='#1976D2')
ax.add_patch(arrow1)
ax.text(6.15, 9.2, '1. Code Analysis', fontsize=8, 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#1976D2'),
        fontweight='bold')

# 2. App to Docker Build
arrow2 = FancyArrowPatch((5.3, 7.6), (10, 8.6),
                         arrowstyle='->', mutation_scale=20, 
                         linewidth=2, color='#1976D2')
ax.add_patch(arrow2)
ax.text(7.5, 8.3, '2. Build Image', fontsize=8, 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#1976D2'),
        fontweight='bold')

# 3. Docker to ECR
arrow3 = FancyArrowPatch((10.5, 8.3), (8.25, 8.0),
                         arrowstyle='->', mutation_scale=20, 
                         linewidth=2, color='#1976D2')
ax.add_patch(arrow3)
ax.text(9.6, 8.5, '3. Push', fontsize=8, 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#1976D2'),
        fontweight='bold')

# 4. App to Helm (update tag)
arrow4 = FancyArrowPatch((3, 7.4), (3, 6.8),
                         arrowstyle='->', mutation_scale=20, 
                         linewidth=2, color='#388E3C', linestyle='dashed')
ax.add_patch(arrow4)
ax.text(3.8, 7.1, '4. Update Tag (PR)', fontsize=8, 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#388E3C'),
        fontweight='bold')

# 5. Helm to ArgoCD
arrow5 = FancyArrowPatch((5.3, 5.9), (7, 5.1),
                         arrowstyle='->', mutation_scale=20, 
                         linewidth=2, color='#0277BD')
ax.add_patch(arrow5)
ax.text(6, 5.8, '5. Sync', fontsize=8, 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#0277BD'),
        fontweight='bold')

# 6. ArgoCD to EKS
arrow6 = FancyArrowPatch((9.5, 5.1), (10.5, 4.5),
                         arrowstyle='->', mutation_scale=25, 
                         linewidth=3, color='#0277BD')
ax.add_patch(arrow6)
ax.text(10, 5.3, '6. Deploy', fontsize=9, 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#0277BD'),
        fontweight='bold')

# 7. EKS pulls from ECR
arrow7 = FancyArrowPatch((12.25, 6), (8.25, 7.5),
                         arrowstyle='->', mutation_scale=20, 
                         linewidth=2, color='#E65100', linestyle='dashed')
ax.add_patch(arrow7)
ax.text(10.5, 7.2, 'Pull Images', fontsize=8, 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#E65100'),
        fontweight='bold')

# 8. Infra to EKS
arrow8 = FancyArrowPatch((5.3, 3), (10.5, 3.5),
                         arrowstyle='->', mutation_scale=25, 
                         linewidth=3, color='#E65100')
ax.add_patch(arrow8)
ax.text(7.5, 3.5, '7. Provision/Destroy', fontsize=9, 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#E65100'),
        fontweight='bold')

# 9. Infra to Slack
arrow9 = FancyArrowPatch((5.3, 1.8), (12.5, 1.8),
                         arrowstyle='->', mutation_scale=20, 
                         linewidth=2, color='#7B1FA2', linestyle='dashed')
ax.add_patch(arrow9)
ax.text(8.5, 2.1, 'Notify', fontsize=8, 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#7B1FA2'),
        fontweight='bold')

# 10. EKS watches Helm
arrow10 = FancyArrowPatch((12.25, 3.5), (5.3, 5.9),
                          arrowstyle='<-', mutation_scale=20, 
                          linewidth=2, color='#4CAF50', linestyle='dotted')
ax.add_patch(arrow10)
ax.text(9, 4.5, 'Watch for Changes', fontsize=8, 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#4CAF50'),
        fontweight='bold')

# Legend
legend_box = FancyBboxPatch((0.5, 0.1), 5, 0.8, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#616161', 
                            facecolor='#FAFAFA', 
                            linewidth=2)
ax.add_patch(legend_box)
ax.text(3, 0.8, 'Legend', fontsize=11, fontweight='bold', ha='center')

# Legend items
solid_line = mlines.Line2D([1, 1.5], [0.5, 0.5], color='#1976D2', linewidth=2)
ax.add_line(solid_line)
ax.text(1.7, 0.5, 'CI/CD Flow', fontsize=8, va='center')

dashed_line = mlines.Line2D([3, 3.5], [0.5, 0.5], color='#4CAF50', 
                             linewidth=2, linestyle='dashed')
ax.add_line(dashed_line)
ax.text(3.7, 0.5, 'Update/Sync', fontsize=8, va='center')

dotted_line = mlines.Line2D([5, 5.5], [0.3, 0.3], color='#4CAF50', 
                            linewidth=2, linestyle='dotted')
ax.add_line(dotted_line)
ax.text(1, 0.25, '← Watch/Monitor', fontsize=8, va='center')

ax.text(3.5, 0.25, '🔒 Quality Gates Enforced', fontsize=8, va='center')

# Save as PDF
plt.tight_layout()
plt.savefig('/Users/mac/Desktop/personalprojects/gitopshelm/vprofile-gitops-architecture.pdf', 
            format='pdf', dpi=300, bbox_inches='tight')
print("✅ PDF diagram generated: vprofile-gitops-architecture.pdf")
plt.close()

print("✅ Architecture diagram created successfully!")
print("\nFiles created:")
print("  1. vprofile-gitops-architecture.drawio (for Draw.io website)")
print("  2. vprofile-gitops-architecture.pdf (visual diagram)")
print("  3. ARCHITECTURE.md (detailed documentation)")
