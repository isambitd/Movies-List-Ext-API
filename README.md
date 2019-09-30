## If you have docker installed in your system ##

Go inside the folder `cd movies_app_cont`

Run this in your terminal `sh start.sh`

While creating image it will run the test cases and output in the terminal

It will deploy docker instance, create an image and run container with the django server at port number 8000

Open browser and load `localhost:8000/movies` 

To check live logs 
`docker ps -aqf "name=movies-app-cont" | xargs docker logs -f`

Once done clean everything with 
`sh clean.sh`



## If you DONT have docker installed in your system ##

Go inside the folder `cd movies_app_cont`

Assuming you have python3 installed in your system

Run `pip install -r requirements.txt`

Run `pip3 install -r requirements.txt`

Run `python3 movies_app/manage.py flush --no-input`

Run `python3 movies_app/manage.py makemigrations`

Run `python3 movies_app/manage.py migrate`

Finally Run `python3 movies_app/manage.py runserver 8000`

Open browser and load `localhost:8000/movies` 

To run the test cases

Run `python3 movies_app/manage.py test -v 2`

Thank you :)


