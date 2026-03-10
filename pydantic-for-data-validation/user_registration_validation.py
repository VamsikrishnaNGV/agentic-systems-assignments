# Part 1: User Registration Validation
# Create a Pydantic model UserRegister with:
# username (str, min 5 characters)
# email (valid email)
# age (int, must be ≥ 18)
# Validate incoming data and reject invalid inputs.

from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationError

class UserRegister(BaseModel):
    username: str = Field(min_length=5, description="Username must be at least 5 characters")
    email: EmailStr = Field(description="Provide valid Email of the student", examples=["abc@gmail.com"])
    age: int = Field(ge=18, description="Age must be 18 or above")
    
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        domain_name = value.split('@')[-1]
        
        if domain_name != 'masai.com' :
            raise ValueError('Not a valid domain for email.')
        
        return value
    
user_data = {"username":"vamsi", "email":"vamsi.ngv@masai.com", "age":17}    

try:
    user_registration = UserRegister(**user_data)
    print(user_registration)
except ValidationError as e:
    print(e)