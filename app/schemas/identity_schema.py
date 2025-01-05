from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field, model_validator
from app.models.enums_model import GenderEnum
from app.utils.validators_utils import ValidationUtils


class IdentityBase(BaseModel):
    """
    Base schema for an identity, including common fields.
    """
    first_name: Optional[str] = Field(None, min_length=1, max_length=50, description="First name of the individual")
    last_name: Optional[str] = Field(None, min_length=1, max_length=50, description="Last name of the individual")
    gender: Optional[GenderEnum] = Field(None, description="Gender of the individual")
    valid_from: Optional[date] = Field(None, description="The start date of this identity's validity")
    valid_until: Optional[date] = Field(None, description="The end date of this identity's validity")

    @model_validator(mode='after')
    def validate_dates(cls, values: 'IdentityBase') -> 'IdentityBase':
        """
        Validates that `valid_from` is earlier than `valid_until`.
        """
        if values.valid_from and values.valid_until:
            ValidationUtils.validate_date_order(
                values.valid_from,
                values.valid_until,
                "Valid from date cannot be after valid until date."
            )
        return values

    class Config:
        from_attributes = True


class IdentityCreate(IdentityBase):
    """
    Schema for creating a new identity.
    """
    individual_id: int = Field(..., description="ID of the associated individual")


class IdentityUpdate(BaseModel):
    """
    Schema for updating an existing identity.
    """
    first_name: Optional[str] = Field(None, min_length=1, max_length=50, description="Updated first name")
    last_name: Optional[str] = Field(None, min_length=1, max_length=50, description="Updated last name")
    gender: Optional[GenderEnum] = Field(None, description="Updated gender")
    valid_from: Optional[date] = Field(None, description="Updated start date of validity")
    valid_until: Optional[date] = Field(None, description="Updated end date of validity")
    is_primary: Optional[bool] = Field(None, description="Whether this identity is the primary identity")

    @model_validator(mode='after')
    def validate_dates(cls, values: 'IdentityUpdate') -> 'IdentityUpdate':
        """
        Validates that `valid_from` is earlier than `valid_until`.
        """
        if values.valid_from and values.valid_until:
            ValidationUtils.validate_date_order(
                values.valid_from,
                values.valid_until,
                "Valid from date cannot be after valid until date."
            )
        return values

    class Config:
        from_attributes = True


class IdentityOut(IdentityBase):
    """
    Schema for returning identity data.
    """
    id: int = Field(..., description="The unique ID of the identity")
    individual_id: int = Field(..., description="The ID of the associated individual")
    is_primary: bool = Field(..., description="Indicates if this is the primary identity")
    created_at: datetime = Field(..., description="The timestamp when this identity was created")
    updated_at: datetime = Field(..., description="The timestamp when this identity was last updated")

    class Config:
        from_attributes = True