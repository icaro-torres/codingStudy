myJedis = {
    "id" : "<empty>",
    "nome" : "<empty>",
    "especie" : "<empty>",
    "afiliacao" : "<empty>",
    "sabre_cor" : "<empty>",
    "nivelForca" : "<empty>",
}

myPlanets = {
    "nome" : "<empty>",
    "clima" : "<empty>",
    "terreno" : "<empty>",
    "populacao" : "<empty>",
}

jediList = []
planetList = []

import csv
import copy

# Lê Jedi
with open('jedis.csv') as csvfile:
    csvReader = csv.DictReader(csvfile)
    next(csvReader)  # Skip the header
    for row in csvReader:
        myJedis = copy.deepcopy(myJedis)
        myJedis["id"] = row["id"]
        myJedis["nome"] = row["nome"]
        myJedis["especie"] = row["especie"]
        myJedis["afiliacao"] = row["afiliacao"]
        myJedis["sabre_cor"] = row["sabre_cor"]
        myJedis["nivelForca"] = row["nivelForca"]
        jediList.append(myJedis)

# Lê Planetas
with open('planets.csv') as csvfile:
    csvReader = csv.DictReader(csvfile)
    next(csvReader)  # Skip the header
    for row in csvReader:
        myPlanets = copy.deepcopy(myPlanets)
        myPlanets["nome"] = row["nome"]
        myPlanets["clima"] = row["clima"]
        myPlanets["terreno"] = row["terreno"]
        myPlanets["populacao"] = row["populacao"]
        planetList.append(myPlanets)

# Exibe Jedi
print("=== Lista de Jedis ===")
for jedi in jediList:
    print(f'ID: {jedi['id']}, Nome: {jedi['nome']}, Especie: {jedi['especie']}, Afiliação: {jedi['afiliacao']}, Sabre: {jedi['sabre_cor']}, Força: {jedi['nivelForca']}')
    
# Exibe Planetas
print("=== Lista de Planetas ===") 
for planet in planetList:
    print(f'Nome: {planet['nome']}, Clima: {planet['clima']}, Terreno: {planet['terreno']}, População: {planet['populacao']}')