from Wanderapp.models import Book
from decimal import Decimal


class Basket:
    """Base Baseket class"""

    def __init__(self, request):
        """ "
        Retrieves user's session
        if not available, creates a new one
        """
        self.session = request.session
        basket = self.session.get("skey")
        if "skey" not in request.session:
            basket = self.session["skey"] = {}
        self.basket = basket

    def add(self, book, qty):
        """
        Adding and updating the user's basket session data
        """
        book_id = str(book.book_id)

        if book_id in self.basket:
            self.basket[book_id]['qty'] = qty
        else:
            self.basket[book_id] = {"price": str(book.price), "qty": int(qty)}
        self.save()

    def __iter__(self):
        """
        Collects the book_id in the session data to query
        the database and return products
        """
        book_ids = self.basket.keys()
        books = Book.books.filter(book_id__in=book_ids)
        basket = self.basket.copy()

        for book in books:
            basket[str(book.book_id)]["book"] = book

        for item in basket.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        """
        Gets basket data and counts qty of items
        """
        return sum(item["qty"] for item in self.basket.values())

    def get_total_price(self):
        """
        Returns total basket price
        """
        return sum(
            Decimal(item["price"]) * item["qty"] for item in self.basket.values()
        )

    def delete(self, book):
        """
        Delete item from session data
        """
        book_id = str(book)
        if book_id in self.basket:
            del self.basket[book_id]
            self.save()

    def update(self, book, qty):
        """
        Updates values in session data
        """
        book_id = str(book)

        if book_id in self.basket:
            self.basket[book_id]["qty"] = qty
        self.save()

    def save(self):
        self.session.modified = True
