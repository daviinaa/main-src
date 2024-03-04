##first take of the assessment using argocd & helm to deploy 

This project builds a web application that that prints the origin public IP of any request it receives in reverse.

##specify where db would be stored

Builds a docker image of the app and an helm chart.
CI\CD pipeline using github actions that builds the docker image, push to a docker registry and then Argocd deploy everything to GKE