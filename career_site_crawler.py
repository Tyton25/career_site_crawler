from bs4 import BeautifulSoup
import csv
import os
import requests


class CareerSiteCrawler:
    def __init__(self, in_file):
        self.input_file = in_file

    def run(self):
        login_list = self.read_csv()
        company_name = login_list[0]
        url = login_list[1]
        username = login_list[2]
        password = login_list[3]

    def read_csv(self):
        login_list = []
        with open(self.input_file, 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                login_list.append(row)
        return login_list

    def career_sites(self):
        pass


def parse_args():
    pass


def get_args():
    pass


if __name__ == '__main__':
    CareerSiteCrawler()
