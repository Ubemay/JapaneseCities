from fastapi import FastAPI
import requests

app = FastAPI()

@app.get('/')
def index():
    return "Hello there! Welcome to the site about cities in Japan!!"

@app.get('/japancities')
def cities():
    return 'Choose a city in Japan that interests you: ' \
           'Kyoto, Tokyo, Osaka, Saitama          ' \
            \
            \
            '(If you choose Osaka, you would write in url row like "http://127.0.0.1:8000/japancities/Osaka")'

@app.get('/japancities/{city}')
def greetings(city):
    db_cities = {
        'Kyoto': {
            'area': 828,
            'population': 1500000,
            'founded': 1889
        },
        'Tokyo': {
            'area': 2194,
            'population': 14000000,
            'founded': 1603
        },
        'Osaka': {
            'area': 223,
            'population': 2700000,
            'founded': 1889
        },
        'Saitama': {
            'area': 217,
            'population': 1200000,
            'founded': 2001
        }
    }

    if city in db_cities:
        result_1 = db_cities[city]
    else:
        result_1 = "Unfortunately, we don't have information about this city"

    return result_1


@app.get('/japancities/{city}/QFA')
def QFA():
    url = 'https://animechan.vercel.app/api/random'
    response = requests.get(url).json()
    result_2 = "You also know that Japan is considered the birthplace of anime, if you are interested, then go to the page and you will be given a random quote from the anime '%s': %s" % (response['anime'] ,response['quote'])
    return result_2