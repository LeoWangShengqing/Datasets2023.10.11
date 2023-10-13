import sys

import create_identity
from tqdm import tqdm

personlist = create_identity.create_N_Person()


def generate_QA_dataset():
    print("")
    print("********** generating QA_dataset **********")
    with open("datasets/QA/QA_dataset.txt", "w") as file:
        for person in tqdm(personlist, desc="Processing ", file=sys.stdout):
            for key, value in person.QA.items():
                file.write(f"{key} : {value}\n")
            file.write("\n")
        file.close()


def generate_bioS_single_dataset():
    print("")
    print("********** generating bioS_single_dataset **********")
    with open("datasets/bioS/bioS_single_dataset.txt", "w") as file:
        for person in tqdm(personlist, desc="Processing ", file=sys.stdout):
            file.write(person.bioS_single)
            file.write("\n")
        file.close()


def generate_bioS_single_full_name_dataset():
    print("")
    print("********** generating bioS_single_full_name_dataset **********")
    with open("datasets/bioS/bioS_single_full_name_dataset.txt", "w") as file:
        for person in tqdm(personlist, desc="Processing ", file=sys.stdout):
            file.write(person.bioS_single_fullname)
            file.write("\n")
        file.close()


def generate_bioS_single_permute_1_2_5_dataset():
    print("")
    print("********** generating bioS_single_permute_1_2_5_dataset **********")
    with open("datasets/bioS/bioS_single_permute_1_2_5_dataset", "w") as file:
        for person in tqdm(personlist, desc="Processing ", file=sys.stdout):
            file.write(person.bioS_single_permute_1_2_5)
            file.write("\n")
        file.close()


def generate_bioS_single_permute_1_2_5_fullname_dataset():
    print("")
    print("********** generating bioS_single_permute_1_2_5_fullname_dataset **********")
    with open("datasets/bioS/bioS_single_permute_1_2_5_fullname_dataset", "w") as file:
        for person in tqdm(personlist, desc="Processing ", file=sys.stdout):
            file.write(person.bioS_single_permute_1_2_5_fullname)
            file.write("\n")
        file.close()


def generate_bioS_multi_2_5_dataset():
    print("")
    print("********** generating bioS_multi_2_5_dataset **********")
    with open("datasets/bioS/bioS_multi_2_5_dataset.txt", "w") as file:
        for person in tqdm(personlist, desc="Processing ", file=sys.stdout):
            for line in person.bioS_multi_2_5:
                file.write(line)
                file.write("\n")
            file.write("\n")
        file.close()


def generate_bioS_multi_2_5_permute_dataset():
    print("")
    print("********** generating bioS_multi_2_5_permute_dataset **********")
    with open("datasets/bioS/bioS_multi_2_5_permute_dataset.txt", "w") as file:
        for person in tqdm(personlist, desc="Processing ", file=sys.stdout):
            for line in person.bioS_multi_2_5_permute:
                file.write(line)
                file.write("\n")
            file.write("\n")
        file.close()


def generate_bioS_multi_2_5_fullname_dataset():
    print("")
    print("********** generating bioS_multi_2_5_fullname_dataset **********")
    with open("datasets/bioS/bioS_multi_2_5_fullname_dataset.txt", "w") as file:
        for person in tqdm(personlist, desc="Processing ", file=sys.stdout):
            for line in person.bioS_multi_2_5_fullname:
                file.write(line)
                file.write("\n")
            file.write("\n")
        file.close()


def generate_bioS_multi_2_5_permute_fullname_dataset():
    print("")
    print("********** generating bioS_multi_2_5_permute_fullname_dataset **********")
    with open("datasets/bioS/bioS_multi_2_5_permute_fullname_dataset.txt", "w") as file:
        for person in tqdm(personlist, desc="Processing ", file=sys.stdout):
            for line in person.bioS_multi_2_5_permute_fullname:
                file.write(line)
                file.write("\n")
            file.write("\n")
        file.close()


# generate_bioS_single_dataset()
# generate_bioS_single_permute_1_2_5_dataset()

# generate_bioS_single_permute_1_2_5_fullname_dataset()

# generate_bioS_multi_2_5_dataset()

# generate_bioS_multi_2_5_permute_dataset()
# generate_bioS_multi_2_5_fullname_dataset()

# generate_bioS_multi_2_5_permute_fullname_dataset()


generate_QA_dataset()
generate_bioS_single_dataset()
generate_bioS_single_full_name_dataset()
generate_bioS_single_permute_1_2_5_dataset()
generate_bioS_single_permute_1_2_5_fullname_dataset()
generate_bioS_multi_2_5_dataset()
generate_bioS_multi_2_5_permute_dataset()
generate_bioS_multi_2_5_fullname_dataset()
generate_bioS_multi_2_5_permute_fullname_dataset()
