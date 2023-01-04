import csv
from menu import admin, pupil, teacher
from inputs import pass



def print_menu(user_type):
    if user_type == 1:
        return admin
    elif user_type == 2:
        return pupil
    elif user_type == 3:
        return teacher

def print_array(array, user, user_type):
    with open(source_path, 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';', skipinitialspace=False)
        info = []
        for row in file_reader:
            if user in row:
                info.append(row)
    return info



def print_aray_search(array, search_string):
    with open(source_path, 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';', skipinitialspace=False)
        info = []
        for row in file_reader:
            if search_string in row:
                info.append(row)
    return info