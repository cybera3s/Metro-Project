class RegisterError(Exception):

    def __init__(self, msg: str, field: str, data: ...) -> None:
        super().__init__(msg, field, data)
        self.msg = msg
        self.field = field
        self.data = data

    def __str__(self):
        return f"Error on field `{self.field}` (invalid data: `{self.data}`): {self.msg}"


class AuthenticationError(Exception):

    def __init__(self, reason, msg, *args) -> None:
        super().__init__(reason, msg, *args)
        self.reason = reason
        self.msg = msg

    def __str__(self):
        return f"Error due to `{self.reason}` >> {self.msg}"


class BankAccountError(Exception):

    def __init__(self, reason, msg, *args) -> None:
        super().__init__(reason, msg, *args)
        self.reason = reason
        self.msg = msg

    def __str__(self):
        return f"Error due to `{self.reason}` >> {self.msg}"
