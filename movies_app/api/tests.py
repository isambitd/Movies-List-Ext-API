import requests
from django.test import TestCase
from .services import sync_db


class TestMovieApp(TestCase):

    def setUp(self):
        self.films_endpoint = "https://ghibliapi.herokuapp.com/films"
        self.people_endpoint = "https://ghibliapi.herokuapp.com/people"

    def test_studio_ghibli_movies_api_is_up(self):
        response = requests.get(self.films_endpoint)
        self.assertEqual(response.status_code,  200)

    def test_studio_ghibli_people_api_is_up(self):
        response = requests.get(self.people_endpoint)
        self.assertEqual(response.status_code,  200)

    def test_studio_ghibli_movies_api_returning_valid_response(self):
        response = requests.get(self.films_endpoint)
        res_json = response.json()
        for i in res_json:
            self.assertIn('id', i)
            self.assertNotEqual(i["id"], "")

    def test_studio_ghibli_people_api_returning_valid_response(self):
        response = requests.get(self.people_endpoint)
        res_json = response.json()
        for i in res_json:
            self.assertIn('id', i)
            self.assertNotEqual(i["id"], "")

    def test_studio_ghibli_people_with_films_api_returning_valid_response(self):
        response = requests.get(self.people_endpoint)
        res_json = response.json()
        for i in res_json:
            self.assertIn('id', i)
            self.assertNotEqual(i["id"], "")
            self.assertIn('films', i)
            for j in i["films"]:
                resp = requests.get(j)
                self.assertEqual(resp.status_code, 200)
                self.assertIn("id", resp.json())
                self.assertNotEqual(resp.json()["id"], "")

    def test_sync_db(self):
        new_movie_count, new_people_count, new_people_in_movie_count, synced = sync_db()
        self.assertNotEqual(new_movie_count, 0)
        self.assertNotEqual(new_people_count, 0)
        self.assertNotEqual(new_people_in_movie_count, 0)
        self.assertEqual(synced, True)
        new_movie_count, new_people_count, new_people_in_movie_count, synced = sync_db(
            True)
        self.assertEqual(new_movie_count, 0)
        self.assertEqual(new_people_count, 0)
        self.assertEqual(new_people_in_movie_count, 0)
        self.assertEqual(synced, True)
