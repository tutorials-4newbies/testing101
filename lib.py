class Validator:
    def __init__(self, val):
        self.val = val

    def is_valid(self):
        res = self._validate()
        return res

    def _validate(self):
        raise NotImplementedError("_validate Not implemented")


VALID_PREFIXES = ["054", "055", "052", "053", "077"]


class CellPhoneValidator(Validator):
    def _validate(self):

        for char in self.val:
            if not char.isdigit():
                return False
        prefix = self.val[0:3]
        if prefix not in VALID_PREFIXES:
            return False
        return True
