from django.contrib import admin

from .models import Author, AuthorProfile, Book, BookInstance, Genre, Language


@admin.register(Genre)
class GenreModelAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Language)
class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ["name"]


class AuthorProfileInlineModelAdmin(admin.TabularInline):
    model = AuthorProfile


class BookInlineModelAdmin(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    list_display = ["first_name", "last_name", "date_of_birth", "date_of_death"]
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [AuthorProfileInlineModelAdmin, BookInlineModelAdmin]


@admin.register(AuthorProfile)
class AuthorProfileModelAdmin(admin.ModelAdmin):
    pass


class BooksInstanceInlineModelAdmin(admin.TabularInline):
    """Defines format of inline book instance insertion (used in BookAdmin)"""
    model = BookInstance


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    """Administration object for Book models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ['title', 'author', 'display_genre']
    inlines = [BooksInstanceInlineModelAdmin]


@admin.register(BookInstance)
class BookInstanceModelAdmin(admin.ModelAdmin):
    """Administration object for BookInstance models.
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ["id", "book", "status", 'borrower', "due_back"]
    list_filter = ["status", "due_back"]
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
