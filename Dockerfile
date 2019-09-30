FROM python:3.7
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./movies_app app/movies_app
WORKDIR /app
EXPOSE 8000
RUN cd movies_app && python3 manage.py test -v 2
RUN python3 movies_app/manage.py flush --no-input
RUN python3 movies_app/manage.py makemigrations
RUN python3 movies_app/manage.py migrate
ENTRYPOINT ["python3", "movies_app/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]