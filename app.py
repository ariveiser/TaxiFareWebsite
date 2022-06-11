import streamlit as st
import datetime
import requests
import random
import pandas as pd
from datetime import date

'''
# **Taxi Fare Web 🚖**
'''

st.markdown('''
## 💡 *This is my first website* :sunglasses:

### And it's supposed to predict taxi fares in NYC 🗽''')



# callback to update emojis in Session State
# in response to the on_click event
def random_emoji():
    st.session_state.emoji = random.choice(emojis)

# initialize emoji as a Session State variable
if "emoji" not in st.session_state:
    st.session_state.emoji = "👈"

emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼"]

st.button(f"My spirit animal is {st.session_state.emoji}", on_click=random_emoji)

d= st.date_input(
    "When do you need your cab? 📆",
    datetime.date(2019, 7, 6))
st.write('You want a cab on:', d)

t = st.time_input('Ok, but what time do you need it? ⏱️', datetime.time(8, 45))

st.write('you will be picked up around', t ,'🚕')

st.text('Now we will need you to get into google maps and get some info: search for your pick up-point and look for the latitude and longitude')

pick_up_latitude = st.number_input('Here you will copy your latitude', 40.7579747)

st.write('latitude of pick-up point is ', pick_up_latitude)

pick_up_longitude = st.number_input('Here you will copy your longiude', -73.9855426)

st.write('longitude of pick-up point is ', pick_up_longitude)

st.text('Great! Now it is time to do the same, but now for your destination')

dropoff_latitude = st.number_input('Here you will copy your destination\'s latitude', 40.7555362)

st.write('latitude of destination is ', dropoff_latitude)

dropoff_longitude = st.number_input('Here you will copy your destination\'s longiude', -73.9817694)

st.write('longitude of destination is ', dropoff_longitude)

st.write('Good, now, how many people are going to hop-on?')

passengers = st.number_input('Insert a number', min_value=1, max_value=4, value=1)

st.write('we are going to be ', passengers, "people" )


url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

#    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

datetime = f'{d} {t}'
#pickup_datetime = datetime.strftime("%Y-%m-%d %H:%M:%S UTC")


X_pred = {"pickup_datetime": datetime,
        "pickup_longitude": pick_up_longitude,
        "pickup_latitude": pick_up_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude":dropoff_latitude,
        "passenger_count":passengers}

fare_json = requests.get(url, params=X_pred).json()
#st.write(fare_json)

fare = fare_json["fare"]

st.write('Your fare will be ', fare, "now you are broke" )
