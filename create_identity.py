import random
import sys

from get_all_info import get_all_info
from genaerate_bioS import bioS_data
from tqdm import tqdm

get_all_info = get_all_info()
all_name_choices = get_all_info.get_N_names()
all_birthday_choices = get_all_info.get_all_birthday_choices()
all_birth_city_choices = get_all_info.get_all_birth_city_choices()
all_university_choices = get_all_info.get_all_university_choices()
all_major_choices = get_all_info.get_all_major_choices()
all_employer_city_choices = get_all_info.get_all_employer_and_city_choices()


class Person:
    def __init__(self, id):
        self.id = id
        self.name = all_name_choices[self.id]
        self.pronoun = random.choice(["he", "she", "they"])
        self.birthday = random.choice(all_birthday_choices)
        self.birth_city = random.choice(all_birth_city_choices)
        self.univerity = random.choice(all_university_choices)
        self.major = random.choice(all_major_choices)
        (employer, company_city) = random.choice(all_employer_city_choices)
        self.employer = employer
        self.company_city = company_city
        self.bioS_single = ""
        self.bioS_single_fullname = ""
        self.bioS_single_permute_1_2_5 = ""
        self.bioS_single_permute_1_2_5_fullname = ""
        self.bioS_multi_2_5 = []
        self.bioS_multi_2_5_permute = []
        self.bioS_multi_2_5_fullname = []
        self.bioS_multi_2_5_permute_fullname = []
        self.QA = {
            "What is the birth date of " + self.name + "?": self.birthday,
            "What is the birth city of " + self.name + "?": self.birth_city,
            "Which university did " + self.name + " study?": self.univerity,
            "What major did " + self.name + " study?": self.major,
            "Which company did " + self.name + " work for?": self.employer,
            "Where did " + self.name + " work?": self.company_city
        }


# p = Person(2)

# with open("1person_info.txt", "w") as file:
# for key, value in p.QA.items():
# file.write(f"{key} : {value}\n")

def create_N_Person():
    print(" ")
    print("---------- Create information for", str(len(all_name_choices)), "individuals ----------")
    personlist = []
    for i in tqdm(range(len(all_name_choices)), desc="Processing ", file=sys.stdout):
        p = Person(i)
        pb = bioS_data(p)
        p.bioS_single = pb.bioS_sentences("bioS single")
        p.bioS_single_fullname = pb.bioS_sentences("bioS single full name")
        p.bioS_single_permute_1_2_5 = pb.bioS_sentences("bioS single permute1/2/5")
        p.bioS_single_permute_1_2_5_fullname = pb.bioS_sentences("bioS single permute1/2/5 fullname")
        p.bioS_multi_2_5 = pb.bioS_sentences("bioS multi2/5")
        p.bioS_multi_2_5_permute = pb.bioS_sentences("bioS multi2/5 permute")
        p.bioS_multi_2_5_fullname = pb.bioS_sentences("bioS multi2/5 fullname")
        p.bioS_multi_2_5_permute_fullname = pb.bioS_sentences("bioS multi2/5 permute fullname")
        personlist.append(p)
    print("------------------------------------------------------------")
    return personlist
