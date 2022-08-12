def create_account(number: str, owner: str, balance: float, account_limit: float):
    """
    Create account in DigitalBank.

    Return:
        dictionary: all information regarding a client account.
    """
    data = {
        "number": number,
        "owner": owner,
        "balance": balance,
        "account_limit": account_limit,
    }
    return data


def deposit(account: dict, value: float):
    """
    To make a deposit in account bank.
    """
    balance = account.get("balance", 0)
    total_balance = balance + value

    account.update({"balance": total_balance})


def withdraw_money(account: dict, value: float):
    """
    To make a withdraw money in account bank.
    """
    balance = account.get("balance", 0)

    if balance <= 0:
        return ValueError(
            "You don't have enough money to procced with withdraw."
        )

    total_balance = balance - value

    account.update({"balance": total_balance})


def bank_statement(account: dict):
    bank_statement_form = f"""
    ------------------------------
    Bank Statement DigitalBank
    ------------------------------
    owner: {account.get("owner")}
    number: {account.get("number")}
    balance: {account.get("balance")}
    limit: {account.get("limit")}
    ------------------------------
    Thank You :)
    ------------------------------
    """
    return bank_statement_form
