# To activate the .venv [.venv\Scripts\Activate.ps1] or .venv\Scripts\activate in the terminal.
# To deactivate .venv [deactivate] in the terminal.

# The reason for virtual enviromenst are used to create a virtual enviroment and install packages that are specific
# to the project rather than the main system (global system)
# We use them in development but do not send them to github or repositories.

# pypi.org is a website for python package index.

# We can include a list of requierments with the github uploads. command below in termanil to create
# py -m pip freeze > requirements.txt

# To ignore a files that may bee in the project that we wish to not send to github we can create a .gitignore file
# It this file we can include the .venv & .env

# This weather project will allow us to search the web and requests the weather from a service and returns the current weather.

# Website openweathermap.org and sign up for a free account.
# Search site for API keys & copy the key
# We can create a .env file which is the enviroment file where we will set 'API_KEY' to = the key copied

# Search to API on website, find the current weather data & copy the API call.

# We can edit the API key wit a unit of measure in the website list.
# metric for celsius
#


import requests
from dotenv import load_dotenv  # Helps get enviroment value not global
import os  # Built into python

load_dotenv()  # calls 'load_dotenv' to load in the enviroment variables so we can retrieve them.(i.e. API_KEY)

# Create a function that will call the weather conditions


def get_current_weather():
    # welcome message when function called.
    print('\n*** Get Current Weather Conditions ***\n')

    # Creates a variable with an input that the user can select a specific city name
    city = input("\nPlease enter a city name:\n")

    # Creates a variable that will call the website API
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    # Note the url has been modified to get the API_KEY and query the city along with the units of measure.

    # Just as a check to make sure what is included as expected.
    print(request_url)

    # Creates a variable that
    # weather_data = requests.get(request_url).json()

    get_current_weather()  # Call the function.

# Create the variable to request the url.
# request_url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}&units=metric'
# Note using '&units=metric' we will get the units in Celsius.
