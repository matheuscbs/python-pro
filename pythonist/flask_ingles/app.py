"""
Implementation of a simplified routing system inspired by Flask.
"""

# Dictionary to store registered routes
_routes = {}


class RouteNotFound(Exception):
    """
    Exception raised when a requested route does not exist.
    """
    def __init__(self, path):
        super().__init__(f'Route not found: {path}')


def route(path):
    """
    Decorator to register a function as a route.

    Args:
        path (str): The route path to register.

    Returns:
        function: The decorated function.
    """
    def decorator(func):
        _routes[path] = func
        return func
    return decorator


def route_dispatch(path, *args, **kwargs):
    """
    Executes the function corresponding to the provided route.

    Args:
        path (str): The route path to execute.
        *args: Positional arguments for the route function.
        **kwargs: Named arguments for the route function.

    Returns:
        Any: The return value of the executed route function.

    Raises:
        RouteNotFound: If the specified route does not exist.
    """
    if path not in _routes:
        raise RouteNotFound(path)
    return _routes[path](*args, **kwargs)
