"""
:author Squidnugi
"""
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
                row[0] = int(row[0])
                loop = 4
                while loop <= 11:
                    row[loop] = int(row[loop])
                    loop+=1
                #changes legandary True and Flase to bool from string
                row[12] = False
                if row[12] == 'True':
                    row[12] = True
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


def pokedex_picker(pokemon,choice):
    #gen picker
    if choice == 'Gen':
        List = []
        gen = 2
        for i in pokemon:
            if i[11] == gen:
                List.append(i)
        return List
    #type picker
    elif choice == 'Type':
        List = []
        type = 'Fire'
        for i in pokemon:
            if i[3] == type or i[4] == type:
                List.append(i)
                return List
    #Legendary picker
    elif choice == 'Legendary':
        List = []
        leg = True
        for i in pokemon:
            if i[12] == leg:
                List.append(i)
        return List
    #number picker
    elif choice == 'Num':
        List = []
        num = 100
        for i in pokemon:
            if i[0] == num:
                List.append(i)
        return List
    #name picker
    elif choice == 'Name':
        List = []
        name = 'Blastoise'
        for i in pokemon:
            if i[1] == name:
                List.append(i)
        return List

def name_filter(pokemon):
    loops = 1
    for i in pokemon:
        if i[0] == loops:
            print(i)
            loops+=1

def main():
    file = 'pokemon.csv'
    pokemon = file_reader(file,False)
    types = file_reader(file,True)
    print(pokemon)
    print(types)
    gen = pokedex_picker(pokemon,'Gen')
    print(gen)
    name_filter(pokemon)


if __name__ == "__main__":
    main()
