#!/bin/bash

images_name=$1
container_id=$(docker ps -a | grep $images_name | awk '{print $1}')
if [[ '' == $container_id ]]; then
  exit 1;
fi
# stop one running containers
echo '####################################################'
echo 'Stopping running containers (if available)...'
echo '####################################################'
docker stop $container_id

# remove one stopped containers
echo '####################################################'
echo 'Removing containers ..'
echo '####################################################'
docker rm $container_id


# remove one images
echo '####################################################'
echo 'Removing images ...'
echo '####################################################'
docker rmi $images_name