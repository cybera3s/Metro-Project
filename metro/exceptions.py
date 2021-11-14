class RegisterError(Exception):

    def __init__(self, msg: str, field: str, data: ...) -> None:
        super().__init__(msg, field, data)
        self.msg = msg
        self.field = field
        self.data = data

    def __str__(self):
        return f"Error on field `{self.field}` (invalid data: `{self.data}`): {self.msg}"
