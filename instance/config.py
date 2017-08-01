DATABASE_URL = 'postgresql://jemnhall:password@localhost/usda'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# variables for the USDA search API
NDBNO_TOTAL = 200000
LAST_SR = 28
API_KEY = '7WqOHQdC2shEfBrx25bIEwxBkvUkYTHMoHYlLWL8' #1000 requests/hour
q = ''
ds = ''
fg = ''
sort = 'n'
mx = 1000 # max is 1500
offset = 1
formt = 'json'
q = ''

# special api request to get meta information on database (total number of items, standard reference version)
initial_search_request = 'https://api.nal.usda.gov/ndb/search/?format=json&q=&sort=n&max=1&offset=0&api_key=7WqOHQdC2shEfBrx25bIEwxBkvUkYTHMoHYlLWL8'

# search API
search_api_request = 'https://api.nal.usda.gov/ndb/search/?format={}&q={}&sort={}&max={}&offset={}&api_key={}'.format(formt, q, sort, mx, offset_temp, API_KEY)
