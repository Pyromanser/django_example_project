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
    list_display = ["first_name", "last_name", "date_of_birth", "date_of_death"]
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [AuthorProfileInlineModelAdmin, BookInlineModelAdmin]


@admin.register(AuthorProfile)
class AuthorProfileModelAdmin(admin.ModelAdmin):
    pass


class BooksInstanceInlineModelAdmin(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']
    inlines = [BooksInstanceInlineModelAdmin]


@admin.register(BookInstance)
class BookInstanceModelAdmin(admin.ModelAdmin):
    list_display = ["id", "book", "status", "due_back"]
    list_filter = ["status", "due_back"]
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
