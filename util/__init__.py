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
                        "total": int(row[4]),
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
        print(list)
        for i in list:
            p_data = self.get_pokemon_by_name(i)
            if (p_data != 0) and (category in p_data):
                if p_data[category] == name:
                    r_val.append(i)

        if len(r_val) == 0:
            return 0
        return r_val
