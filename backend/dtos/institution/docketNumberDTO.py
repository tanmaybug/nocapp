from pydantic import BaseModel


class SetDocketNumberRequest(BaseModel):
    docketNumber: str
