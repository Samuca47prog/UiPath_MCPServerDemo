from mcp.server.fastmcp import FastMCP

# ---- Pure functions (unit test) ----
def add_fn(a: float, b: float) -> float:
    return a + b

def subtract_fn(a: float, b: float) -> float:
    return a - b

def multiply_fn(a: float, b: float) -> float:
    return a * b

def divide_fn(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b

def fibonacci_fn(n: int) -> list[int]:
    n = max(0, min(n, 50))
    seq, a, b = [], 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# ---- MCP tool registrations ----
def register(app: FastMCP):
    @app.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        return add_fn(a, b)

    @app.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a."""
        return subtract_fn(a, b)

    @app.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return multiply_fn(a, b)

    @app.tool()
    def divide(a: float, b: float) -> float | None:
        """Divide a by b (returns None if dividing by zero)."""
        return divide_fn(a, b)

    @app.tool()
    def fibonacci(n: int) -> list[int]:
        """Return the first n Fibonacci numbers (n ≤ 50)."""
        return fibonacci_fn(n)
