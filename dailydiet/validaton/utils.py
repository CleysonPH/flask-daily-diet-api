from .errors import FieldError, ValidationError


def convert_pydantic_validation_error_to_field_errors(e):
    errors = {}
    for error in e.errors():
        field = error["loc"][0]
        if field not in errors:
            errors[field] = []
        errors[field].append(error["msg"])
    return ValidationError(
        [FieldError(field, errors[field]) for field in errors]
    )
