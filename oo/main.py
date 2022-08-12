data = {
    "account_number": "1293471-8",
    "agency": "3108",
    "bank": "Bradesco",
    "city": "Ipixuna Do Para",
    "state": "PA",
    "name": "Diego Julio Ribeiro",
    "document": "936.143.434-99",
    "birthday": "24/04/2002",
    "cellphone": "(94) 98248-7328",
}


class Account:
    def __init__(self, account_number, agency, bank, city, state, name, document, birthday, cellphone, balance, limit):
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
