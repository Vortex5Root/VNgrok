#!/bin/bash

REPO_NAME="Loadbalancer-SSHTunnel"
GITHUB_USER_OR_ORG="Vortex5Root"
GITHUB_REF="$1"

if [ -d "$REPO_NAME" ]; then
    cd ./$REPO_NAME
else
    git clone https://github.com/$GITHUB_USER_OR_ORG/$REPO_NAME.git
    cd $REPO_NAME
fi

# Example deployment script
echo "Deploying the application..."

# Pull the latest changes
git pull origin $GITHUB_REF



echo "Deployment to $GITHUB_REF branch completed."
