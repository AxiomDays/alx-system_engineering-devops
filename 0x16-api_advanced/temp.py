#!/usr/bin/python3
"""
0-subs
script to query the API and return the number of subscribers
"""
def number_of_subscribers(subreddit):
    """
    the function in question
    """
    if __name__ == "__main__":
        import requests

        CLIENT_ID = "RHsVSB48R90oK68HCGwizQ"
        SECRET_KEY = "P0ofQX8iQBHccbGpsGMAUBAAfGdegw"

        auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

        data = {
                'grant_type': 'password',
                'username': 'Axiom_Days',
                'password': 'excalibro'
                }

        headers = {'User-Agent': 'MyAPI/0.0.1'}
        res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

        TOKEN = res.json()['access_token']
        headers['authorization'] = f'bearer {TOKEN}'

        res = requests.get('https://oauth.reddit.com/r/{}/hot'.format(subreddit), headers=headers).json()

        for post in res['data']['children']:
            print('{}: {}'.format(post['data']['title'], post['data']['url']))

number_of_subscribers("Megaten")
