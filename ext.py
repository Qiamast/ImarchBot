import re
from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class InlineCommand:
    """Represents a command parsed from an inline query string."""
    name: str
    """Name of the command."""
    value: Optional[str] = None
    """Value of the command (if any)."""


@dataclass(frozen=True)
class ParsedQuery:
    """Represents a parsed query object from an inline query string."""
    text: str
    """The original query string that was parsed."""
    query: str
    """The query string without the commands."""
    commands: Optional[List[InlineCommand]] = None
    """A list of tuples of commands and their arguments from the query."""


def parse_query(text: str) -> ParsedQuery:
    """Return a parsed query object from the given query string.

    Args:
        - text (`str`): The query string to parse.

    Returns:
        - `ParsedQuery`: A parsed query object.
    """
    cmd_pattern = r"([0-9a-zA-Z_]+):([^\s]*)"
    commands = re.findall(cmd_pattern, text)
    if commands:
        commands = [
            InlineCommand(name, value)
            for name, value in commands
        ]
    query = re.sub(cmd_pattern, "", text).strip()
    return ParsedQuery(text, query, commands)
