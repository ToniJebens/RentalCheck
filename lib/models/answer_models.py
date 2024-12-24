from pydantic import BaseModel, Field

from lib.models.base_models import (
    DateValue,
    MonetaryValue,
    StringValue,
)

class Name(BaseModel):
    name: StringValue

class Renters(BaseModel):
    names: list[Name] = Field(description="Names of all listed renters for this property.")

class Answers(BaseModel):
    renters: Renters
    letting_agency: StringValue
    property_address: StringValue
    agreement_date: DateValue
    deposit: MonetaryValue = Field(description="Deposit amount with currency.")
    rent: MonetaryValue = Field(description="Monthly rent amount with currency.")
