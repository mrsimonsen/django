from django.test import TestCase

from catalog.models import Author, Genre, Language, Book, BookInstance

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

# test labels
    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

# Test lenghts

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

# Test custom methods

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals('/catalog/author/1', author.get_absolute_url())

class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name='Testing')

    def test_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name(self):
        genre = Genre.objects.get(id=1)
        expected_object_name = genre.name
        self.assertEquals(expected_object_name, str(genre))

    def test_name_help_text(self):
        genre = Genre.objects.get(id=1)
        recieved = genre._meta.get_field('name').help_text
        self.assertEquals('Enter a book genre (e.g. Science Fiction)', recieved)


class LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Language.objects.create(name='Klingon')

    def test_name_label(self):
        lan = Language.objects.get(id=1)
        field_label = lan._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        lan = Language.objects.get(id=1)
        max_length = lan._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name(self):
        lan = Language.objects.get(id=1)
        expected_object_name = lan.name
        self.assertEquals(expected_object_name, str(lan))

    def test_name_help_text(self):
        lan = Language.objects.get(id=1)
        recieved = lan._meta.get_field('name').help_text
        self.assertEquals("Enter the book's written languague", recieved)

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name='Genre 2')
        Book.objects.create(
            title="Test Book",
            summary="This is a test summary.",
            isbn="1234567890123"
            )
        Book.objects.get(id=1).genre.set(
        (Genre.objects.create(name='Genre 1'),
        Genre.objects.create(name='Genre 2')))

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')

    def test_summary_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('summary').max_length
        self.assertEquals(max_length, 1000)

    def test_summary_help_text(self):
        book = Book.objects.get(id=1)
        recieved = book._meta.get_field('summary').help_text
        self.assertEquals("Enter a brief description of the book", recieved)

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label, 'ISBN')

    def test_isbn_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('isbn').max_length
        self.assertEquals(max_length, 13)

    def test_isbn_help_text(self):
        book = Book.objects.get(id=1)
        recieved = book._meta.get_field('isbn').help_text
        self.assertEquals('13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', recieved)

    def test_object_name(self):
        book = Book.objects.get(id=1)
        expected_object_name = book.title
        self.assertEquals(expected_object_name, str(book))

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEquals('/catalog/book/1', book.get_absolute_url())

    def test_display_genre(self):
        book = Book.objects.get(id=1)
        self.assertEquals('Genre 1, Genre 2', book.display_genre())


class BookInstanceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='test title')
        BookInstance.objects.create(id=1,imprint='test imprint', due_back='1111-11-11', status='m', book=Book.objects.get(id=1))

    def test_imprint_label(self):
        bi = BookInstance.objects.get(id=1)
        label = bi._meta.get_field('imprint').verbose_name
        self.assertEquals(label, 'imprint')

    def test_book_label(self):
        bi = BookInstance.objects.get(id=1)
        label = bi._meta.get_field('book').verbose_name
        self.assertEquals(label, 'book')

    def test_imprint_max_length(self):
        bi = BookInstance.objects.get(id=1)
        max = bi._meta.get_field('imprint').max_length
        self.assertEquals(max, 200)

    def test_due_back_label(self):
        bi = BookInstance.objects.get(id=1)
        label = bi._meta.get_field('due_back').verbose_name
        self.assertEquals(label, 'due back')

    def test_status_label(self):
        bi = BookInstance.objects.get(id=1)
        label = bi._meta.get_field('status').verbose_name
        self.assertEquals(label, 'status')

    def test_status_max_length(self):
        bi = BookInstance.objects.get(id=1)
        max = bi._meta.get_field('status').max_length
        self.assertEquals(max, 1)

    def test_object_name(self):
        bi = BookInstance.objects.get(id=1)
        expected_object_name = f'{bi.id} ({bi.book.title})'
        self.assertEquals(expected_object_name, str(bi))

    def test_is_overdue(self):
        bi = BookInstance.objects.get(id=1)
        self.assertEquals(True, bi.is_overdue)
