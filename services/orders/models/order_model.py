from pydantic import BaseModel, field_validator

class OrderModel(BaseModel):
    status: str
    courierId: int
    customerName: str
    customerPhone: str
    comment: str
    id: int

    @field_validator("status","customerName", "customerPhone", "comment")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value