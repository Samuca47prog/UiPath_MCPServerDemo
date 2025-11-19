import pytest
from demo_server.tools.uipath_tools import get_folders_fn

def test_get_folders_fn_returns_list():
    """Verify get_folders_fn returns a list of folders with correct fields."""
    folders = get_folders_fn()
    assert isinstance(folders, list)

    if not folders:
        pytest.skip("No folders returned from the current Orchestrator context.")

    first = folders[0]
    assert isinstance(first, dict)
    assert "key" in first
    assert "name" in first
    assert "path" in first

    print("folders list:")
    for f in folders:
        print(f"{f['path']}")