#!/bin/bash
# Simple script to restart to rebuild and restart the docker container 
# For testing puroposes (only?)
# Also is probably not needed for actual deployment, but an artefact of 
# my shitty setup/..

service="test"
echo "services available: \n - challenge \n- activity-logger"
sudo docker build -f ./"${service[@]}"/Dockerfile -t "${service[@]}"-image ./
# need to do the stop and rm in an if statement, unless these have been done before.
# cleanup will remove the standardised service-image, 

# Cleanup on port: 
PORT="80"
cleanup(){
  sudo docker container stop "${service[@]}"-container &&
  sudo docker container rm "${service[@]}"-container
}
cleanport(){
  ID=$(\
     sudo docker container ls -a --format="{{.ID}}\t{{.Ports}}" |\
     grep ${PORT} |
     awk '{print $1}')
  sudo docker container stop ${ID} && sudo docker container rm ${ID}
}

# Catch exceptoions from cleanup here, and continue... 
cleanup || true
cleanport || true

# Still possible to encounter port-issue with multiple containrs running. 
# e.g. activity-logger running on 80:80 will block the challenge from starting. 
sudo docker run -d --name "${service[@]}"-container -p 80:80 "${service[@]}"-image
