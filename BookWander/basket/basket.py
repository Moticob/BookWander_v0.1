


class Basket():
    """Base Baseket class"""

    def __init__(self, request):
        """"
        Retrieves user's session
        if not available, creates a new one
        """
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {'number':123123}
        self.basket = basket

    
    def add(self, book, qty):
        """
        Adding and updating the user's basket session data
        """
        book_id = book.id

        if book_id not in self.basket:
            self.basket[book_id] = {'price': str( book.price), 'qty':int(qty)}
        self.session.modified = True

    def __len__(self):
        """
        Gets basket data and counts qty of items
        """
        return sum(item['qty'] for item in self.basket.values())