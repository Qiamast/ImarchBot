from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Image:
    """Image part of the search result item."""
    contextLink: str
    height: int
    width: int
    byteSize: int
    thumbnailLink: str
    thumbnailHeight: int
    thumbnailWidth: int


@dataclass(frozen=True)
class Item:
    """An item from search results."""
    kind: str
    title: str
    html_title: str
    link: str
    display_link: str
    snippet: str
    html_snippet: str
    cache_id: Optional[str] = None
    formatted_url: Optional[str] = None
    html_formatted_url: Optional[str] = None
    pagemap: Optional[Dict[str, Any]] = None
    mime: Optional[str] = None
    file_format: Optional[str] = None
    image: Optional[Image] = None


@dataclass(frozen=True)
class SearchResult:
    """A search result from GSE API."""
    kind: str
    url: Dict[str, str]
    queries: Dict[str, Any]
    context: Dict[str, Any]
    search_information: Dict[str, Any]
    items: List[Item]
    spelling: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert the search result object to a dictionary."""
        return asdict(self)
