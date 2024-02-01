from django import setup
from django.test import TestCase
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password, is_password_usable, identify_hasher
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookWander.settings")
setup()
from api.models import User, Book, Order, OrderItem
# Tests for the models.


class TestUser(TestCase):
    """tests user model
    """
    USERNAME = "robin_book_worm"
    EMAIL = "rb@ohara.com"
    PASSWRD = make_password("ftpNOg8", hasher="bcrypt")
    ID = None
    CREATEDAT = None

    def setUp(self):
        """ the set up function"""
        self.u1 = User.objects.create(
            username=self.USERNAME,
            email=self.EMAIL,
            password_hash=self.PASSWRD,
            registration_date=timezone.now()
        )
        self.ID = User.objects.get(email=self.EMAIL).user_id
        self.CREATEDAT = User.objects.get(email=self.EMAIL).registration_date

    def tearDown(self):
        """ the tear down function"""
        User.objects.all().delete()

    def test_pass_crypt(self):
        """tests the encryption 
        this shoud be added to the testviews"""
        self.assertTrue(is_password_usable(self.PASSWRD))
        self.assertTrue(self.PASSWRD.startswith("bcrypt$"))
        self.assertTrue(check_password("ftpNOg8", self.PASSWRD))
        self.assertFalse(check_password("ftpnOg8", self.PASSWRD))
        self.assertEqual(identify_hasher(self.PASSWRD).algorithm, "bcrypt")

    def test_instance(self):
        """checks if instance is created"""
        self.assertTrue(isinstance(self.u1, User))
        self.assertEqual(True, self.u1 in User.objects.all())

    def test_attrs(self):
        """ checks the name of attributes created and their values"""
        self.assertTrue(hasattr(self.u1, "user_id"))
        self.assertTrue(hasattr(self.u1, "username"))
        self.assertTrue(hasattr(self.u1, "email"))
        self.assertTrue(hasattr(self.u1, "password_hash"))
        self.assertTrue(hasattr(self.u1, "registration_date"))
        self.assertIsNotNone(self.ID)
        self.assertEqual(self.u1.username, self.USERNAME)
        self.assertEqual(self.u1.email, self.EMAIL)
        self.assertTrue(self.u1.password_hash.startswith("bcrypt$"))
        self.assertTrue(check_password("ftpNOg8", self.u1.password_hash))
        self.assertFalse(check_password("ftpnOg8", self.u1.password_hash))
        self.assertEqual(identify_hasher(self.u1.password_hash).algorithm, "bcrypt")
        self.assertEqual(self.u1.registration_date, self.CREATEDAT)

    def test_update(self):
        """ tests the updating of an instance"""
        User.objects.filter(user_id=self.ID).update(password_hash=make_password("motpNOg8", hasher="bcrypt"))
        self.u1.refresh_from_db()
        self.assertNotEqual(self.u1.password_hash, self.PASSWRD)
        self.assertTrue(check_password("motpNOg8", self.u1.password_hash))
        self.assertEqual(self.u1.registration_date, self.CREATEDAT)


class TestBook(TestCase):
    """tests for the Book model.
    
    """
    def setUp(self):
        """ the set up function"""
        self.b1 = Book.objects.create(
            title = "Dune",
            author = "Frank Herbert",
            genre = "Science Fiction",
            publication_date = timezone.now(),
            price = 100.00
        )
        self.ID = Book.objects.get(title="Dune").book_id

    def tearDown(self):
        """ the tear down function"""
        Book.objects.all().delete()

    def test_instance(self):
        """checks if instance is created"""
        self.assertTrue(isinstance(self.b1, Book))
        self.assertEqual(True, self.b1 in Book.objects.all())   

    def test_attrs(self):
        """
        checks the name of attributes created and their values
        """
        attribs = ["book_id", "title", "author",
                   "genre", "publication_date", "price",
                   "description", "cover_image_url"
                   ]
        for a in attribs:
            self.assertTrue(hasattr(self.b1, a))
        self.assertIsNotNone(self.ID)

    def test_update(self):
        """
        tests update description
        """
        text_desc = "Set on the desert planet Arrakis,\
            Dune is the story of the boy Paul Atreides,\
            heir to a noble family tasked with ruling\
            an inhospitable world where the only thing\
            of value is the 'spice' melange, a\
            drug capable of extending life and enhancing consciousness.\
            Coveted across the known universe,\
            melange is a prize worth killing for...."
        self.assertEqual(self.b1.description, "")
        Book.objects.filter(book_id=self.ID).update(description=text_desc)
        self.b1.refresh_from_db()
        self.assertNotEqual(self.b1.description, None)

    def test_delete(self):
        """
        tests delete book
        """
        Book.objects.filter(book_id=self.ID).delete()
        self.assertFalse(Book.objects.filter(book_id=self.ID).all())


