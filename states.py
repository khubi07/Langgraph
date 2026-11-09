import os

# 1st way: typed dict, common appeoach

from typing import TypedDict

class State(TypedDict):
    topic : str
    summary : str
    score : int

# 2nd way: pydantic approach
# good at data validation and type checking during runtime

from pydantic import BaseModel, field_validator

class state(BaseModel):
    topic : str
    summary : str = ""
    score : int

    @field_validator("score")
    def score_positive(cls,v: int)
        if v < 0:
            raise ValueError("score must be positive")

# 3rd way: python dataclass, used rarely
from dataclasses import dataclass, field 

@dataclass
class State:
    topic : str = ""
    summary  : str = ""
    messages : list = field(default_factory=list)

# 4th way: using langgraph
from langgraph.graph import MessagesState

class State(MessagesState):
    # messages field is already included with add_messages reducer
    # just add your extra fields
    user_name: str
    language: str