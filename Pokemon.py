import json

def makePokemon(rating,height,weight):
    reb = rating[0]["reb"]
    end = rating[0]["endu"]
    str = rating[0]["stre"]
    ft = rating[0]["ft"]
    off = rating[0]["oiq"]
    fg = rating[0]["fg"]
    defs = rating[0]["diq"]
    tp = rating[0]["tp"]
    dnk = rating[0]["dnk"]
    drb = rating[0]["drb"]
    spe = rating[0]["spd"]
    jmp = rating[0]["jmp"]
    healthPoints = (str*end*weight)**(1/2.6)
    attack = ((off*fg*height))**(1/2.5)
    deffense = ((weight*defs*spe))**(1/2.5)
    if(tp == 0):
        tp = 10
    if(ft == 0):
        ft = 15
    if(dnk == 0):
        dnk = 10
    specialAttack = (tp*ft*dnk)**(1/2.5)
    speed = (spe*end*drb)**(1/2.5)
    specialDefense = (str*jmp*reb)**(1/2.5)
    return {"hp" : healthPoints,
            "atk" : attack,
            "def" : deffense,
            "spa" : specialAttack,
            "spe" : speed,
            "spd" : specialDefense
            }


def playerStats(givenName):
    with open('players.json', encoding='utf-8') as f:
        players = json.load(f)['players']
        for x in players:
            if('firstName' in x):
                playerName = x['firstName'] + x['lastName']
            else:
                playerName = str(x['name'])
            if(playerName == givenName):

                playerWeight = x['weight']
                playerHeight = x['hgt']
                playerRatings = x['ratings']
                return makePokemon(playerRatings, playerHeight, playerWeight)


def adjStats(givenPlayerStats):
    aStats = {"hp" : 0,
        "atk": 0,
        "def": 0,
        "spa": 0,
        "spd": 0,
        "spe": 0,
        "tot": 0,
    }

    stats = getStats()

    NBAHIGH = getMaxNBA()
    NBALOW = getMinNBA()
    POKEHIGH = getMaxPoke()
    POKELOW = getMinPoke()

    slopes = {"hp": 0,
              "atk": 0,
              "def": 0,
              "spa": 0,
              "spd": 0,
              "spe": 0,
              }

    for stat in stats:
        slopes[stat] = (NBAHIGH[stat] - NBALOW[stat]) / (POKEHIGH[stat] - POKELOW[stat])

    for i in givenPlayerStats:
        adj = int((givenPlayerStats[i] - NBALOW[i]) / slopes[i])
        aStats[i] = adj
    total = 0
    for j in aStats:
        total += aStats[j]
    aStats["tot"] = total
    return aStats


def getStats():
    return ["hp", "atk", "def", "spa", "spd", "spe"]


def getMaxNBA():
    maxStats = {"hp": 0,
            "atk": 0,
            "def": 0,
            "spa": 0,
            "spd": 0,
            "spe": 0,
            }

    with open('players.json') as f:
        players = json.load(f)['players']
        for x in players:
            playerWeight = x['weight']
            playerHeight = x['hgt']
            playerRatings = x['ratings']
            stats = makePokemon(playerRatings, playerHeight, playerWeight)
            for stat in getStats():
                if stats[stat] > maxStats[stat]:
                    maxStats[stat] = stats[stat]
    return maxStats


def getMinNBA():
    minStats = {"hp": 9999999999999990,
                "atk": 9999999999999990,
                "def": 9999999999999990,
                "spa": 9999999999999990,
                "spd": 9999999999999990,
                "spe": 9999999999999990,
                }

    with open('players.json') as f:
        players = json.load(f)['players']
        for x in players:
            playerWeight = x['weight']
            playerHeight = x['hgt']
            playerRatings = x['ratings']
            stats = makePokemon(playerRatings, playerHeight, playerWeight)
            for stat in getStats():
                if stats[stat] < minStats[stat]:
                    minStats[stat] = stats[stat]
    return minStats



def getMaxPoke():
    maxStats = {"hp": 0,
                "atk": 0,
                "def": 0,
                "spa": 0,
                "spd": 0,
                "spe": 0,
                }

    with open('pokemon.json') as f:
        pokedex = json.load(f)
        count = 0
        for pokemon in pokedex:
            if count <=1008:
                for stat in getStats():
                    if pokedex[pokemon]['baseStats'][stat] > maxStats[stat]:
                        maxStats[stat] = pokedex[pokemon]['baseStats'][stat]
    return maxStats


def getMinPoke():
    minStats = {"hp": 9999,
                "atk": 9999,
                "def": 9990,
                "spa": 9990,
                "spd": 9990,
                "spe": 9990,
                }

    with open('pokemon.json') as f:
        pokedex = json.load(f)
        count = 0
        for pokemon in pokedex:
            if count <= 1008:
                for stat in getStats():
                    if pokedex[pokemon]['baseStats'][stat] < minStats[stat]:
                        minStats[stat] = pokedex[pokemon]['baseStats'][stat]
    return minStats


def topThree(givenPlayerName):
    with open('pokemon.json') as f:
        pokedex = json.load(f)


    stats = getStats()

    NBAHIGH = getMaxNBA()
    NBALOW = getMinNBA()
    POKEHIGH = getMaxPoke()
    POKELOW = getMinPoke()

    slopes = {"hp" : 0,
            "atk": 0,
            "def": 0,
            "spa": 0,
            "spd": 0,
            "spe": 0,
    }

    for stat in stats:
        slopes[stat] = (NBAHIGH[stat]-NBALOW[stat])/(POKEHIGH[stat]-POKELOW[stat])

    count = 0
    minDif = [9999999999, "name"]
    minList = [minDif,minDif,minDif]
    playerStatsats = playerStats(givenPlayerName)

    for pokemon in pokedex:
        try:
            pokedex[pokemon]["baseSpecies"]
        except:
            if count <= 1008:
                squaredDiff = 0
                for stat in stats:
                    adj = (playerStatsats[stat] - NBALOW[stat]) / slopes[stat]
                    squaredDiff += (adj - pokedex[pokemon]['baseStats'][stat])**2

                    #if best
                if squaredDiff < minList[0][0]:
                    minList[2] = minList[1]
                    minList[1] = minList[0]
                    minList[0] = [squaredDiff, pokemon]
                    #if 2nd
                elif squaredDiff < minList[1][0]:
                    minList[2] = minList[1]
                    minList[1] = [squaredDiff, pokemon]
                    #if 3rd
                elif squaredDiff < minList[2][0]:
                    minList[2] = [squaredDiff, pokemon]
            count += 1
    ret = []
    ret.append(minList[0][1])
    ret.append(minList[1][1])
    ret.append(minList[2][1])
    return ret

givenName = "Jamal Murray"
print(topThree(givenName))
print(adjStats(playerStats(givenName)))
