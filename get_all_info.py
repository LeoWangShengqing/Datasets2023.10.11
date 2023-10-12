import data_utils
import random


class get_all_info:
    def __init__(self):
        self.firstnamelist = data_utils.readList("materials/Raw materials/Raw_Firstname.txt")
        self.middlenamelist = data_utils.readList("materials/Raw materials/Raw_Middlename.txt")
        self.lastnamelist = data_utils.readList("materials/Raw materials/Raw_Lastname.txt")

        self.birthdaylist = data_utils.readList("materials/Raw materials/Raw_birth_day.txt")
        self.birthmonthlist = data_utils.readList("materials/Raw materials/Raw_birth_month.txt")
        self.birthyearlist = data_utils.readList("materials/Raw materials/Raw_birth_year.txt")

        self.birthcitylist = data_utils.readList("materials/Raw materials/Raw_cities.txt")

        self.universitylist = data_utils.readList("materials/Raw materials/Raw_universities.txt")
        self.majorlist = data_utils.readList("materials/Raw materials/Raw_majors.txt")

        # self.employers_and_city_list = data_utils.readList(
        # "materials/Raw materials/Raw_employers and company cities.txt")
        self.employers_and_city_list = [item.split(" - ") for item in data_utils.readList(
            "materials/Raw materials/Raw_employers and company cities.txt")]

        self.Sample_size_people = int(input("----Please input Sample size for people (5):"))
        self.Sample_size_birth_city = int(input("----Please input Sample size for birth city (100~1000) :"))
        self.Sample_size_university = int(input("----Please input Sample size for university (100~1000) :"))
        self.Sample_size_major = int(input("----Please input Sample size for major (100~1000) :"))
        self.Sample_size_employer_company_city = int(input("----Please input Sample size for employer (100~1000) :"))

    def get_N_names(self):  # this N supposed to be 100000
        combined_names = [f"{first} {middle} {last}" for first in self.firstnamelist for middle in self.middlenamelist
                          for last in
                          self.lastnamelist]
        selected_name_list = random.sample(combined_names, self.Sample_size_people)
        random.shuffle(selected_name_list)
        return selected_name_list

    def get_all_birthday_choices(self):
        birthday_list = [f"{month} {day}, {year}" for month in self.birthmonthlist for day in self.birthdaylist for year
                         in self.birthyearlist]
        return birthday_list

    def get_all_birth_city_choices(self):  # this N supposed to be 100 ~ len(birthcitylist)
        if self.Sample_size_birth_city < len(self.birthcitylist):
            birth_city_list = random.sample(self.birthcitylist, self.Sample_size_birth_city)
        else:
            birth_city_list = self.birthcitylist
        return birth_city_list

    def get_all_university_choices(self):  # this N supposed to be 100 ~ len(universitylist)
        if self.Sample_size_university < len(self.universitylist):
            university_list = random.sample(self.universitylist, self.Sample_size_university)
        else:
            university_list = self.universitylist
        return university_list

    def get_all_major_choices(self):  # this N supposed to be 100 ~ len(majorlist)
        if self.Sample_size_major < len(self.majorlist):
            major_list = random.sample(self.majorlist, self.Sample_size_major)
        else:
            major_list = self.majorlist
        return major_list

    def get_all_employer_and_city_choices(self):  # this N supposed to be 100 ~ len(employers_and_city_list)
        if self.Sample_size_employer_company_city < len(self.employers_and_city_list):
            employer_and_city_list = random.sample(self.employers_and_city_list, self.Sample_size_employer_company_city)
        else:
            employer_and_city_list = self.employers_and_city_list
        return employer_and_city_list
