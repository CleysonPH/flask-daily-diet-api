class FieldError:
    def __init__(self, field, errors):
        self.field = field
        self.errors = errors


class ValidationError(Exception):
    def __init__(self, errors, message="Validation error"):
        self.errors = errors
        self.message = message

    def to_dict(self):
        return {
            "message": self.message,
            "errors": {error.field: error.errors for error in self.errors},
        }
