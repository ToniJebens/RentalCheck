from pydantic import BaseModel, Field
from typing import Union

CITATION_STRING = "An exact sub-string of the provided text that provides the most relevant citation to the answer. Can be None if answer is None."

class StringValue(BaseModel):
    value: Union[str, None]
    citation: Union[str, None] = Field(description=CITATION_STRING)

class NumericValue(BaseModel):
    amount: Union[int, float, None]
    citation: Union[str, None] = Field(description=CITATION_STRING)

class MonetaryValue(BaseModel):
    amount: Union[int, float, None]
    currency: Union[str, None]
    citation: Union[str, None] = Field(description=CITATION_STRING)

class DateValue(BaseModel):
    day: Union[int, None]
    month: Union[int, None]
    year: Union[int, None]
    citation: Union[str, None] = Field(description=CITATION_STRING)
    