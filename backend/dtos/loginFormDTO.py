from pydantic import BaseModel, Field, ConfigDict

class LoginFormRequestDTO(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    username: str = Field(description="User Name")
    password: str = Field(description="Password")