class TestOrder(TestCase):
    """tests for the Order, OrderItem models.
    """


    def setUp(self):
        """ the set up function"""
        u1_val = ["robin_book_worm", "rb@ohara.com",
               make_password("ftpNOg8", hasher="bcrypt")
               ]
        b1_val = ["Dune", "Frank Herbert",
                  "Science Fiction",
                  "Set on the desert planet Arrakis..."]
        self.u1 = User.objects.create(
            username = u1_val[0],
            email = u1_val[1],
            password_hash = u1_val[2],
            registration_date = timezone.now()
        )
        self.b1 = Book.objects.create(
            title = b1_val[0],
            author = b1_val[1],
            genre = b1_val[2],
            publication_date = timezone.now(),
            price = 100.00,
            description = b1_val[3]
        )
        self.o1 = Order.objects.create(
            user_id = self.u1,
            order_date = timezone.now(),
            total_amount = 0
        )
        self.oi1 = OrderItem.objects.create(
            order_id = self.o1,
            book = self.b1,
            quantity = 3
        )
        self.u1_id = self.u1.user_id
        self.b1_id = self.b1.book_id
        self.o1_id = self.o1.order_id
        self.oi1_id = self.oi1.order_item_id

    def tearDown(self):
        """ the tear down function"""
        User.objects.all().delete()
        Book.objects.all().delete()
        Order.objects.all().delete()

    def test_instance(self):
        """checks if instance is created"""
        self.assertTrue(isinstance(self.u1, User))
        self.assertTrue(isinstance(self.b1, Book))
        self.assertTrue(isinstance(self.o1, Order))
        self.assertTrue(isinstance(self.oi1, OrderItem))
        self.assertEqual(True, self.u1 in User.objects.all()) 
        self.assertEqual(True, self.b1 in Book.objects.all())
        self.assertEqual(True, self.o1 in Order.objects.all())
        self.assertEqual(True, self.oi1 in OrderItem.objects.all())

    def test_attributs(self):
        """
        checks the attributes.
        """
        o1_attribs = ["order_id", "user_id",
                      "order_date", "total_amount"]
        oi1_attribs = ["order_id", "order_item_id",
                       "book", "quantity"]
        for o in o1_attribs:
            self.assertTrue(hasattr(self.o1, o))
        for o in oi1_attribs:
            self.assertTrue(hasattr(self.oi1, o))
        self.assertIsNotNone(self.o1_id)
        self.assertIsNotNone(self.oi1_id)

    def test_update(self):
        """
        tests update order and oerderItem.
        """
        #sub_q = OrderItem.objects.select_related("book").filter(order_item_id=self.oi1_id)
        up = Book.objects.filter(book_id=self.b1_id).all()
        q = OrderItem.objects.filter(book=self.b1_id).all()
        ta = up[0].price * q[0].quantity
        #OrderItem.objects.filter(order_item_id=self.oi1_id).update(unit_price=up[0].price)
        Order.objects.filter(order_id=self.o1_id).update(total_amount=ta)
        self.oi1.refresh_from_db()
        self.o1.refresh_from_db()
        #self.assertNotEqual(self.oi1.unit_price, 0)
        self.assertNotEqual(self.o1.total_amount, 0)
        #self.assertEqual(self.oi1.unit_price, 100.00)
        self.assertEqual(self.o1.total_amount, 300.00)

    def test_delete_book(self):
        """
        tests delete book if order item is deleted.
        """
        Book.objects.filter(book_id=self.b1_id).delete()
        self.assertFalse(Book.objects.filter(book_id=self.b1_id).all())
        self.assertFalse(OrderItem.objects.filter(book=self.b1_id).all())
        self.assertFalse(OrderItem.objects.filter(order_item_id=self.oi1_id).all())

    def test_delete_user(self):
        """
        tests delete user if order is deleted.
        """
        User.objects.filter(user_id=self.u1_id).delete()
        self.assertFalse(User.objects.filter(user_id=self.u1_id).all())
        self.assertFalse(Order.objects.filter(user_id=self.u1_id).all())
        self.assertFalse(Order.objects.filter(order_id=self.o1_id).all())

    def test_delete_order(self):
        """
        tests delete order if order item is deleted.
        """
        Order.objects.filter(order_id=self.o1_id).delete()
        self.assertFalse(Order.objects.filter(order_id=self.o1_id).all())
        self.assertFalse(OrderItem.objects.filter(order_id=self.o1_id).all())
        self.assertFalse(OrderItem.objects.filter(order_item_id=self.oi1_id).all())

    def test_delete_order_item(self):
        """
        tests delete order item.
        """
        OrderItem.objects.filter(order_item_id=self.oi1_id).delete()
        self.assertFalse(OrderItem.objects.filter(order_item_id=self.oi1_id).all())


class TestUserPreferences(TestCase):
    """
    tests for the UserPreferences.
    """


class TestReview(TestCase):
    """
    tests for the Review.
    """


class TestShoppingCart(TestCase):
    """
    tests for the ShoppingCart.
    """


class TestCartItem(TestCase):
    """
    tests for the CartItem.
    """


class TestSubscription(TestCase):
    """
    tests for the Subscription.
    """


class TestImage(TestCase):
    """
    tests for the Image.
    """
