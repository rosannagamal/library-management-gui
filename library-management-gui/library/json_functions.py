import json
from classes.user import User
from classes.book import Book


def unload_json(file) -> dict:
    def get_data(file):
        # getting the entire dictionary from json file

        with open(file) as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return dict()

    def return_class_instance(string):
        # return_class_instance(key) returns User() if the dict contains
        # user data and Book() if the dict contains book data

        lst = ["registered", "restricted", "active loans", "users"]
        return User() if string in lst else Book()

    data = get_data(file)  # dict from JSON file

    keys_lst = list(data.keys())  # extracting keys from dictionary

    general_dict = (
        dict()
    )  # initializing dict that will contain all previously created instances

    for key in keys_lst:

        # checking if the key is not 'active loans' since active loans is a dict and not a class instance
        if key != "active loans":

            # using return_class_instance(key) in order to use the correct method for the data type
            classs = return_class_instance(key)

            general_dict[key] = [classs.instance(dct) for dct in data[key]]

        else:
            general_dict[key] = data[key]

    return general_dict


def load_json(file, dct) -> None:

    with open(file, "w") as f:
        json.dump(dct, f, indent=5)