import data_utils
import random

firstnamelist = data_utils.readList("materials/Raw materials/Raw_Firstname.txt")
middlenamelist = data_utils.readList("materials/Raw materials/Raw_Middlename.txt")
lastnamelist = data_utils.readList("materials/Raw materials/Raw_Lastname.txt")


def get_N_names(N):
    combined_names = [f"{first} {middle} {last}" for first in firstnamelist for middle in middlenamelist for last in
                      lastnamelist]
    selected_name_list = random.sample(combined_names, N)  # supposed to be 100000
    return selected_name_list






print(get_N_names(4))
