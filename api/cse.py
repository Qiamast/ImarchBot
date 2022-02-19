from typing import Any, ClassVar, Dict, Optional, Union
from urllib.parse import urlencode, urljoin

from requests import HTTPError, Response, Session

from .exceptions import AuthError, CSEAPIError
from .types import Image, Item, SearchResult


class GoogleSearchEngine:
    """Google custom search engine handler.
    
    Args:
        - api_key (`str`): Google API key.
        - engine_id (`str`): Google custom search engine (CSE) ID (can be found in the CSE panel).
        
    Note:
        - If you want to get image results, you need to enable "Image Search" in your CSE configuration.
        
    You can access your CSE configuration at:
    https://programmablesearchengine.google.com/
    """
    VERSION: ClassVar[str] = "1"
    """GSE API version to use."""
    BASE_URL: ClassVar[str] = f"https://www.googleapis.com/customsearch/v{VERSION}/"
    """GSE API base URL."""
    
    def __init__(self, api_key: str, engine_id: str) -> None:
        self.api_key = api_key
        self.engine_id = engine_id
        self._sess = Session()
        
    @property
    def auth_params(self) -> Dict[str, str]:
        """Returns GSE API authentication parameters."""
        return {
            "key": self.api_key,
            "cx": self.engine_id,
        }

    def __repr__(self) -> str:
        return "%s(api_key=%r, engine_id=%r)" % (
            self.__class__.__name__, 
            self.api_key, 
            self.engine_id
        )
    
    def __enter__(self) -> "GoogleSearchEngine":
        return self
    
    def __exit__(self, *args) -> None:
        self.close()
        
    def _request(self, method: str, endpoint: str, **kwargs) -> Response:
        """Sends a request to GSE API and returns the response."""
        url = urljoin(self.BASE_URL, endpoint)
        r = self._sess.request(method, url, **kwargs)
        try:
            r.raise_for_status()
        except HTTPError:
            status_code = r.status_code
            if status_code in (401, 403):
                raise AuthError(
                    "Authentication error occurred, API response: %s" % r.text
                )
            else:
                raise CSEAPIError(
                    "An error occurred while requesting the API, status code: %s, response: %s" % (
                        status_code, r.text
                    ),
                    status_code
                )
        return r

    def search(
        self, 
        query: str, 
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        safe_search: Optional[bool] = None,
        only_image: Optional[bool] = None,
        **kwargs
    ) -> Union[SearchResult, Dict[str, Any]]:
        """Search functionality for GSE API.
        
        Args:
            - query (`str`): The query to search for.
            - page (`int`): The page number to return.
            - per_page (`int`): The number of results per page.
            - safe_search (`bool`): Whether to return results that may contain adult content.
            - only_image (`bool`): Whether to return only image results.
                
        Possible kwargs:
            - as_dict (`bool`): Whether to return the result as a dictionary.        
        
        Returns:
            - `~api.types.SearchResult`: The search result object containing the search results.
            
        Note:
            - :class:`~api.types.SearchResult` is a dataclass containing the search results 
            that can be easily converted to a dictionary by calling :meth:`.to_dict()`
            method on it.
        """
        _page = abs(int(page or 1))
        if _page == 0:
            _page = 1
        _start = (_page - 1) * 10 + 1
        params = {
            **self.auth_params,
            "q": query,
            "start": _start,
            "safe": "off" if not safe_search else "active",
        }
        if per_page and 1 <= int(per_page) <= 10:
            params["num"] = per_page
        if only_image:
            params["searchType"] = "image"
        ep = "?{}".format(urlencode(params))
        res: Dict[str, Any] = self._request("GET", ep).json()
        if kwargs.get("as_dict", False):
            return res
        # parse the response and return the search result object
        items = []
        if res.get("items"):
            items = [
                Item(
                    kind=item["kind"],
                    title=item["title"],
                    html_title=item["htmlTitle"],
                    link=item["link"],
                    display_link=item["displayLink"],
                    snippet=item["snippet"],
                    html_snippet=item["htmlSnippet"],
                    cache_id=item.get("cacheId"),
                    formatted_url=item.get("formattedUrl"),
                    html_formatted_url=item.get("htmlFormattedUrl"),
                    pagemap=item.get("pagemap"),
                    mime=item.get("mime"),
                    file_format=item.get("fileFormat"),
                    image=Image(**item["image"]) if only_image else None
                )
                for item in res["items"]
            ]
        return SearchResult(
            kind=res["kind"],
            url=res["url"],
            queries=res["queries"],
            context=res.get("context"),
            search_information=res["searchInformation"],
            items=items,
            spelling=res.get("spelling")
        )

    def close(self) -> None:
        """Closes the GSE API session."""
        self._sess.close()
