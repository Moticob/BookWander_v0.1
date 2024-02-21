
from django.core.management.base import BaseCommand
from Wanderapp.models import Book, Genre
from django.utils import timezone


class Command(BaseCommand):
    help = "Populates the database with some testing data."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Started database population process..."))
        if Book.books.filter(title="The shining").exists():
            self.stdout.write(self.style.SUCCESS("Database has already been populated. Cancelling the operation."))
            return
        fiction = Genre.objects.create(genre_name="Fiction", slug="Fic")
        drama = Genre.objects.create(genre_name="Drama", slug="Dr")
        programming = Genre.objects.create(genre_name="Programming", slug="Prg")
        manga = Genre.objects.create(genre_name="Manga", slug="Mng")
        fiction.save()
        drama.save()
        programming.save()
        manga.save()
        shining = Book.books.create(
           title="The Shining",
           slug="The_Shining",
           author="Stephen King",
           genre_name=fiction,
           publication_date = timezone.now(),
           price = 100.00,
           cover_image_url="images/the_shining.jpg",
           description="Jack Torrance's new job at the Overlook Hotel is the perfect chance for a fresh start.\
               As the off-season caretaker at the atmospheric old hotel, he'll have plenty of time to spend\
               reconnecting with his family and working on his writing. But as the harsh winter weather sets\
                   in, the idyllic location feels ever more remote...and more sinister. And the only one to\
                       notice the strange and terrible forces gathering around the Overlook is Danny Torrance,\
                           a uniquely gifted five-year-old."
        )
        shining.save()
        
        azkaban = Book.books.create(
           title="Harry Potter and the Prisoner of Azkaban",
           slug="HP_azkaban",
           author="J.K. Rowling",
           genre_name=fiction,
           publication_date = timezone.now(),
           price = 130.00,
           cover_image_url="images/azkaban.jpg",
           description="JWelcome to the Knight Bus, emergency transport for the\
               stranded witch or wizard. Just stick out your wand hand, step on\
                   board and we can take you anywhere you want to go. When the Knight Bus\
                       crashes through the darkness and screeches to a halt in front of him,\
                           it is the start of another far from ordinary year at Hogwarts for\
                               Harry Potter. Sirius Black, escaped mass-murderer and follower\
                                   of Lord Voldemort, is on the run - and they say he is coming\
                                       after Harry. In his first ever Divination class,\
                                           Professor Trelawney sees an omen of death in Harry s\
                                               tea leaves... But perhaps most terrifying of\
                                                   all are the Dementors patrolling the school\
                                                       grounds, with their soul-sucking kiss..."
        )
        azkaban.save()
        
        vagabond = Book.books.create(
           title="Vagabond volume 1",
           slug="Vagabond001",
           author="Takehiko Inoue",
           genre_name=manga,
           publication_date = timezone.now(),
           price = 90.50,
           cover_image_url="images/vagabond.jpg",
           description="Preoccupied with a single leaf...\
               you won't see the tree. Preoccupied with a single tree...\
                   you'll miss the entire forest. Don't be preoccupied with a single spot.\
                       See everything in it's entirety... effortlessly. That is what\
                           it means to truly see."
        )
        vagabond.save()
        pr = Book.books.create(
           title="Python Data Science Handbook",
           slug="Python_Data_Science_Handbook",
           author="Jake VanderPlas",
           genre_name=programming,
           publication_date = timezone.now(),
           price = 230.00,
           cover_image_url="images/py.jpg",
           description="For many researchers, Python\
               is a first-class tool mainly because of\
                   its libraries for storing, manipulating,\
                       and gaining insight from data. Several\
                           resources exist for individual pieces\
                               of this data science stack, but only\
                                   with the Python Data Science Handbook\
                                       do you get them all--IPython, NumPy,\
                                           Pandas, Matplotlib, Scikit-Learn,\
                                               and other related tools."
        )
        pr.save()
        
        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))