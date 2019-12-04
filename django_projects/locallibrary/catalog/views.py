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

	# Number of visits to this view, as counted in the session variable.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	context = {
		'num_books' : num_books,
		'num_instances' : num_instances,
		'num_instances_available' : num_instances_available,
		'num_authors' : num_authors,
		'num_sgenre': num_sgenre,
		'num_sinstance': num_sinstance,
		'num_visits': num_visits,
	}

	# Render the HTML template index.html with the data in the context variable
	return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
	model = Book
	paginate_by = 10

class BookDetailView(generic.DetailView):
	model = Book

class AuthorListView(generic.ListView):
	model = Author
	paginate_by = 10

class AuthorDetailView(generic.DetailView):
	model = Author

from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class AllLoanedBooksListView(LoginRequiredMixin,generic.ListView):
	'''Generic class-based view listing all books on loan and the user that has them.'''
	model = BookInstance
	template_name = 'catalog/bookinstance_list_borrowed_all.html'
	paginate_by = 10
	permission_required = 'catalog.can_mark_returned'

	def get_queryset(self):
		return BookInstance.objects.filter(status__exact='o').order_by('due_back')
