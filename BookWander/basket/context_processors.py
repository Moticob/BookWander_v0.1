"""
Any object defined here would be available throughout
the project
"""

from .basket import Basket


def basket(request):
    return {"basket": Basket(request)}
