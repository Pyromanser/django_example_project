import uuid
from datetime import date

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(_("name"), max_length=200, help_text=_("Enter a book genre (e.g. Scince fiction, French Poentry etc.)"))

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(_("name"), max_length=50, help_text=_("Enter the book's natural language (e.g. English, French etc.)"))

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(_("title"), max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(_("summary"), max_length=1000, help_text=_("Enter a brief description of the book"))
    isnb = models.CharField("ISBN", max_length=13, help_text=_("13 character ISBN number"))
    genre = models.ManyToManyField(Genre, verbose_name=_("genre"), help_text=_("Select a genre for this book"))
    language = models.ForeignKey("Language", verbose_name=_("language"), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):

    class LoanStatus(models.IntegerChoices):
        MAINTENANCE = 1, _('Maintenance')
        ON_LOAN = 2, _('On loan')
        AVAILABLE = 3, _("Available")
        RESERVED = 4, _("Reserved")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text=_("Unique ID for this particular book across whole library"))
    book = models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(_("imprint"), max_length=200, help_text=_("Enter publisher trade name"))
    due_back = models.DateField(_("due back"), null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=LoanStatus.choices, default=LoanStatus.MAINTENANCE, blank=True, help_text=_('Book availability'))
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        return f"{self.id} ({self.book.title})"


class Author(models.Model):
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)
    date_of_birth = models.DateField(_("date of birth"), null=True, blank=True)
    date_of_death = models.DateField(_("date of death"), null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])


class AuthorProfile(models.Model):
    author = models.OneToOneField("Author", on_delete=models.CASCADE)
    about = models.TextField(_("about"), max_length=1000, help_text=_("Author bio"))

    def __str__(self):
        return f"{self.author.last_name} {self.author.first_name} Profile"
