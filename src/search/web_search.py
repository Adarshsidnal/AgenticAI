"""Web search using DuckDuckGo."""

from duckduckgo_search import DDGS


def search_web(query: str, max_results: int = 3) -> str:
    """
    Search the web and return combined results.
    
    Args:
        query: Search query
        max_results: Maximum number of results to return
    
    Returns:
        Combined text from search results
    """
    search_results = []
    
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        
        for r in results:
            search_results.append(r["body"])
    
    search_text = "\n".join(search_results)
    return search_text
