"""Pydantic models for structured outputs and tool results."""

from pydantic import BaseModel


class SampleOutput(BaseModel):
    """
    Represents a generic structured output from the AI.

    Attributes:
        result (str): The main content of the response.
    """
    integer_result: int
    string_result: str
    boolean_result: bool = False
