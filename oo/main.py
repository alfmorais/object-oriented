# pendencies for class
# 1:TODO: To create a regex form for account number value
# 2:TODO: To create a validate method or external lib to document
# 3:TODO: To create a regex form for document
# 4:TODO: To create a regex form for birthday
# 5:TODO: To create a regex form for cellphone


class Account:
    """
    Class to represent the account object.
    """

    def __init__(
        self,
        account_number: str,
        agency: str,
        bank: str,
        city: str,
        state: str,
        name: str,
        document: str,
        birthday: str,
        cellphone: str,
        balance: float,
        limit: float,
    ):
        self.account_number = account_number
        self.agency = agency
        self.bank = bank
        self.city = city
        self.state = state
        self.name = name
        self.document = document
        self.birthday = birthday
        self.cellphone = cellphone
        self.balance = balance
        self.limit = limit

    def __str__(self):
        return f"{self.account_number} - {self.name}"
