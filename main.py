"""
Zadanie: biblioteka filmów
A teraz coś z zupełnie innej beczki. Wyobraź sobie, że tworzysz system obsługujący bibliotekę filmów i seriali.
Wykorzystaj wiedzę na temat programowania obiektowego i napisz program, który spełnia następujące założenia:

Jest w stanie przechowywać informacje na temat filmów, które znajdują się w systemie.
Każdy film powinien mieć następujące atrybuty:
Tytuł
Rok wydania
Gatunek
Liczba odtworzeń
Umożliwia przechowywanie informacji na temat seriali. Każdy serial powinien mieć następujące atrybuty:
Tytuł
Rok wydania
Gatunek
Numer odcinka
Numer sezonu
Liczba odtworzeń
Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.
Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku,
np.: “The Simpsons S01E05” (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej,
natomiast po E - numer odcinka, również w zapisie dwucyfrowym).
Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.
Przechowuje filmy i seriale w jednej liście.
Dodatkowo:

Napisz funkcje get_movies oraz get_series, które będą filtrować listę i zwracać odpowiednio tylko filmy oraz
tylko seriale. Posortuj listę wynikową alfabetycznie.
Napisz funkcję search, która wyszukuje film lub serial po jego tytule.
Napisz funkcję generate_views, która losowo wybiera element z biblioteki,
a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
Napisz funkcję, która uruchomi generate_views 10 razy.
Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki.

Dla chętnych: dodaj do funkcji parametr content_type, którym wybierzesz czy mają zostać pokazane filmy, czy seriale.
Zadania dla chętnych
Napisz funkcję, która za pomocą pętli dodaje pełne sezony seriali do biblioteki. Funkcja powinna przyjmować parametry
takie jak: tytuł serialu, rok wydania, gatunek, numer sezonu, liczba odcinków do dodania.
Do klasy reprezentującej serial, dopisz funkcję zewnętrzną, która wyświetla liczbę odcinków
danego serialu dostępnych w bibliotece.
Niech program po uruchomieniu działa w następujący sposób:

Wyświetli na konsoli komunikat Biblioteka filmów.
Wypełni bibliotekę treścią.
Wygeneruje odtworzenia treści za pomocą funkcji generate_views.
Wyświetli na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>,
gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
Wyświetli listę top 3 najpopularniejszych tytułów.
Kod udostępnij na Githubie i wyślij link do Mentora.
"""
import dill
import random

GENRE = {
    'A': 'Akcja',
    'K': 'Komedia',
    'D': 'Dramat',
    'H': 'Horror',
    'S': 'Sci-Fi',
    'F': 'Fantastyka'
}

YN = [
    'Y',
    'N'
]

TEXT = [
    'Czy chcesz dodać{0} pozycję? Y/N: ',
    'Czy chcesz wyświetlić{0} Filmy/Seriale? Y/N: '
]


class Movie:
    def __init__(self, title, release_year, genre, viewed=0):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        # Variable
        self.viewed = viewed

    def play(self):
        self.viewed += 1

    def __str__(self):
        return f'{self.title} ({self.release_year}) '


class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season}E{self.episode}'


def get_movies():
    only_movies = []
    for record in library:
        if isinstance(record, Series):
            continue
        else:
            only_movies.append(record)
    sorted_by_title = sorted(only_movies, key=lambda movie: movie.title)
    for record in sorted_by_title:
        print(record)


def get_series():
    only_series = []
    for record in library:
        if isinstance(record, Series):
            only_series.append(record)
    sorted_by_title = sorted(only_series, key=lambda movie: movie.title)
    for record in sorted_by_title:
        print(record)


def search():
    z = input('Jakiego Filmu/Serialu szukasz? Podaj tytuł: ')
    found = False
    for i in library:
        if i.title.upper() == str(z).upper():
            searched = i
            found = True
    if found:
        while True:
            x = input(f'Znalazłem {searched} czy chcesz wyświetlić? Y/N: ')
            if check_dict(x, YN):
                if str(x).upper() == "Y":
                    searched.play()
                    print('Tytuł został odtworzony - viewed +1')
    else:
        print('Nie znalazłem takiego tytułu.')


def generate_views():
    pick_title = random.randint(0, len(library) - 1)
    library[pick_title].viewed += random.randint(1, 100)
    for i in range(0, len(library)):
        if i == 0:
            with open('database.dill', 'wb') as handle:
                dill.dump(library[i], handle, protocol=dill.HIGHEST_PROTOCOL)
        else:
            with open('database.dill', 'ab') as handle:
                dill.dump(library[i], handle, protocol=dill.HIGHEST_PROTOCOL)


def g10():
    pass


def top_titles(content_type):
    content_type

    pass


def choose():
    x = input('Film/Serial - F/S: ')
    generate(x)


def check_dict(x, y):
    if str(x).upper() in y:
        return True
    else:
        return False


def generate(x):
    title = input('Podaj tytuł filmu: ')
    release_year = input(f'Podaj rok filmu ({title}): ')
    while True:
        check_genre = str(input(
            f'Podaj gatunek filmu ({title}) - (H)orror / (S)ci-Fi / (F)antastyka / (A)kcja / (D)ramat / (K)omedia: ')).upper()
        if check_dict(check_genre, GENRE):
            genre = GENRE[check_genre]
            break
    if str(x).upper() == 'S':
        episode = input('Podaj numer odcinka: ')
        season = input('Podaj numer sezonu: ')
        new = Series(episode, season, title, release_year, genre)
    else:
        new = Movie(title, release_year, genre)
    library.append(new)


def next_operation(y, operation_type):
    while True:
        x = input(TEXT[operation_type].format(y))
        if check_dict(x, YN):
            if str(x).upper() == 'N':
                next_bool = False
            else:
                next_bool = True
            return next_bool


def add_new():
    choose_bool = next_operation('', 0)
    while choose_bool:
        choose()
        choose_bool = next_operation(' kolejną', 0)

    choose_bool = next_operation('', 1)
    if choose_bool:
        print('Dostępne filmy: ')
        get_movies()
        print('\n')
        print('Dostępne seriale: ')
        get_series()
        print('\n')


def popular():
    print('Najpopularniejsze tytuły: ')
    by_popularity = sorted(library, key=lambda movie: movie.viewed, reverse=True)
    for i in range(0, 3):
        print(f"{i + 1}. {by_popularity[i]}")


if __name__ == "__main__":
    print('Biblioteka filmów')
    library = [Movie('Szklana Pułapka', 1988, 'Akcja'), Movie('Przekręt', 2000, 'Komedia'), Movie('Joker', 2019, 'Dramat'), Series('01', '01', 'South Park', 1996, 'Komedia')]
    add_new()
    search()
    generate_views()
    popular()
