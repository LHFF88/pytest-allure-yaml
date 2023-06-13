import json


class DoubleQuoteDict(dict):

    def __str__(self):

        return json.dumps(self)

    def __repr__(self):

        return json.dumps(self)

