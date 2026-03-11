# Part 1: You are building a User Registration System for an e-commerce platform.
# Design a Pydantic model system with the following requirements:

# Address Model

# city → string (minimum length 3)
# pincode → string (must be exactly 6 digits)
# User Model

# user_id → integer
# name → string
# email → email string
# age → integer (must be ≥ 18)
# address → nested Address model
# is_premium → optional boolean (default = False)
# Assignment validation should be enabled

from typing import Optional

from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator

class AddressModel(BaseModel):
    city: str = Field(..., min_length=3, description="City name should be minimum 3 characters")
    pincode: str
    
    @field_validator("pincode")
    @classmethod
    def pincode_validator(cls, value):
        if not value.isdigit() or len(value) != 6:
            raise ValueError("Pincode must be exactly 6 digits")
        return value

class UserModel(BaseModel):
    user_id: int
    name: str
    email: EmailStr = Field(..., description="Enter valid email address", examples=["abc@masai.com"])
    age: int = Field(..., ge=18, description="Age should be greater than or equal to 18 years")
    address: AddressModel
    is_premium: Optional[bool] = False

user_data = {"user_id":"76543", "name":"Vamsikrishna N G V", "email":"vamsi.ngv@gmail.com", "age": 18, "address":{"city":"Hyderabad", "pincode":"asd321"}}

try:
    user_data = UserModel(**user_data)
    print(user_data.address.city)
except ValidationError as e:
    print(e)
    