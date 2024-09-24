import enum


class ApiType(enum.Enum):
    ORDER = 'ORDER'
    TICKER = 'TICKER'
    HISTORY = 'HISTORY'
    PNL = 'PNL'

    def __repr__(self):
        return self.value
