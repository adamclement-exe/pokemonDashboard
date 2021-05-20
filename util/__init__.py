
"""
:author Madmegsox1
"""
import csv


class file_loader:
    def __init__(self, file_dir):
        self.file_dir = file_dir

    def read(self):
        f = open(self.file_dir, "r")
        return f.read()

    def write(self, text):
        f = open(self.file_dir, "w")
        f.write(text)
        f.close()

    def append(self, text):
        f = open(self.file_dir, "a")
        f.write(text)
        f.close()


def get_pokemon_by_category_opp(category, name, data):
    r_val = []
    for i in data:
        if category not in data[i]:
            return 0
        if data[i][category] == name:
            r_val.append(i)
    if len(r_val) == 0:
        return 0
    return r_val


class csv_loader:

    def __init__(self, file_dir):
        self.file_dir = file_dir
        self.data = self.read_csv()

    def read_csv(self):
        r_val = {}
        with open(self.file_dir) as csv_loader:
            csv_reader = csv.reader(csv_loader)
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    leg = False
                    if row[12] == "True":
                        leg = True

                    data = {
                        "id": int(row[0]),
                        "name": row[1],
                        "type1": row[2],
                        "type2": row[3],
                        "Total": int(row[4]),
                        "HP": int(row[5]),
                        "Attack": int(row[6]),
                        "Defence": int(row[7]),
                        "Sp. Atk": int(row[8]),
                        "Sp. Def": int(row[9]),
                        "Speed": int(row[10]),
                        "Generation": int(row[11]),
                        "Legendary": leg
                    }
                    r_val[row[1]] = data
                line_count += 1
        return r_val

    def get_pokemon_by_name(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return 0

    def get_pokemon_by_char(self, name):
        r_val = []
        for names in self.data:
            if name.lower() in names.lower():
                r_val.append(self.data[names])
        if len(r_val) == 0:
            return 0
        else:
            return r_val

    def get_pokemon_by_category(self, category, name):
        r_val = []
        for i in self.data:
            if category not in self.data[i]:
                return 0
            if self.data[i][category] == name:
                r_val.append(i)
        if len(r_val) == 0:
            return 0
        return r_val

    def sort(self, category, high_to_low):
        r_val = []
        sort = []
        pok = []
        for i in self.data:
            if category not in self.data[i]:
                return 0
            r_val.append(self.data[i])

        for x in r_val:
            sort.append(x[category])
        sort.sort(reverse=high_to_low)

        for y in sort:
            v = get_pokemon_by_category_opp(category, y, self.data)
            for a in v:
                if a in pok:
                    continue
                pok.append(a)

        return pok

    def refactor_list(self, list, category, name):
        r_val = []
        for i in list:
            p_data = self.get_pokemon_by_name(i)
            if (p_data != 0) and (category in p_data):
                if p_data[category] == name:
                    r_val.append(i)

        if len(r_val) == 0:
            return 0
        return r_val


class search:
    def __init__(self):
        self.instance = csv_loader("Pokemon.csv")

    def getList(self, sort, hTl, list):

        #  ( code to make Alphabetical sorts possible )
        if sort == "Alphabetical":
            Alpha = sort
            sort = "id"
        else:
            Alpha = None
        #  ( code to make Alphabetical sorts possible )

        r_val = self.instance.sort(sort, hTl)

        type_list = ["type1", "type2", "Generation", "Legendary"]
        for i in range(len(list)):
            if (list[i] == "All") or (list[i] is None): continue
            if r_val == 0:
                return 0
            r_val = self.instance.refactor_list(r_val, type_list[i], list[i])

            #  ( code to make Alphabetical sorts possible )
            if Alpha == "Alphabetical":
                r_val = sorted(r_val, reverse=not hTl)
            #  ( code to make Alphabetical sorts possible )

        return r_val
        # ------------HOW TO CONSTRUCT------------#
        #   The Pram "list" must be in the same
        #   sequence as type_list e.g.
        #   index1 -> type1
        #   index2 -> type2
        #   index3 -> Generation
        #   index4 -> Legendary
        #   if the search is null it returns None
