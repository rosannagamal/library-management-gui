class User(object):
    def __init__(self, name: str = "", email: str = "", username: str = "", password: str = "",
                 municipality: str = None, social_sec_num: str = None, credit_card: list = None):

        self.name = name
        self.id_num: int = id(self)
        self.email = email
        self.username = username
        self.password = password

        # Optional Arguments
        self.municipality = municipality
        self._social_sec_num = social_sec_num
        self.credit_card = credit_card

    @property
    def social_sec_num(self) -> int:
        return int(self._social_sec_num)

    @social_sec_num.setter
    def social_sec_num(self, num: str):
        while len(num) != 9:
            # Making sure that the social security number is 9 digits long
            self.social_sec_num(input("social security number must be 9 digits long"))
        self._social_sec_num = num

    def __dict__(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "priv_level": self.__class__.__name__,
            "username": self.username,
            "password": self.password,
            "id_num": self.id_num,
            "municipality": self.municipality,
            "ssn": self.social_sec_num,
            "card data": self.credit_card,
        }

    def __str__(self) -> str:
        return f"{self.name}\t{'id_num'}\t{self.email}\t{self.municipality}\t" \
               f"{self.social_sec_num}\t{self.credit_card}\t"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, type(self)):
            return NotImplemented
        return self.name == __o.name

    def instance(self, dct) -> str:

        # values = [name, email, priv_level, username, password, id_num, municipality, ssn, card data, books borrowed]

        values = dict(dct.items())

        # creating a new instance of the User class from values extracted from dict

        users_dict = {
            "Regular": Regular,
            "Student": Student,
            "Librarian": Librarian,
            "Admin": Admin,
        }

        priv_level = values["priv_level"]

        user = users_dict[priv_level](
            name=values["name"],
            email=values["email"],
            username=values["username"],
            password=values["password"],
            municipality=values["municipality"],
            social_sec_num=values["ssn"],
            credit_card=values["card data"],
        )

        # setting the id_num from data in dict
        user.id_num = values["id_num"]

        return user


class Regular(User):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __dict__(self) -> dict:
        return super().__dict__()


class Student(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __dict__(self) -> dict:
        return super().__dict__()


class Librarian(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __dict__(self) -> dict:
        return super().__dict__()


class Admin(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __dict__(self) -> dict:
        return super().__dict__()