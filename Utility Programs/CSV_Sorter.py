import csv
path = "M:\pk\pokemonDashboard\main"
evo = open(path+"\PokemonEvolutions.csv","r")
evocsv = list(csv.reader(evo, delimiter=","))
poke = open(path+"\Pokemon.csv","r")
pokecsv = list(csv.reader(poke, delimiter=","))
evo.close()
poke.close()

#clones csv
temppokecsv = pokecsv
with open("temp.csv","w", newline="") as f:
    writer = csv.writer(f, delimiter=',')
    for i in temppokecsv:
        writer.writerow(i)

pokecsv.remove(pokecsv[0])

#clears csv file
with open(path+"\Pokemon.csv","w")as f:
    f.write("")
    f.write("#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary\n")

#sorting
for row1 in evocsv:
    for i in row1:
        for row in pokecsv:
            if row[1] == i:

#writing back in evolution order
                with open(path+"\Pokemon.csv","a", newline="") as f:
                    writer = csv.writer(f, delimiter=',')
                    writer.writerow(row)


print("Complete")