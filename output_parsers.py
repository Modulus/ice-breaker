from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Summary(BaseModel):
    summary : str  = Field(description="summary")
    facts : List[str]= Field(description="interesting facts about them")

    required: list[str] = Field(default=["summary", "facts"])

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts}
    
# TO debug
def parse_json(json_str: str) -> Summary:
    parsed_json = PydanticOutputParser(pydantic_object=Summary).parse(json_str)
    if not isinstance(parsed_json, Summary):
        raise ValueError("Invalid JSON format")
    return parsed_json

summary_parser = PydanticOutputParser(pydantic_object=Summary)
