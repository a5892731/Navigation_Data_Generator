'''
file version 1.0
author: a5892731
date: 2021-03-04
'''
import os


class DataExport:

    def __init__(self, data, FILE_ADDRESS, CALL_TYPE, FILE_FOLDER = "data_output"):
        self.list = []
        self.dicionary = {}
        self.call_type = CALL_TYPE

        self.open_file(FILE_ADDRESS, FILE_FOLDER)

        if CALL_TYPE == "list":
            self.list = data
            self.save_list()
        elif CALL_TYPE == "dict":
            self.dicionary = data
            self.save_dict()

    def __call__(self):
        if self.call_type == "list":
            return self.list
        elif self.call_type == "dict":
            return self.dicionary
        else:
            return None

    def open_file(self, FILE_ADDRESS, FILE_FOLDER):
        os.chdir(FILE_FOLDER)
        self.file = open(FILE_ADDRESS, "w")
        os.chdir("..")

    def save_list(self):
        for element in self.list:
            print("{}".format(element), file = self.file)

        self.file.close()

    def save_dict(self):
        for key in self.dicionary:
            print("{}: {}".format(key, self.dicionary[key]), file = self.file)
        self.file.close()


if __name__ == "__main__":  # test

    os.chdir("..")



    os.chdir("system")
