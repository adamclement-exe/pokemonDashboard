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


class csv_loader:

    def __init__(self, file_dir):
        self.file_dir = file_dir

    def read_csv(self):
        r_val = {}
        with open(self.file_dir) as csv_loader:
            csv_reader = csv.reader(csv_loader)
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    data = {
                        "id": int(row[0]),
                        "type1": row[2],
                        "type2": row[3],
                        "total": int(row[4]),
                        "hp": int(row[5]),
                        "attack": int(row[6]),
                        "defence": int(row[7]),
                        "spAtk": int(row[8]),
                        "spDef": int(row[9]),
                        "speed": int(row[10]),
                        "gen": int(row[11]),
                        "legendary": bool(row[12])
                    }
                    r_val[row[1]] = data
                line_count += 1
        return r_val

    def get_pokemon(self, name):
        data = self.read_csv()
        if(name in data):
            return data[name]
        else:
            return 0
