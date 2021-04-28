import csv


def file_reader(file,choice):
    list_of_stuff = []
    types = []
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            #makes sure the first line is not read
            if '#' not in row:
                #changes the number valuse to int from string
                loop = 4
                while loop <= 11:
                    row[loop] = int(row[loop])
                    loop+=1
                #changes legandary True and Flase to bool from string
                if row[12] == 'True':
                    row[12] = True
                elif row[12] == 'False':
                    row[12] = False
                list_of_stuff.append(row)
                #creates a list of the pokemon types
                if row[2] not in types:
                    types.append(row[2])
    #returns the pokedex if False
    if choice == False:
        return list_of_stuff
    #returns the type list of True
    elif choice == True:
        return types


def pokedex_filter(pokemon,types,choice):
    #gen filter
    if choice == 'Gen':
        List = []
        gen = 2
        for i in pokemon:
            if i[11] == gen:
                List.append(i)
        return List
    #type filter
    elif choice == 'Type':
        List = []
        type = 'Fire'
        for i in pokemon:
            if i[3] == type or i[4] == type:
                List.append(i)
                return List
    #Legendary filter
    elif choice == 'Legendary':
        List = []
        leg = True
        for i in pokemon:
            if i[12] == leg:
                List.append(i)
        return List
    #number filter
    elif choice == 'Num':
        List = []
        num = 100
        for i in pokemon:
            if i[0] == num:
                List.append(i)
        return List
    #name filter
    elif choice == 'Name':
        List = []
        name = 'Blastoise'
        for i in pokemon:
            if i[1] == name:
                List.append(i)
        return List


def main():
    file = 'pokemon.csv'
    pokemon = file_reader(file,False)
    types = file_reader(file,True)
    print(pokemon)
    print(types)
    gen = pokedex_filter(pokemon,types,'Name')
    print(gen)


if __name__ == "__main__":
    main()
