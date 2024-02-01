from .basket import Basket
from django.shortcuts import get_object_or_404, render
from Wanderapp.models import Book
from django.http import JsonResponse
# Create your views here.

def basket_summary(request):
    basket = Basket(request)
    return render(request, 'Wanderapp/basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookid'))
        book_qty = int(request.POST.get('bookqty'))
        book = get_object_or_404(Book, id=book_id)
        basket.add(book=book, qty=book_qty)
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response