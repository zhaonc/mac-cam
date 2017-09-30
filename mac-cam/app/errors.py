class GenericError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        """
        Base class for all error responses.
        :param message:
        :param status_code:
        :param payload:
        """
        Exception.__init__(self)

        self.message = message
        if status_code is not None:
            self.status_code = status_code

        self.payload = payload

    def to_dict(self):
        kv = dict(self.payload or ())
        kv['message'] = self.message
        return kv


class Forbidden(GenericError):
    def __init__(self, message, payload=None):
        GenericError.__init__(self, message, 403, payload)
