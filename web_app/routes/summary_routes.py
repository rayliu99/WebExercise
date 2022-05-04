# web_app/routes/weather_routes.py

from app.pokemon_service import poke
from flask import Blueprint, request, jsonify, render_template, redirect, flash # FYI new imports
from IPython.display import Image, display
from app.pokemon_service import poke

summary_routes = Blueprint("summary_routes", __name__)

@summary_routes.route("/pokemon")
def pokemon():
    print("Pokemon...")
    return render_template("pokemon.html")


@summary_routes.route("/summary", methods=["POST"])
def summary():

    print("FORM DATA:", dict(request.form))
    request_data = dict(request.form)
    #get userinput from pokemon.html
    userinput1 = request_data.get("Color")
    userinput2 = request_data.get("Personality")
    userinput3 = request_data.get("age")
    userinput4 = request_data.get("season")
    userinput5 = request_data.get("special")

    results, image_url = poke(userinput1 = userinput1, userinput2 = userinput2,userinput3 = userinput3,userinput4 = userinput4,userinput5 = userinput5)

    if results:
        return render_template("summary.html", x = results, image_url = image_url)

    

