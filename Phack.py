
import csv
from tabulate import tabulate
global full_display
full_display = []

class south:
    def __init__(self):
        self.list1 = []
        self.southlist = []
        self.southlistnum = []
        self.southdisplay = []

    def csv_to_list(self):
        with open('stats.csv', newline='') as f:
            self.reader = csv.reader(f)
            self.data_list = list(self.reader)
        
        return self.data_list


    def listofsouthwest(self):
        test = "SOUTH"
        self.res = [idx for idx in self.data_list if idx[0].lower() == test.lower()]
        
        return self.res
    
    def listofsouthwestnum(self):
        for line in self.res:
            a = int(line[1])
            self.southlistnum.append(a)

        
        x = sum(self.southlistnum)
        self.southdisplay.append("SOUTH")
        self.southdisplay.append(x)
    
    def south_display(self):
        
        return self.southdisplay


class southeast():
    def __init__(self):
        self.list1 = []
        self.southeastlist = []
        self.southeastlistnum = []
        self.southeastdisplay = []

    def csv_to_list(self):
        with open('stats.csv', newline='') as f:
            self.reader = csv.reader(f)
            self.data_list = list(self.reader)
        
        return self.data_list


    def listofsouthwest(self):
        test = "SOUTHEAST"
        self.res = [idx for idx in self.data_list if idx[0].lower() == test.lower()]
        
        return self.res
    
    def listofsouthwestnum(self):
        for line in self.res:
            a = int(line[1])
            self.southeastlistnum.append(a)

        
        x = sum(self.southeastlistnum)
        self.southeastdisplay.append("SOUTHEAST")
        self.southeastdisplay.append(x)
    
    def south_display(self):
        
        return self.southeastdisplay


class west():
    def __init__(self):
        self.list1 = []
        self.southwestlist = []
        self.southwestlistnum = []
        self.southwestdisplay = []

    def csv_to_list(self):
        with open('stats.csv', newline='') as f:
            self.reader = csv.reader(f)
            self.data_list = list(self.reader)
        
        return self.data_list


    def listofsouthwest(self):
        test = "WEST"
        self.res = [idx for idx in self.data_list if idx[0].lower() == test.lower()]
        
        return self.res
    
    def listofsouthwestnum(self):
        for line in self.res:
            a = int(line[1])
            self.southwestlistnum.append(a)

        
        x = sum(self.southwestlistnum)
        self.southwestdisplay.append("West")
        self.southwestdisplay.append(x)
    
    def south_display(self):
        
        return self.southwestdisplay

class centre():
    def __init__(self):
        self.list1 = []
        self.centrelist = []
        self.centrelistnum = []
        self.centredisplay = []

    def csv_to_list(self):
        with open('stats.csv', newline='') as f:
            self.reader = csv.reader(f)
            self.data_list = list(self.reader)
        
        return self.data_list


    def listofsouthwest(self):
        test = "CENTRE"
        self.res = [idx for idx in self.data_list if idx[0].lower() == test.lower()]
        
        return self.res
    
    def listofsouthwestnum(self):
        for line in self.res:
            a = int(line[1])
            self.centrelistnum.append(a)

        
        x = sum(self.centrelistnum)
        self.centredisplay.append("CENTRE")
        self.centredisplay.append(x)
    
    def south_display(self):
        
        return self.centredisplay


class east():
    def __init__(self):
        self.list1 = []
        self.eastlist = []
        self.eastlistnum = []
        self.eastdisplay = []

    def csv_to_list(self):
        with open('stats.csv', newline='') as f:
            self.reader = csv.reader(f)
            self.data_list = list(self.reader)
        
        return self.data_list


    def listofsouthwest(self):
        test = "EAST"
        self.res = [idx for idx in self.data_list if idx[0].lower() == test.lower()]
        
        return self.res
    
    def listofsouthwestnum(self):
        for line in self.res:
            a = int(line[1])
            self.eastlistnum.append(a)

        
        x = sum(self.eastlistnum)
        self.eastdisplay.append("EAST")
        self.eastdisplay.append(x)
    
    def south_display(self):
        
        return self.eastdisplay




