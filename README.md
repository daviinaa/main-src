##first take of the assessment using argocd & helm to deploy 

This project builds a web application that that prints the origin public IP of any request it receives in reverse.

##specify where db would be stored

Builds a docker image of the app and an helm chart.
CI\CD pipeline using github actions that builds the docker image, push to a docker registry and then Argocd deploy everything to GKE


UPDATE ON TASK
Completed the project of building and deploying a web application that prints the reverse IP of incoming requests. The code was written in nodejs.
I utilized a set of modern tools and practices to automate the CI/CD pipeline, enhance security, and streamline deployment on Google Kubernetes Engine (GKE) using GCP Autopilot.

Repository Structure:

Application Source Code and CI/CD Workflow:
Source code Repository: https://github.com/daviinaa/reverse-deel.git
The repository contains the application source code along with GitHub Actions workflows for continuous integration. The CI workflow builds the Docker image, pushes it to Docker Hub, and triggers the ArgoCD deployment.


Argocd Repository: https://github.com/daviinaa/argocd-manifests.git
This repository includes ArgoCD manifests to set up ArgoCD on the Kubernetes cluster, add the cluster to ArgoCD, and declare application sets and projects for efficient management.


Helm Repository: https://github.com/daviinaa/helm-chart.git
Helm charts were used for templating Kubernetes resources such as deployment, ingress, service, and horizontal pod autoscaler. The repository contains reusable chart templates for easy configuration.
CI/CD Pipeline:

Continuous Integration:
Leveraged GitHub Actions for CI workflows.
Automated the build process of the Docker image and pushed it to Docker Hub, and then used the RUN NUMBER as the image tag.

Continuous Deployment:
The deploy step basically involed using a sed replacement script to find the image and tag it with the new tage from the previous build process.
Utilized ArgoCD for declarative and automated Kubernetes deployments.
Configured ArgoCD application sets and projects to manage applications efficiently.
Kubernetes Deployment:

Cluster:
GCP Autopilot was chosen for Kubernetes cluster management, providing a serverless, managed Kubernetes experience.
Application Deployment:

Helm charts were employed for defining and templating Kubernetes resources.
Configured deployment, ingress, service, and horizontal pod autoscaler using Helm templates.

Security Considerations:
Implemented best practices for securing the CI/CD pipeline, such as using secrets for sensitive information.
Leveraged GCP security features and policies for secure Kubernetes cluster management.

Cost Optimisation:
Horozontal pod Autoscaler: this scales up and down based on the application requirement. the GKE also ensures that only the exact resource needed for deployment would be used, and these help save cose in terms of memory and cpu utilisation (compute)
This also ensures high reliability and scalability

Final Deployment:
The deployed application can be accessed at http://35.226.27.83/ 
In summary, this project focused on reliability, cost, scalability, automation and security, utilizing GitHub Actions for CI, ArgoCD for CD, Helm charts for Kubernetes resource templating, and GCP Autopilot for a managed Kubernetes cluster. The overall architecture ensures a streamlined and secure deployment process, adhering to best practices in the DevOps domain.
