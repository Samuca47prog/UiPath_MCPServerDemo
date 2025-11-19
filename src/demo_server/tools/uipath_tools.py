from uipath import UiPath
from mcp.server.fastmcp import FastMCP

def get_folders_fn(limit: int = 20, search_text: str = "") -> list[dict]:
    """
    List folders using the low-level ApiClient in the UiPath SDK.
    Auth and base URL are handled automatically by the SDK.
    """
    sdk = UiPath()
    client = sdk.api_client

    url = "orchestrator_/api/FoldersNavigation/GetFoldersForCurrentUser"
    params = {"searchText": search_text, "skip": 0, "take": limit}

    response = client.request("GET", url, scoped="tenant", params=params)
    data = response.json()

    items = data.get("items") or data.get("PageItems") or []
    return [
        {
            "key": f.get("Key"),
            "name": f.get("DisplayName"),
            "path": f.get("FullyQualifiedName"),
        }
        for f in items
    ]


def register(app: FastMCP):
    """Register UiPath demo tools (simple get_folders)."""

    @app.tool()
    def get_folders(limit: int = 20, search_text: str = "") -> dict:
        """
        Fetch folders visible to the current user from UiPath Orchestrator.
        """
        return get_folders_fn(limit, search_text)
