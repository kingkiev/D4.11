from django.contrib import admin
from p_library.models import Book, Author, Publish

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

	@staticmethod
	def author_full_name(obj):
		return obj.author.full_name

	list_display = ('title', 'author_full_name', 'publish_book')
	fields = ('ISBN', 'title', 'description', 'year_release', 'publish_book', 'author', 'price', 'copy_count')
	pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	pass

@admin.register(Publish)
class PublishAdmin(admin.ModelAdmin):
	pass