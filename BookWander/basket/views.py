from .basket import Basket
from django.shortcuts import get_object_or_404, render
from Wanderapp.models import Book
from django.http import JsonResponse

# Create your views here.


def basket_summary(request):
    basket = Basket(request)
    return render(request, "./basket/summary.html", {"basket": basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        book_id = int(request.POST.get("bookid"))
        book_qty = int(request.POST.get("bookqty"))
        book = get_object_or_404(Book, book_id=book_id)
        basket.add(book=book, qty=book_qty)
        basketqty = basket.__len__()
        response = JsonResponse({"qty": basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        book_id = int(request.POST.get("bookid"))
        basket.delete(book=book_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({"qty": basketqty, "subtotal": baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        book_id = int(request.POST.get("bookid"))
        book_qty = int(request.POST.get("bookqty"))

        basket.update(book=book_id, qty=book_qty)
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({"qty": basketqty, "subtotal": baskettotal})
        return response
