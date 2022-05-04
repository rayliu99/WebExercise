from app.pokemon_service import poke

def testpokemon1(): 
    results, image_url = poke(userinput1 = "A", userinput2 = "B",userinput3 = "C",userinput4 = "A",userinput5 = "A")

    assert image_url == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/250.png"
    assert results == "you are the legend! As a Ho-Oh, you're very graceful. But you like to be by yourself, so even your friends don’t know if you really exist. Try to be a little bit more approachable!"

def testpokemon2(): 
    results, image_url = poke(userinput1 = "D", userinput2 = "D",userinput3 = "D",userinput4 = "D",userinput5 = "D")

    assert image_url == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    assert results ==  "You are a rascal! As a Pichu, you're cute, but a little bit cheeky. Almost everybody likes you despite your problems with authority figures. You’ve got a lot of potential, so use it for something good!"

def testpokemon3(): 
    results, image_url = poke(userinput1 = "B", userinput2 = "B",userinput3 = "D",userinput4 = "D",userinput5 = "D")

    assert image_url == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png"
    assert results == "You are the powerhouse! You're a Dragonite! You're cute, soft, strong, and almost a legend! Trainers love to have you on their team because of your versatility. Even though you’re quite a good person you can get mad very fast!"

def testpokemon4(): 
    results, image_url = poke(userinput1 = "C", userinput2 = "C",userinput3 = "C",userinput4 = "C",userinput5 = "C")

    assert image_url == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"
    assert results == "You are a freak!You're a very weird fellow, but a strong one. Everybody that dares to mess with you will get obliterated. You try to stay alone, but people tend to get on your nerves."

def testpokemon5(): 
    results, image_url = poke(userinput1 = "B", userinput2 = "B",userinput3 = "C",userinput4 = "C",userinput5 = "C")

    assert image_url == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"
    assert results == "You are a cool guy! As a charmander, you're probably one of the coolest folks around. Everybody likes you, except for yourself. Sometimes you’re quite insecure, and you try to hide that by being mean to others."