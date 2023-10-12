import random
import data_utils

template_birth_date_sentences = data_utils.readList(
    "materials/Raw materials/Raw_bioS_materials/Raw_templates_birth dates.txt")
template_birth_city_sentences = data_utils.readList("materials/Raw materials/Raw_bioS_materials/Raw_templates_birth "
                                                    "cities.txt")
template_university_sentences = data_utils.readList("materials/Raw materials/Raw_bioS_materials"
                                                    "/Raw_templates_university.txt")
template_major_sentences = data_utils.readList("materials/Raw materials/Raw_bioS_materials/Raw_templates_major.txt")
template_employer_sentences = data_utils.readList("materials/Raw materials/Raw_bioS_materials/Raw_templates_employer"
                                                  ".txt")
template_company_city_sentences = data_utils.readList("materials/Raw materials/Raw_bioS_materials"
                                                      "/Raw_templates_company cities.txt")


class get_raw_sentences:
    def __init__(self):
        pass

    def sentence_birth_date(self):
        Sentence = random.choice(template_birth_date_sentences)
        return Sentence

    def sentence_birth_city(self):
        Sentence = random.choice(template_birth_city_sentences)
        return Sentence

    def sentence_university(self):
        Sentence = random.choice(template_university_sentences)
        return Sentence

    def sentence_major(self):
        Sentence = random.choice(template_major_sentences)
        return Sentence

    def sentence_employer(self):
        Sentence = random.choice(template_employer_sentences)
        return Sentence

    def sentence_company_city(self):
        Sentence = random.choice(template_company_city_sentences)
        return Sentence

    def sentence_birth_date_for_2_or_5(self, num):
        Sentences = random.sample(template_birth_date_sentences, num)
        return Sentences

    def sentence_birth_city_for_2_or_5(self, num):
        Sentences = random.sample(template_birth_city_sentences, num)
        return Sentences

    def sentence_university_for_2_or_5(self, num):
        Sentences = random.sample(template_university_sentences, num)
        return Sentences

    def sentence_major_for_2_or_5(self, num):
        Sentences = random.sample(template_major_sentences, num)
        return Sentences

    def sentence_employer_for_2_for_5(self, num):
        Sentences = random.sample(template_employer_sentences, num)
        return Sentences

    def sentence_company_city_for_2_or_5(self, num):
        Sentences = random.sample(template_company_city_sentences, num)
        return Sentences


