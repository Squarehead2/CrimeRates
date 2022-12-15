import os
import tkinter as tk
from tkinter import simpledialog

# check it out
def regionSelector():
    print("Select a Region you want to choose:")
    print("1 - North West \n2 - North \n3 - North East \n4 - Center \n5 - West \n6 - East \n7 - South \n8 - South East")
    boolean = False
    while boolean == False:

        ROOT = tk.Tk()
        ROOT.withdraw()
        region_selection = simpledialog.askstring(title="Test",
                                        prompt="What's Region Do You Want To Select:")
        if region_selection == "North West":
            region_selection = 1
            boolean = True
        elif region_selection == "North":
            region_selection = 2
            boolean = True
        elif region_selection == "North East":
            region_selection = 3
            boolean = True
        elif region_selection == "Center":
            region_selection = 4
            boolean = True
        elif region_selection == "West":
            region_selection = 5
            boolean = True
        elif region_selection == "East":
            region_selection = 6
            boolean = True
        elif region_selection == "South":
            region_selection = 7
            boolean = True
        elif region_selection == "South East":
            region_selection = 8
            boolean = True
        else:
            print("Please Enter A Valid Inpput!")
        return region_selection


def perCapitaCalculator(crime_type, region_selection):
    file = open("populations.txt", mode="r")
    population_list = []
    for line in file:
        print(line)
        population_list.append(line.replace("\n", ""))
    print(population_list)
    print(int(population_list[region_selection - 1]))
    perCaptia = round(crime_type / int(population_list[region_selection - 1]), 3)
    return perCaptia

region_selection = regionSelector()
crime_type = 1
print(perCapitaCalculator(crime_type, region_selection))
