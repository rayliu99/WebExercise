from flask import Blueprint, request, jsonify, render_template, redirect, flash
from IPython.display import Image, display


def poke(userinput1, userinput2, userinput3, userinput4, userinput5):
    myarray = ["", "", "", "", ""]
    strong = 0 
    extrovert = 0
    personable = 0
    x = ""
    myarray[0] = userinput1
    myarray[1] = userinput2
    myarray[2] = userinput3
    myarray[3] = userinput4
    myarray[4] = userinput5

    #validate user's input
    for i in myarray:
        if i == "A": 
            strong = strong + 1
        elif i == "B":
            strong = strong + 2
        elif i == "C":
            extrovert = extrovert + 2
        elif i == "D":
            personable = personable + 2
    #determine what animal you are based on your personality (the values of strong/extrovert/personable) 
    if personable >= 4 and personable <= 10 and extrovert >= 4 and extrovert <=10 and strong >= 0 and strong <= 3:
        image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
        x = "You are a rascal! As a Pichu, you're cute, but a little bit cheeky. Almost everybody likes you despite your problems with authority figures. You’ve got a lot of potential, so use it for something good!"
    if personable >= 4 and personable <= 10 and extrovert >= 0 and extrovert <=3 and strong >= 0 and strong <= 3:
        image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
        x= "You are a rascal! As a Pichu, you're cute, but a little bit cheeky. Almost everybody likes you despite your problems with authority figures. You’ve got a lot of potential, so use it for something good!"
    if personable >= 0 and personable <= 3 and extrovert >= 4 and extrovert <=10 and strong >= 0 and strong <= 3:
        image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"
        x = "You are a freak!You're a very weird fellow, but a strong one. Everybody that dares to mess with you will get obliterated. You try to stay alone, but people tend to get on your nerves."
    if personable >= 0 and personable <= 3 and extrovert >= 4 and extrovert <=10 and strong >= 4 and strong <= 10:
        image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"
        x = "You are a cool guy! As a charmander, you're probably one of the coolest folks around. Everybody likes you, except for yourself. Sometimes you’re quite insecure, and you try to hide that by being mean to others."
    if personable >= 0 and personable <= 3 and extrovert >= 0 and extrovert <=3 and strong >= 0 and strong <= 3:
        image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/250.png"
        x = "you are the legend! As a Ho-Oh, you're very graceful. But you like to be by yourself, so even your friends don’t know if you really exist. Try to be a little bit more approachable!"
    if personable >= 0 and personable <= 3 and extrovert >= 0 and extrovert <=3 and strong >= 4 and strong <= 10:
        image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/250.png"
        x = "you are the legend! As a Ho-Oh, you're very graceful. But you like to be by yourself, so even your friends don’t know if you really exist. Try to be a little bit more approachable!"
    if personable >= 4 and personable <= 10 and extrovert >= 0 and extrovert <=3 and strong >= 4 and strong <= 10:
        image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png"
        x = "You are the powerhouse! You're a Dragonite! You're cute, soft, strong, and almost a legend! Trainers love to have you on their team because of your versatility. Even though you’re quite a good person you can get mad very fast!"
    return x, image_url

   #if __name__ == "__main__":

   #    print(f"RUNNING THE WEATHER SERVICE IN {APP_ENV.upper()} MODE...")

   #    # CAPTURE INPUTS

   #    user_country, user_zip = set_geography()
   #    print("COUNTRY:", user_country)
   #    print("ZIP CODE:", user_zip)

   #    # FETCH DATA

   #    result = get_hourly_forecasts(country_code=user_country, zip_code=user_zip)
   #    if not result:
   #        print("INVALID GEOGRAPHY. PLEASE CHECK YOUR INPUTS AND TRY AGAIN!")
   #        exit()

   #    # DISPLAY OUTPUTS

   #    print("-----------------")
   #    print(f"TODAY'S WEATHER FORECAST FOR {result['city_name'].upper()}...")
   #    print("-----------------")

   #    for forecast in result["hourly_forecasts"]:
   #        print(forecast["timestamp"], "|", forecast["temp"], "|", forecast["conditions"])