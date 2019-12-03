from django.shortcuts import render

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre, Language

def index(request):
	'''View function for home page of site.'''

	# Generate counts of some of the main objects
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()

	# Available book s(status = 'a')
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()

	# The 'all()' is implied by default.
	num_authors = Author.objects.count()

	num_sgenre = Genre.objects.filter(name__icontains="fan").count()
	num_sinstance = BookInstance.objects.filter(book__genre__name__icontains="fan").count()

	context = {
		'num_books' : num_books,
		'num_instances' : num_instances,
		'num_instances_available' : num_instances_available,
		'num_authors' : num_authors,
		'num_sgenre': num_sgenre,
		'num_sinstance': num_sinstance,
	}

	# Render the HTML template index.html with the data in the context variable
	return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
	model = Book

class BookDetailView(generic.DetailView):
	model = Book
