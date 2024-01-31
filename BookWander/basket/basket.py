


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