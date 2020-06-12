from django.test import TestCase, Client
import requests


class RepoTrend(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        url = 'https://api.github.com/search/repositories?q=created:>{}&sort={}&order={}&page={}&per_page={}'
        date = '2020-06-10'
        sort = 'stars'
        order = 'desc'
        page = '1'
        per_page = '100'
        self.git_response = requests.get(url.format(date, sort, order, page, per_page)).json()

    def test_receiving_items(self):
        """Check if we receive 100 items as expected """
        self.assertEqual(len(self.git_response['items']), 100)
