import create_identity

personlist = create_identity.create_N_Person()


def generate_QA_dataset():
    with open("datasets/QA/QA_dataset.txt", "w") as file:
        for person in personlist:
            for key, value in person.QA.items():
                file.write(f"{key} : {value}\n")
            file.write("\n")
        file.close()


#generate_QA_dataset()