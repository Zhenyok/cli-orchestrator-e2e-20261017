"""Simple greeting helper."""


def greet(name: str) -> str:
    """Return a greeting for ``name`` after trimming surrounding whitespace.

    Raises ValueError if the name is empty or contains only whitespace.
    """
    trimmed = name.strip()
    if not trimmed:
        raise ValueError("name must not be empty")
    return f"Hello, {trimmed}!"
