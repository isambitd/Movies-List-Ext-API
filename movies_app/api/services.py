import requests
import time
from .models import Movie, People

LAST_SYNCED = 0


def sync_db(force_update=False):
    global LAST_SYNCED
    new_movie_count = 0
    new_people_count = 0
    new_people_in_movie_count = 0
    synced = False
    if time.time() - LAST_SYNCED > 60 or force_update is True:
        response = requests.get("https://ghibliapi.herokuapp.com/films")
        if response.status_code == 200:
            for i in response.json():
                me = Movie.objects.filter(movie_id=i["id"])
                if me.count() == 0:
                    m = Movie(movie_id=i["id"], title=i["title"], description=i["description"],
                              director=i["director"], producer=i["producer"])
                    m.save()
                    new_movie_count += 1
                    print('Adding a new movie')
                else:
                    print("movie exists")

        response = requests.get("https://ghibliapi.herokuapp.com/people")
        if response.status_code == 200:
            for i in response.json():
                p_data = None
                pe = People.objects.filter(people_id=i["id"])
                if pe.count() == 0:
                    p_data = People(people_id=i["id"], name=i["name"], gender=i["gender"],
                                    age=i["age"], eye_color=i["eye_color"], hair_color=i["hair_color"])
                    p_data.save()
                    new_people_count += 1
                    print('Adding a new people')
                else:
                    print("people exists")
                for j in i["films"]:
                    ml_resp = requests.get(j)
                    if ml_resp.status_code == 200:
                        ml_data = ml_resp.json()
                        ml = Movie.objects.filter(movie_id=ml_data["id"])
                        if ml.count() > 0:
                            mlpl = ml[0].people.filter(people_id=i["id"])
                            if mlpl.count() == 0:
                                mlc = Movie.objects.get(
                                    movie_id=ml_data["id"])
                                mlc.people.add(
                                    p_data) if p_data != None else mlc.people.add(pe[0])
                                new_people_in_movie_count += 1
                                print("Adding people to movie")
                            else:
                                print("people in movie list exists")
        print("Sync Done!")
        print("new movies added: ", new_movie_count)
        print("new people added: ", new_people_count)
        print("new people mapped to movie: ", new_people_in_movie_count)
        LAST_SYNCED = time.time()
        synced = True
    return new_movie_count, new_people_count, new_people_in_movie_count, synced
