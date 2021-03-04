'''
file version 1.2
author: a5892731
date: 2021-03-04
'''
import os


class DataImport:

    def __init__(self, FILE_ADDRESS, CALL_TYPE, FILE_FOLDER = "data_files"):
        self.list = []
        self.dicionary = {}
        self.call_type = CALL_TYPE

        self.open_file(FILE_ADDRESS, FILE_FOLDER)

        if CALL_TYPE == "list":
            self.read_list()
        elif CALL_TYPE == "dict":
            self.read_dict()

    def __call__(self):
        if self.call_type == "list":
            return self.list
        elif self.call_type == "dict":
            return self.dicionary
        else:
            return None

    def open_file(self, FILE_ADDRESS, FILE_FOLDER):
        os.chdir(FILE_FOLDER)
        self.file = open(FILE_ADDRESS, "r")
        os.chdir("..")

    def read_list(self):
        for line in self.file:
            self.list.append(line.rstrip("\n"))
        self.file.close()

    def read_dict(self):
        for line in self.file:
            line = line.rstrip("\n").split(": ")
            self.dicionary[line[0]] = line[1]
        self.file.close()


if __name__ == "__main__":  # test

    os.chdir("..")


    os.chdir("system")