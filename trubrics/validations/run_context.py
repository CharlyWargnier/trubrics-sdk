"""
Something
"""

from typing import Any, Optional

from pydantic import BaseModel, validator

from trubrics.context import DataContext, TrubricContext
from trubrics.validations import ModelValidator


class TrubricRun(BaseModel):
    """The TrubricRun object to group all necessary contexts in order for a run.
    Attributes:
        data_context: a data context to validate a model on
        model_context: a model context with the model to validate
        trubric_context: a trubric context listing all validations to execute
        custom_validator: an optional custom validator
    """

    data_context: DataContext
    model: Any
    trubric_context: TrubricContext
    custom_validator: Optional[Any] = None

    @validator("custom_validator")
    def validate_some_foo(cls, val):
        if issubclass(val, ModelValidator):
            return val
        raise TypeError("Wrong type for 'custom_validator', must be subclass of ModelValidator.")