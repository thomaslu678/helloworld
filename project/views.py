from django.shortcuts import render
from django.http import HttpResponse
from.models import FoodItem

# -------------------
import streamlit as st
import pydeck as pdk
import pandas as pd

# Create your views here.

def home(request):
    context = {
        'foods': FoodItem.objects.all()
    }
    return render(request, 'project/home2.html', context)

def data(request):
    return render(request, 'project/traveler-map.html')


def load_iframe():
    SCATTERPLOT_LAYER_DATA = "https://raw.githubusercontent.com/DeerEdge/Traveler-Discover-Your-Next-Destination/main/Application%20Data%20and%20Documentation%20Files/Attractions%20Data.csv"

    df = pd.read_csv(SCATTERPLOT_LAYER_DATA)

    # Define a layer to display on a map
    layer = pdk.Layer(
        "ScatterplotLayer",
        df,
        pickable=True,
        opacity=0.8,
        stroked=True,
        filled=True,
        get_radius=1000,
        radius_scale=6,
        radius_min_pixels=1,
        radius_max_pixels=100,
        line_width_min_pixels=1,
        get_position=["longitude", "latitude"],
        get_fill_color=[255, 140, 0],
        get_line_color=[0, 0, 0],
    )

    # Set the viewport location
    # view_state = pdk.ViewState(latitude=37.7749295, longitude=-122.4194155, zoom=10, bearing=0, pitch=0)

    # Render
    r = pdk.Deck(layers=[layer], tooltip={"text": "{name}"})
    r.to_html("traveler-map.html")

    return r
