from datetime import datetime

from pydantic import BaseModel, Field
from pydantic import ValidationError as PydanticValidationError
from pydantic import field_validator

from .utils import convert_pydantic_validation_error_to_field_errors


class MealValidator:
    class BaseMeal(BaseModel):
        name: str = Field(..., min_length=3, max_length=50)
        description: str = Field(..., min_length=3, max_length=100)
        datetime: str
        in_diet: bool

        @field_validator("datetime")
        def validate_datetime(cls, v):
            datetime.fromisoformat(v)
            return v

    @staticmethod
    def validate_create_meal(data):
        try:
            return MealValidator.BaseMeal(**data).model_dump()
        except PydanticValidationError as e:
            raise convert_pydantic_validation_error_to_field_errors(e)

    @staticmethod
    def validate_update_meal(data):
        try:
            return MealValidator.BaseMeal(**data).model_dump()
        except PydanticValidationError as e:
            raise convert_pydantic_validation_error_to_field_errors(e)
