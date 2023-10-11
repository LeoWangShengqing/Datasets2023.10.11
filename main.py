import torch
import data_utils
from data_utils import *

firstnamelist = data_utils.readList("materials/Raw materials/Raw_Firstname.txt")
middlenamelist = data_utils.readList("materials/Raw materials/Raw_Middlename.txt")
lastnamelist = data_utils.readList("materials/Raw materials/Raw_Lastname.txt")

# print(firstnamelist)
combined_names = [f"{first} {middle} {last}" for first in firstnamelist for middle in middlenamelist for last in
                  lastnamelist]
print(len(combined_names))
print(combined_names)
