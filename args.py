import argparse


class args(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.initialize()

    def initialize(self):
        self.parser.add_argument('--Sample_size_people', default=None)
        self.parser.add_argument('--Sample_size_birthday_choices', default="200 x 12 x 28")
        self.parser.add_argument('--Sample_size_birth_city_choices', default=None)
        self.parser.add_argument('--Sample_size_university_choices)', default=None)
        self.parser.add_argument('--Sample_size_major_choices)', default=None)
        self.parser.add_argument('--Sample_size_employer_company_city_choices)', default=None)

    def parse(self):
        self.args = self.parser.parse_args()
        return self.args