class bioS_data:
    def __init__(self, p):

        self.pronoun = p.pronoun
        if self.pronoun == "he":
            self.subj_pronoun = "he"
            self.obj_pronoun = "him"
            self.pos_pronoun = "his"
            self.be_present = "is"
            self.be_past = "was"
        elif self.pronoun == "she":
            self.subj_pronoun = "she"
            self.obj_pronoun = "her"
            self.pos_pronoun = "her"
            self.be_present = "is"
            self.be_past = "was"
        elif self.pronoun == "they":
            self.subj_pronoun = "they"
            self.obj_pronoun = "them"
            self.pos_pronoun = "their"
            self.be_present = "are"
            self.be_past = "were"

        self.fullName = p.name
        self.birthDate = p.birthday
        self.birthCity = p.birth_city
        self.university = p.univerity
        self.major = p.major
        self.employer = p.employer
        self.companyCity = p.company_city

        self.temp = get_raw_sentences()
        self.sentence_1 = self.temp.sentence_birth_date()
        self.sentence_2 = self.temp.sentence_birth_city()
        self.sentence_3 = self.temp.sentence_university()
        self.sentence_4 = self.temp.sentence_major()
        self.sentence_5 = self.temp.sentence_employer()
        self.sentence_6 = self.temp.sentence_company_city()

        self.sentencelist = []
        self.sentencelist.append(self.sentence_1)
        self.sentencelist.append(self.sentence_2)
        self.sentencelist.append(self.sentence_3)
        self.sentencelist.append(self.sentence_4)
        self.sentencelist.append(self.sentence_5)
        self.sentencelist.append(self.sentence_6)

    def bioS_sentences(self, datatype=""):
        resultSentences = ""

        if datatype == "bioS single":
            sentence_1 = data_utils.capitalize_first(
                self.sentence_1.replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(birthday)",
                                                                                                self.birthDate))

            sentence_2 = data_utils.capitalize_first(
                self.sentence_2.replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                     self.obj_pronoun).replace(
                    "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                        self.be_past).replace(
                    "(birth_city)", self.birthCity))

            sentence_3 = data_utils.capitalize_first(
                self.sentence_3.replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                     self.obj_pronoun).replace(
                    "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                        self.be_past).replace(
                    "(university)", self.university))

            sentence_4 = data_utils.capitalize_first(
                self.sentence_4.replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                     self.obj_pronoun).replace(
                    "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                        self.be_past).replace(
                    "(major)", self.major))

            sentence_5 = data_utils.capitalize_first(
                self.sentence_5.replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                     self.obj_pronoun).replace(
                    "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                        self.be_past).replace(
                    "(employer)", self.employer))

            sentence_6 = data_utils.capitalize_first(
                self.sentence_6.replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                     self.obj_pronoun).replace(
                    "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                        self.be_past).replace(
                    "(company_city)", self.companyCity))

            resultSentences = sentence_1 + " " + sentence_2 + " " + sentence_3 + " " + sentence_4 + " " + sentence_5 + " " + sentence_6

            return resultSentences

        elif datatype == "bioS single full name":
            sentence_1 = data_utils.capitalize_first(
                self.sentence_1.replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(birthday)",
                                                                                                self.birthDate))

            sentence_2 = data_utils.capitalize_first(
                self.sentence_2.replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(birth_city)",
                                                                                                self.birthCity))

            sentence_3 = data_utils.capitalize_first(
                self.sentence_3.replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(university)",
                                                                                                self.university))

            sentence_4 = data_utils.capitalize_first(
                self.sentence_4.replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(major)", self.major))

            sentence_5 = data_utils.capitalize_first(
                self.sentence_5.replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(employer)",
                                                                                                self.employer))

            sentence_6 = data_utils.capitalize_first(
                self.sentence_6.replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(company_city)",
                                                                                                self.companyCity))

            resultSentences = sentence_1 + " " + sentence_2 + " " + sentence_3 + " " + sentence_4 + " " + sentence_5 + " " + sentence_6

            return resultSentences

        elif datatype == "bioS single permute1/2/5":
            permuteNum = random.choice([1, 2, 5])
            sentencelist = self.sentencelist

            for i in range(permuteNum):
                random.shuffle(sentencelist)

            sentence_1 = data_utils.capitalize_first(
                sentencelist[0].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(birthday)",
                                                                                                self.birthDate).replace(
                    "(birth_city)", self.birthCity).replace("(university)", self.university).replace("(major)",
                                                                                                     self.major).replace(
                    "(employer)", self.employer).replace("(company_city)", self.companyCity))
            sentence_2 = data_utils.capitalize_first(
                sentencelist[1].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                     self.obj_pronoun).replace(
                    "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                        self.be_past).replace(
                    "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                  self.university).replace(
                    "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                        self.companyCity))
            sentence_3 = data_utils.capitalize_first(
                sentencelist[2].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                     self.obj_pronoun).replace(
                    "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                        self.be_past).replace(
                    "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                  self.university).replace(
                    "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                        self.companyCity))
            sentence_4 = data_utils.capitalize_first(
                sentencelist[3].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                     self.obj_pronoun).replace(
                    "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                        self.be_past).replace(
                    "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                  self.university).replace(
                    "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                        self.companyCity))
            sentence_5 = data_utils.capitalize_first(
                sentencelist[4].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                     self.obj_pronoun).replace(
                    "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                        self.be_past).replace(
                    "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                  self.university).replace(
                    "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                        self.companyCity))
            sentence_6 = data_utils.capitalize_first(
                sentencelist[5].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                     self.obj_pronoun).replace(
                    "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                        self.be_past).replace(
                    "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                  self.university).replace(
                    "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                        self.companyCity))

            resultSentences = sentence_1 + " " + sentence_2 + " " + sentence_3 + " " + sentence_4 + " " + sentence_5 + " " + sentence_6

            return resultSentences

        elif datatype == "bioS single permute1/2/5 fullname":
            permuteNum = random.choice([1, 2, 5])
            sentencelist = self.sentencelist

            for i in range(permuteNum):
                random.shuffle(sentencelist)

            sentence_1 = data_utils.capitalize_first(
                sentencelist[0].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(birthday)",
                                                                                                self.birthDate).replace(
                    "(birth_city)", self.birthCity).replace("(university)", self.university).replace("(major)",
                                                                                                     self.major).replace(
                    "(employer)", self.employer).replace("(company_city)", self.companyCity))
            sentence_2 = data_utils.capitalize_first(
                sentencelist[1].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(birthday)",
                                                                                                self.birthDate).replace(
                    "(birth_city)", self.birthCity).replace("(university)", self.university).replace("(major)",
                                                                                                     self.major).replace(
                    "(employer)", self.employer).replace("(company_city)", self.companyCity))
            sentence_3 = data_utils.capitalize_first(
                sentencelist[2].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(birthday)",
                                                                                                self.birthDate).replace(
                    "(birth_city)", self.birthCity).replace("(university)", self.university).replace("(major)",
                                                                                                     self.major).replace(
                    "(employer)", self.employer).replace("(company_city)", self.companyCity))
            sentence_4 = data_utils.capitalize_first(
                sentencelist[3].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(birthday)",
                                                                                                self.birthDate).replace(
                    "(birth_city)", self.birthCity).replace("(university)", self.university).replace("(major)",
                                                                                                     self.major).replace(
                    "(employer)", self.employer).replace("(company_city)", self.companyCity))
            sentence_5 = data_utils.capitalize_first(
                sentencelist[4].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(birthday)",
                                                                                                self.birthDate).replace(
                    "(birth_city)", self.birthCity).replace("(university)", self.university).replace("(major)",
                                                                                                     self.major).replace(
                    "(employer)", self.employer).replace("(company_city)", self.companyCity))
            sentence_6 = data_utils.capitalize_first(
                sentencelist[5].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                 self.fullName).replace("(pos_pronoun)",
                                                                                                        self.fullName).replace(
                    "(be_present)", self.be_present).replace("(be_past)", self.be_past).replace("(birthday)",
                                                                                                self.birthDate).replace(
                    "(birth_city)", self.birthCity).replace("(university)", self.university).replace("(major)",
                                                                                                     self.major).replace(
                    "(employer)", self.employer).replace("(company_city)", self.companyCity))

            resultSentences = sentence_1 + " " + sentence_2 + " " + sentence_3 + " " + sentence_4 + " " + sentence_5 + " " + sentence_6
            return resultSentences

        elif datatype == "bioS multi2/5":
            resultSentenceslist = []

            entriesNum = random.choice([2, 5])

            sentence_1_list = self.temp.sentence_birth_date_for_2_or_5(entriesNum)
            sentence_2_list = self.temp.sentence_birth_city_for_2_or_5(entriesNum)
            sentence_3_list = self.temp.sentence_university_for_2_or_5(entriesNum)
            sentence_4_list = self.temp.sentence_major_for_2_or_5(entriesNum)
            sentence_5_list = self.temp.sentence_employer_for_2_for_5(entriesNum)
            sentence_6_list = self.temp.sentence_company_city_for_2_or_5(entriesNum)

            for i in range(entriesNum):
                sentence_1 = data_utils.capitalize_first(
                    sentence_1_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                        self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                         self.be_past).replace(
                        "(birthday)", self.birthDate))
                sentence_2 = data_utils.capitalize_first(
                    sentence_2_list[i].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                            self.obj_pronoun).replace(
                        "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(birth_city)", self.birthCity))
                sentence_3 = data_utils.capitalize_first(
                    sentence_3_list[i].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                            self.obj_pronoun).replace(
                        "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(university)", self.university))
                sentence_4 = data_utils.capitalize_first(
                    sentence_4_list[i].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                            self.obj_pronoun).replace(
                        "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(major)", self.major))
                sentence_5 = data_utils.capitalize_first(
                    sentence_5_list[i].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                            self.obj_pronoun).replace(
                        "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(employer)", self.employer))
                sentence_6 = data_utils.capitalize_first(
                    sentence_6_list[i].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                            self.obj_pronoun).replace(
                        "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(company_city)", self.companyCity))

                resultSentences = sentence_1 + " " + sentence_2 + " " + sentence_3 + " " + sentence_4 + " " + sentence_5 + " " + sentence_6
                resultSentenceslist.append(resultSentences)

            return resultSentenceslist

        elif datatype == "bioS multi2/5 permute":
            resultSentenceslist = []

            entriesNum = random.choice([2, 5])

            sentenseslist = []
            sentence_1_list = self.temp.sentence_birth_date_for_2_or_5(entriesNum)
            sentence_2_list = self.temp.sentence_birth_city_for_2_or_5(entriesNum)
            sentence_3_list = self.temp.sentence_university_for_2_or_5(entriesNum)
            sentence_4_list = self.temp.sentence_major_for_2_or_5(entriesNum)
            sentence_5_list = self.temp.sentence_employer_for_2_for_5(entriesNum)
            sentence_6_list = self.temp.sentence_company_city_for_2_or_5(entriesNum)

            sentenseslist.append(sentence_1_list)
            sentenseslist.append(sentence_2_list)
            sentenseslist.append(sentence_3_list)
            sentenseslist.append(sentence_4_list)
            sentenseslist.append(sentence_5_list)
            sentenseslist.append(sentence_6_list)

            for i in range(entriesNum):
                index = [0, 1, 2, 3, 4, 5]
                random.shuffle(index)
                sentence_1_list = sentenseslist[index[0]]
                sentence_2_list = sentenseslist[index[1]]
                sentence_3_list = sentenseslist[index[2]]
                sentence_4_list = sentenseslist[index[3]]
                sentence_5_list = sentenseslist[index[4]]
                sentence_6_list = sentenseslist[index[5]]

                sentence_1 = data_utils.capitalize_first(
                    sentence_1_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                        self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                         self.be_past).replace(
                        "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                      self.university).replace(
                        "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                            self.companyCity))
                sentence_2 = data_utils.capitalize_first(
                    sentence_2_list[i].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                            self.obj_pronoun).replace(
                        "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                      self.university).replace(
                        "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                            self.companyCity))
                sentence_3 = data_utils.capitalize_first(
                    sentence_3_list[i].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                            self.obj_pronoun).replace(
                        "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                      self.university).replace(
                        "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                            self.companyCity))
                sentence_4 = data_utils.capitalize_first(
                    sentence_4_list[i].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                            self.obj_pronoun).replace(
                        "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                      self.university).replace(
                        "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                            self.companyCity))
                sentence_5 = data_utils.capitalize_first(
                    sentence_5_list[i].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                            self.obj_pronoun).replace(
                        "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                      self.university).replace(
                        "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                            self.companyCity))
                sentence_6 = data_utils.capitalize_first(
                    sentence_6_list[i].replace("(subj_pronoun)", self.subj_pronoun).replace("(obj_pronoun)",
                                                                                            self.obj_pronoun).replace(
                        "(pos_pronoun)", self.pos_pronoun).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                      self.university).replace(
                        "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                            self.companyCity))

                resultSentences = sentence_1 + " " + sentence_2 + " " + sentence_3 + " " + sentence_4 + " " + sentence_5 + " " + sentence_6
                resultSentenceslist.append(resultSentences)

            return resultSentenceslist
        elif datatype == "bioS multi2/5 fullname":
            resultSentenceslist = []

            entriesNum = random.choice([2, 5])

            sentence_1_list = self.temp.sentence_birth_date_for_2_or_5(entriesNum)
            sentence_2_list = self.temp.sentence_birth_city_for_2_or_5(entriesNum)
            sentence_3_list = self.temp.sentence_university_for_2_or_5(entriesNum)
            sentence_4_list = self.temp.sentence_major_for_2_or_5(entriesNum)
            sentence_5_list = self.temp.sentence_employer_for_2_for_5(entriesNum)
            sentence_6_list = self.temp.sentence_company_city_for_2_or_5(entriesNum)

            for i in range(entriesNum):
                sentence_1 = data_utils.capitalize_first(
                    sentence_1_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                        self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                         self.be_past).replace(
                        "(birthday)", self.birthDate))
                sentence_2 = data_utils.capitalize_first(
                    sentence_2_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                            self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(birth_city)", self.birthCity))
                sentence_3 = data_utils.capitalize_first(
                    sentence_3_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                            self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(university)", self.university))
                sentence_4 = data_utils.capitalize_first(
                    sentence_4_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                            self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(major)", self.major))
                sentence_5 = data_utils.capitalize_first(
                    sentence_5_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                            self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(employer)", self.employer))
                sentence_6 = data_utils.capitalize_first(
                    sentence_6_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                            self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                            self.be_past).replace(
                        "(company_city)", self.companyCity))

                resultSentences = sentence_1 + " " + sentence_2 + " " + sentence_3 + " " + sentence_4 + " " + sentence_5 + " " + sentence_6
                resultSentenceslist.append(resultSentences)

            return resultSentenceslist


        elif datatype == "bioS multi2/5 permute fullname":
            resultSentenceslist = []

            entriesNum = random.choice([2, 5])

            sentenseslist = []
            sentence_1_list = self.temp.sentence_birth_date_for_2_or_5(entriesNum)
            sentence_2_list = self.temp.sentence_birth_city_for_2_or_5(entriesNum)
            sentence_3_list = self.temp.sentence_university_for_2_or_5(entriesNum)
            sentence_4_list = self.temp.sentence_major_for_2_or_5(entriesNum)
            sentence_5_list = self.temp.sentence_employer_for_2_for_5(entriesNum)
            sentence_6_list = self.temp.sentence_company_city_for_2_or_5(entriesNum)

            sentenseslist.append(sentence_1_list)
            sentenseslist.append(sentence_2_list)
            sentenseslist.append(sentence_3_list)
            sentenseslist.append(sentence_4_list)
            sentenseslist.append(sentence_5_list)
            sentenseslist.append(sentence_6_list)

            for i in range(entriesNum):
                index = [0, 1, 2, 3, 4, 5]
                random.shuffle(index)
                sentence_1_list = sentenseslist[index[0]]
                sentence_2_list = sentenseslist[index[1]]
                sentence_3_list = sentenseslist[index[2]]
                sentence_4_list = sentenseslist[index[3]]
                sentence_5_list = sentenseslist[index[4]]
                sentence_6_list = sentenseslist[index[5]]

                sentence_1 = data_utils.capitalize_first(
                    sentence_1_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                        self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                         self.be_past).replace(
                        "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                      self.university).replace(
                        "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                            self.companyCity))
                sentence_2 = data_utils.capitalize_first(
                    sentence_2_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                        self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                         self.be_past).replace(
                        "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                      self.university).replace(
                        "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                            self.companyCity))
                sentence_3 = data_utils.capitalize_first(
                    sentence_3_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                        self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                         self.be_past).replace(
                        "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                      self.university).replace(
                        "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                            self.companyCity))
                sentence_4 = data_utils.capitalize_first(
                    sentence_4_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                        self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                         self.be_past).replace(
                        "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                      self.university).replace(
                        "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                            self.companyCity))
                sentence_5 = data_utils.capitalize_first(
                    sentence_5_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                        self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                         self.be_past).replace(
                        "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                      self.university).replace(
                        "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                            self.companyCity))
                sentence_6 = data_utils.capitalize_first(
                    sentence_6_list[i].replace("(subj_pronoun)", self.fullName).replace("(obj_pronoun)",
                                                                                        self.fullName).replace(
                        "(pos_pronoun)", self.fullName).replace("(be_present)", self.be_present).replace("(be_past)",
                                                                                                         self.be_past).replace(
                        "(birthday)", self.birthDate).replace("(birth_city)", self.birthCity).replace("(university)",
                                                                                                      self.university).replace(
                        "(major)", self.major).replace("(employer)", self.employer).replace("(company_city)",
                                                                                            self.companyCity))

                resultSentences = sentence_1 + " " + sentence_2 + " " + sentence_3 + " " + sentence_4 + " " + sentence_5 + " " + sentence_6
                resultSentenceslist.append(resultSentences)

            return resultSentenceslist

