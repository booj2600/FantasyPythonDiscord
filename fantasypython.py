# import xml parser
from lxml import objectify

# Yahoo API authorization
from yahoo_oauth import OAuth2
oauth = OAuth2(None, None, from_file='yahoo_api_oauth2.json')

# imports webbrowser
import webbrowser

if not oauth.token_is_valid():
    oauth.refresh_access_toke()

# Example
# url = 'https://fantasysports.yahooapis.com/fantasy/v2/team/223.l.431.t.9/stats;type=week;week=2'
url = 'https://fantasysports.yahooapis.com/fantasy/v2/league/.l.315895/teams'
# response = oauth.session.get(url, params=payload)
response = oauth.session.get(url)

#
# print(response)
print(response.content)

# root = objectify.fromstring(response.content)
# team_logo = str(root.team.team_logos.team_logo.url)

# opens team logo in browser
# webbrowser.open(team_logo)

# import ipdb; ipdb.set_trace()