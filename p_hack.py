import csv

def school_csv_to_list():
    with open('School_Locations.csv', newline='') as f:
        reader = csv.reader(f)
        school_data_list = list(reader)
    return school_data_list

def compare_area(school_data_list):
    school_in_center = 0
    for i in range(1,len(school_data_list)):
        postal_code = school_data_list[i][6]
        postal_code_3 = postal_code[:3]
        if(postal_code_3 == "T2P"):
            school_in_center += 1
        else:
            pass
    print(school_in_center)
    return school_in_center

             