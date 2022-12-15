def addLocation():
    with open("locations.txt", 'a') as file:
        sector = input("Please Enter the Sector of the Communnity:\n\n")
        community = input("Please Enter the name of the new community:\n\n")
        format  = (f"\n{sector}_{community}")
        file.write(format)

def editLocation():
    with open("locations.txt", 'r+') as file:
        for line in file:
            a = line.split("_")
            a[1] = input("Please enter the new name of the Community:\n\n r")
            print(a)