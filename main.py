import data_utils
import random

firstnamelist = data_utils.readList("materials/Raw materials/Raw_Firstname.txt")
middlenamelist = data_utils.readList("materials/Raw materials/Raw_Middlename.txt")
lastnamelist = data_utils.readList("materials/Raw materials/Raw_Lastname.txt")

birthdaylist = data_utils.readList("materials/Raw materials/Raw_birth_day.txt")
birthmonthlist = data_utils.readList("materials/Raw materials/Raw_birth_month.txt")
birthyearlist = data_utils.readList("materials/Raw materials/Raw_birth_year.txt")

birthcitylist = data_utils.readList("materials/Raw materials/Raw_cities.txt")

universitylist = data_utils.readList("materials/Raw materials/Raw_universities.txt")
majorlist = data_utils.readList("materials/Raw materials/Raw_majors.txt")

employers_and_city_list = data_utils.readList("materials/Raw materials/Raw_employers and company cities.txt")


def get_N_names(N=4):  # this N supposed to be 100000
    combined_names = [f"{first} {middle} {last}" for first in firstnamelist for middle in middlenamelist for last in
                      lastnamelist]
    selected_name_list = random.sample(combined_names, N)
    return selected_name_list


# November 12, 2088
def get_all_birthday_choices():
    birthday_list = [f"{month} {day}, {year}" for month in birthmonthlist for day in birthdaylist for year in
                     birthyearlist]
    return birthday_list


def get_all_birth_city_choices(N=4):  # this N supposed to be 100 ~ len(birthcitylist)
    if N < len(birthcitylist):
        birth_city_list = random.sample(birthcitylist, N)
    else:
        birth_city_list = birthcitylist
    return birth_city_list


def get_all_university_choices(N=4):  # this N supposed to be 100 ~ len(majorlist)
    if N < len(universitylist):
        university_list = random.sample(universitylist, N)
    else:
        university_list = universitylist
    return university_list


def get_all_majors(N=4):  # this N supposed to be 100 ~ len(majorlist)
    if N < len(majorlist):
        major_list = random.sample(majorlist, N)
    else:
        major_list = majorlist
    return major_list


def get_all_employers_and_city_choices(N=4):  # this N supposed to be 100 ~ len(employers_and_city_list)
    if N < len(employers_and_city_list):
        employer_and_city_list = random.sample(employers_and_city_list, N)
    else:
        employer_and_city_list = employers_and_city_list
    return employer_and_city_list

# print(get_all_birthday_choices())
# print(get_all_university_choices())
# print(get_all_majors())
# cities = [
# "New York, NY", "Los Angeles, CA", "Chicago, IL", "Houston, TX", "Phoenix, AZ",
# "Philadelphia, PA", "San Antonio, TX", "San Diego, CA"]

# with open('materials/Raw materials/Raw_cities.txt', 'w') as file:
# for city in cities:
# file.write(city + "\n")
print(get_all_employers_and_city_choices())