## Cleaning Docker images
function clean_images {
    if docker images | awk '{ print $1,$3 }' | grep none
    then 
        docker images | awk '{ print $1,$3 }' | grep none | awk '{print $2 }' | xargs -I {} docker rmi {}
    fi
    if docker images | awk '{ print $1,$3 }' | grep movies-app-img
    then 
        docker images | awk '{ print $1,$3 }' | grep movies-app-img | awk '{print $2 }' | xargs -I {} docker rmi {}
    fi
}
function clean_containers {
    if docker ps -a | grep Exit
    then 
        docker ps -a | grep Exit | cut -d ' ' -f 1 | xargs docker rm
    fi
    if docker ps -a | grep Created
    then
        docker ps -a | grep Created | cut -d ' ' -f 1 | xargs docker rm
    fi
    stop_and_clean_movies_app_cont
}

function stop_and_clean_movies_app_cont {
    container_id=`docker ps -aqf "name=movies-app-cont" `
    if [ ! -z "$container_id" ]
    then 
        docker ps | awk '{ print $1 }' | grep "$container_id" | awk '{print $1 }' | xargs -I {} docker stop {}
    fi
    if [ ! -z "$container_id" ]
    then 
        docker rm $container_id
    fi
}

function build_and_run {
    docker build -t movies-app-img .
    docker run -it --name=movies-app-cont -p 8000:8000 -d movies-app-img
    container_id=`docker ps -aqf "name=movies-app-cont" `
    
}

function clean_and_start {
    clean_containers
    clean_images
    build_and_run
}

function start {
    stop_and_clean_movies_app_cont
    build_and_run
}

# clean_and_start
start

echo "You can access the webpage at localhost:8000"

echo "Thank you :)"