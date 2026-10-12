from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    age: int = Field(gt=0)
    email: str


user = User(name="Alice", age=30, email="alice@example.com")

print(user)
print(user.model_dump())
