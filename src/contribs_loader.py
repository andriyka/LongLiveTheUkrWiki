import datetime
import json
from urllib.parse import quote

import requests


class ContributionsLoader(object):
    def __init__(self):
        # TODO: Move to config when in prod
        self.uk_wiki_url = 'https://uk.wikipedia.org/w/api.php'
        self.default_params = {
            'format': 'json',
            'prop': 'revisions',
            'rvlimit': 500,
            'action': 'query'
        }
        self.contrib_data = {}

    def _get_contribs(self, title, date_time):
        params = {'rvstart': date_time, 'titles': quote(title)}
        params = dict(self.default_params, **params)
        contribs = []
        revs = []

        while True:
            response = requests.get(
                self.uk_wiki_url,
                params=dict(self.default_params, **params),
            )

            res = response.content.decode('utf-8')
            data = json.loads(res)
            pages = data['query']['pages']
            key = list(pages.keys())[0]
            revisions = pages[key]['revisions']
            contribs.extend([rev['user'] for rev in revisions])
            revs.extend(revisions)

            if 'continue' in data.keys():
                params['rvcontinue'] = data['continue']['rvcontinue']
            else:
                break
        last_revision = revs[-1] if revs else None
        first_rev = datetime.datetime.strptime(last_revision['timestamp'], '%Y-%m-%dT%H:%M:%SZ') if last_revision \
            else None
        return contribs, first_rev

    def get_contribs(self, pages, on_date):
        contribs = []
        revs = []

        for page in pages:
            c, lr = self._get_contribs(page, on_date)
            contribs.extend(c)
            revs.append(lr)


if __name__ == '__main__':
    cont = ContributionsLoader()
    cont._get_contribs('Main_Page', '2018-05-20T00:00:00Z')