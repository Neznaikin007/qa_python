import pytest


class TestBooksCollector:


    #добавление несколько книг без жанра, используя параметризацию
    @pytest.mark.parametrize('name',
                             ['Анжелика', 'Путь Абая']
                             )
    def test_add_new_books_in_dict_added(self, books_collector, name):
        books_collector.add_new_book(name)
        expected_dict = books_collector.books_genre.keys()
        assert name in expected_dict
    #добавление несколько книг с жанром
    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Терминатор', 'Фантастика'],
                                 ['Микки маус', 'Мультфильмы']
                             ])
    def test_set_book_genre_in_dict_added(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert genre in books_collector.books_genre.values()
    #Проверка жанра
    def test_get_book_genre_dict_is_received(self, books_collector):
        books_collector.add_new_book('Микки маус')
        books_collector.set_book_genre('Микки маус', 'Мультфильмы')
        assert books_collector.get_book_genre('Микки маус') == 'Мультфильмы'
    #Добавление книги без жанра
    def test_get_book_genre_no_genre_added(self, books_collector):
        books_collector.add_new_book('Терминатор')
        assert books_collector.get_book_genre('Терминатор') == ''
    #Список с жанром книг
    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Омен', 'Ужасы'],
                                 ['Стражы галактики', 'Фантастика']
                             ])
    def test_get_books_with_specific_genre_books_received(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_books_with_specific_genre(genre) == [name]
    # проверка словаря books_genre
    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Укол зонтиком', 'Комедии'],
                                 ['Русалочка', 'Мультфильмы'],
                                 ['Дэдпулл', 'Фантастика'],
                                 ['38 попугаев', 'Мультфильмы'],
                                 ['Крик', 'Ужасы'],
                                 ['Странные игры', 'Детективы']
                             ])
    def test_get_books_genre_books_genre_received(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_books_genre() == {name: genre}
    #проверка книг детям
    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Маска', 'Комедии'],
                                 ['Виннипух', 'Мультфильмы'],
                                 ['Машина времени', 'Фантастика']
                             ])
    def test_get_books_for_children_book_is_received(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_books_for_children() == [name]
    #проверка книг детям "неподходящих"
    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Дракула', 'Ужасы'],
                                 ['Концы в воду', 'Детектив']
                             ])
    def test_get_books_for_children_book_is_not_received(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_books_for_children() != [name]
    #проверка добавление в избранное
    def test_add_book_in_favorites_in_list_is_added(self, books_collector):
        name = 'Анжелика'
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        favorite_books = books_collector.get_list_of_favorites_books()
        assert name in favorite_books
    #проверка удаления
    def test_delete_book_from_favorites_book_is_deleted(self, books_collector):
        name = 'Анжелика'
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        books_collector.delete_book_from_favorites(name)
        assert name not in books_collector.favorites
    #проверка избранного
    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Шерлок','Детектив'],
                                 ['Алиса','Фантастика']
                             ])
    def test_get_list_of_favorites_books_have_books(self, books_collector, genre, name):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        books_collector.add_book_in_favorites(name)
        assert name in books_collector.get_list_of_favorites_books()