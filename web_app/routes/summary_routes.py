# web_app/routes/weather_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash # FYI new imports
from IPython.display import Image, display
#from app.pokemon_service import poke

summary_routes = Blueprint("summary_routes", __name__)

@summary_routes.route("/pokemon")
def pokemon():
    print("Pokemon...")
    return render_template("pokemon.html")


@summary_routes.route("/summary", methods=["GET","POST"])
def summary():

    #if request.method == "GET":
    #    print("URL PARAMS:", dict(request.args))
    #    request = dict(request.args)
    #elif request.method == "POST": # the form will send a POST
    #    print("FORM DATA:", dict(request.form))
    #    request_data = dict(request.form)





    #myarray = ["", "", "", "", ""]
    #strong = 0 
    #extrovert = 0
    #personable = 0
    #x = ""
#
#
    #input1 = request.form["Color"]
    #input2 = request.form["Personality"]
    #input3 = request.form["age"]
    #input4 = request.form["season"]
    #input5 = request.form["special"]
#
    #myarray[0] = input1
    #myarray[1] = input2
    #myarray[2] = input3
    #myarray[3] = input4
    #myarray[4] = input5
#
    ##validate user's input
    #for i in myarray:
    #    if i == "A": 
    #        strong = strong + 1
    #    elif i == "B":
    #        strong = strong + 2
    #    elif i == "C":
    #        extrovert = extrovert + 2
    #    elif i == "D":
    #        personable = personable + 2
    ##determine what animal you are based on your personality (the values of strong/extrovert/personable) 
    #if personable >= 4 and personable <= 10 and extrovert >= 4 and extrovert <=10 and strong >= 0 and strong <= 3:
    #    image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    #    x = "You are a rascal! As a Pichu, you're cute, but a little bit cheeky. Almost everybody likes you despite your problems with authority figures. You’ve got a lot of potential, so use it for something good!"
    #if personable >= 4 and personable <= 10 and extrovert >= 0 and extrovert <=3 and strong >= 0 and strong <= 3:
    #    image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    #    x= "You are a rascal! As a Pichu, you're cute, but a little bit cheeky. Almost everybody likes you despite your problems with authority figures. You’ve got a lot of potential, so use it for something good!"
    #if personable >= 0 and personable <= 3 and extrovert >= 4 and extrovert <=10 and strong >= 0 and strong <= 3:
    #    image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"
    #    x = "You are a freak!You're a very weird fellow, but a strong one. Everybody that dares to mess with you will get obliterated. You try to stay alone, but people tend to get on your nerves."
    #if personable >= 0 and personable <= 3 and extrovert >= 4 and extrovert <=10 and strong >= 4 and strong <= 10:
    #    image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"
    #    x = "You are a cool guy! As a charmander, you're probably one of the coolest folks around. Everybody likes you, except for yourself. Sometimes you’re quite insecure, and you try to hide that by being mean to others."
    #if personable >= 0 and personable <= 3 and extrovert >= 0 and extrovert <=3 and strong >= 0 and strong <= 3:
    #    image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/250.png"
    #    x = "you are the legend! As a Ho-Oh, you're very graceful. But you like to be by yourself, so even your friends don’t know if you really exist. Try to be a little bit more approachable!"
    #if personable >= 0 and personable <= 3 and extrovert >= 0 and extrovert <=3 and strong >= 4 and strong <= 10:
    #    image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/250.png"
    #    x = "you are the legend! As a Ho-Oh, you're very graceful. But you like to be by yourself, so even your friends don’t know if you really exist. Try to be a little bit more approachable!"
    #if personable >= 4 and personable <= 10 and extrovert >= 0 and extrovert <=3 and strong >= 4 and strong <= 10:
    #    image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png"
    #    x = "You are the powerhouse! You're a Dragonite! You're cute, soft, strong, and almost a legend! Trainers love to have you on their team because of your versatility. Even though you’re quite a good person you can get mad very fast!"
    #
    return render_template("summary.html")

    

