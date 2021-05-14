import csv
path = "M:\pk\pokemonDashboard\main"
evo = open(path+"\PokemonEvolutions.csv","r")
evocsv = list(csv.reader(evo, delimiter=","))
poke = open(path+"\Pokemon.csv","r")
pokecsv = list(csv.reader(poke, delimiter=","))

evo.close()
poke.close()

#clears csv file

with open(path+"\Pokemon.csv","w")as f:
    f.write("")

temppokecsv = pokecsv
with open("temp.csv","w") as f:
    for i in temppokecsv:
        for x in i:
            f.write(x)
            f.write(",")
        f.write("\n")

for row in pokecsv:
    for row in pokecsv:
        for row1 in evocsv:
            for i in row1:
                if row[1] == i:
                    temp1 = row[1]
                    temp2 = i
                    print(temp1, temp2)
                    pokecsv.pop(row.index(temp1))

                    with open(path+"\Pokemon.csv","a") as poke:
                        for i in pokecsv[row.index(temp1)]:
                            poke.write(i)
                            poke.write(",")
                        poke.write("\n")