class north():
    def __init__(self):
        self.list1 = []
        self.northlist = []
        self.northlistnum = []
        self.northdisplay = []

    def csv_to_list(self):
        with open('stats.csv', newline='') as f:
            self.reader = csv.reader(f)
            self.data_list = list(self.reader)
        
        return self.data_list


    def listofsouthwest(self):
        test = "NORTH"
        self.res = [idx for idx in self.data_list if idx[0].lower() == test.lower()]
        
        return self.res
    
    def listofsouthwestnum(self):
        for line in self.res:
            a = int(line[1])
            self.northlistnum.append(a)

        
        x = sum(self.northlistnum)
        self.northdisplay.append("NORTH")
        self.northdisplay.append(x)
    
    def south_display(self):
        
        return self.northdisplay


class northeast():
    def __init__(self):
        self.list1 = []
        self.northeastlist = []
        self.northeastlistnum = []
        self.northeastdisplay = []

    def csv_to_list(self):
        with open('stats.csv', newline='') as f:
            self.reader = csv.reader(f)
            self.data_list = list(self.reader)
        
        return self.data_list


    def listofsouthwest(self):
        test = "NORTHEAST"
        self.res = [idx for idx in self.data_list if idx[0].lower() == test.lower()]
        
        return self.res
    
    def listofsouthwestnum(self):
        for line in self.res:
            a = int(line[1])
            self.northeastlistnum.append(a)

        
        x = sum(self.northeastlistnum)
        self.northeastdisplay.append("NORTHEAST")
        self.northeastdisplay.append(x)
    
    def south_display(self):
        
        return self.northeastdisplay


class northwest():
    def __init__(self):
        self.list1 = []
        self.northwestlist = []
        self.northwestlistnum = []
        self.northwestdisplay = []

    def csv_to_list(self):
        with open('stats.csv', newline='') as f:
            self.reader = csv.reader(f)
            self.data_list = list(self.reader)
        
        return self.data_list


    def listofsouthwest(self):
        test = "NORTHWEST"
        self.res = [idx for idx in self.data_list if idx[0].lower() == test.lower()]
        
        return self.res
    
    def listofsouthwestnum(self):
        for line in self.res:
            a = int(line[1])
            self.northwestlistnum.append(a)

        
        x = sum(self.northwestlistnum)
        self.northwestdisplay.append("NORTHWEST")
        self.northwestdisplay.append(x)
    
    def south_display(self):
    
        return self.northwestdisplay



alex = centre()
alex.csv_to_list()
alex.listofsouthwest()
alex.listofsouthwestnum()
alex.south_display()
full_display.append(alex.south_display())


jhio = east()
jhio.csv_to_list()
jhio.listofsouthwest()
jhio.listofsouthwestnum()
jhio.south_display()
full_display.append(jhio.south_display())


val = north()
val.csv_to_list()
val.listofsouthwest()
val.listofsouthwestnum()
val.south_display()
full_display.append(val.south_display())


gps = northwest()
gps.csv_to_list()
gps.listofsouthwest()
gps.listofsouthwestnum()
gps.south_display()
full_display.append(gps.south_display())

arvie = northeast()
arvie.csv_to_list()
arvie.listofsouthwest()
arvie.listofsouthwestnum()
arvie.south_display()
full_display.append(arvie.south_display())


will = south()
will.csv_to_list()
will.listofsouthwest()
will.listofsouthwestnum()
will.south_display()
full_display.append(will.south_display())

john = southeast()
john.csv_to_list()
john.listofsouthwest()
john.listofsouthwestnum()
john.south_display()
full_display.append(john.south_display())

yuki = west()
yuki.csv_to_list()
yuki.listofsouthwest()
yuki.listofsouthwestnum()
yuki.south_display()
full_display.append(yuki.south_display())


print(tabulate(full_display))