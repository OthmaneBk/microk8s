# flask-postgres-redis
docoker, github actions, and k8s

# Step 1 docker compose
- clone this project in your local machine (choose the mounted directory in multipass )
- run the app in your multipass primary and test it using curl you must see hello from docker
- take a look at the source code and create your test plan (from database to endpoints)
- as soon as it is ok make down to your containers
# Step 2 convert dcoker compose to configmap, deployment and services
- download and install locally kompose : https://github.com/kubernetes/kompose/blob/main/docs/installation.md#docker
- convert your compose.yaml, you must see 1 configmap file, three deployment and services files

# Step 3 deploy in K8s
- Check if microk8s is running
- Verify your nodes, pods, deployement and services (one node and no pods)
- First problem to resolve : backend image is a private one so tou must register it (in docker hube or locally in mikrok8s)
- Apply all files in order : start with configmap file, and db deployement file
- Check that your pod is healthy and verify your logs to be sur tht the databse was created
- Apply all the remaining files and check that all is ok
- Test from inside the cluster you must see hello from docker
- What about from outside your cluster find the error and correct it and test again

Good lucky you are free to use gpt
