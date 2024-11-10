from pydantic import BaseModel, ConfigDict


class BaseRespone(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
