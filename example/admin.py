from django.contrib import admin

from .models import Genre, Language, Book, BookInstance, Author, AuthorProfile


@admin.register(Genre)
class GenreModelAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Language)
class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ["name"]


class AuthorProfileInlineModelAdmin(admin.TabularInline):
    model = AuthorProfile


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "date_of_birth", "date_of_death"]
    inlines = [AuthorProfileInlineModelAdmin]


@admin.register(AuthorProfile)
class AuthorProfileModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(BookInstance)
class BookInstanceModelAdmin(admin.ModelAdmin):
    list_display = ["id", "book", "status", "due_back"]
    list_filter = ["status"]
