import datetime
import json

import requests
from requests.utils import quote


class ContributionsLoader(object):
    def __init__(self):
        # TODO: Move to config when in prod
        self.uk_wiki_url = 'https://uk.wikipedia.org/w/api.php'
        self.default_params = {
            'format': 'json',
            'prop': 'revisions',
            'rvlimit': 1000,
            'action': 'query'
        }

    def __load_contribs_for_page(self):
        pass

    def _get_contribs(self, title, date_time):
        params = {'rvstart': date_time, 'titles': quote(title)}
        params = dict(self.default_params, **params)
        contribs = []
        last_revision = None

        while True:
            response = requests.get(
                self.uk_wiki_url,
                params=dict(self.default_params, **params),
            )

            res = response.content.decode('utf-8')
            dataJson = json.loads(response)
            pages = dataJson["query"]["pages"]
            key = list(pages.keys())[0]
            revisions = pages[key]['revisions']
            users = users + [rev["user"] for rev in revisions]
            revs = revs + [rev for rev in revisions]

            if "continue" in dataJson.keys():
                cont = dataJson["continue"]["rvcontinue"]
                params["rvcontinue"] = cont
            else:
                break
        last_revision = revs[-1]
        page_born = datetime.datetime.strptime(last_revision['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
        timestamp_datetime = datetime.datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%SZ')

        delta = timestamp_datetime - page_born
        return users, delta.days



if __name__ == '__main__':
    cont = ContributionsLoader()
    cont._get_contribs('Lviv', '2018-05-20T00:00:00Z')