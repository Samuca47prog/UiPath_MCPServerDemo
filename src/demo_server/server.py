from mcp.server.fastmcp import FastMCP
from .tools import math_tools, uipath_tools

def main():
    app = FastMCP("demo-server")
    math_tools.register(app)
    uipath_tools.register(app)
    # text_tools.register(app)
    app.run()

if __name__ == "__main__":
    main()