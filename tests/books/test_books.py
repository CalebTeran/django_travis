import pytest
from library.books.models import *

@pytest.mark.django_db
def test_author_name():
        author = Author.objects.create(name='J.K.', last_name='rowling')
        print('Author name>>>', author.name)
        assert author.last_name == 'rowling'