class Validator:
    def __init__(self, val):
        self.val = val

    def is_valid(self):
        res = self._validate()
        return res

    def _validate(self):
        raise NotImplementedError("_validate Not implemented")


class CellPhoneValidator(Validator):
    pass
