import csv

class CrimeTypes:
    def __init__(self):
        self.csv_to_list()

    def csv_to_list(self):
        self.file = open('Community_Crime_Statistics.csv', newline='')
        self.reader = csv.reader(self.file)
        crimelist = []
        for line in self.reader:
            crimes = line[2]
            c = crimes.split(" ")
            crimelist.append(c)
        crimetup = [tuple(x) for x in crimelist]
        crimedict = list(dict.fromkeys(crimetup))
        self.duple = [list(x) for x in crimedict]

    def displayCrimesList(self):
        for line in self.duple:
            print(str(line))
