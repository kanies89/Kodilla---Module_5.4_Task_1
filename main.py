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
import random
from datetime import date

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

UNITS = {
    '1': ['jeden', 'pierwszy'],
    '2': ['dwu', 'drugi'],
    '3': ['trzy', 'trzeci'],
    '4': ['czter', 'czwarty'],
    '5': ['pięt', 'piąty'],
    '6': ['szes', 'szósty'],
    '7': ['siedem', 'siódmy'],
    '8': ['osiem', 'ósmy'],
    '9': ['dzięwięt', 'dziewiąty'],
    '10': 'dziesiąty'
}


def change_to_word(to_change):
    if to_change[0] == '0':
        word = UNITS[to_change[1]][1]
    elif to_change == '10':
        word = UNITS[to_change]
    elif to_change[0] == '1':
        word = UNITS[to_change[1]][0] + "nasty"
    else:
        if to_change[1] == '0':
            word = UNITS[to_change[0]][0] + "dziesty"
        else:
            word = UNITS[to_change[0]][0] + "dziesty " + UNITS[to_change[1]][1]
    return word


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
        return f'{self.title} - S{self.season}E{self.episode} - sezon {change_to_word(self.season)}, odcinek {change_to_word(self.episode)}.'


def get_movies():
    return get(Movie)


def get_series():
    return get(Series)


def get(ms_type):
    filtered_library = []
    for record in library:
        if type(record) == ms_type:
            filtered_library.append(record)
    sorted_by_title = sorted(filtered_library, key=lambda movie: movie.title)
    return sorted_by_title


def search():
    z = input('Jakiego Filmu/Serialu szukasz? Podaj tytuł: ')
    found = False
    for i in library:
        if i.title.upper() == z.upper():
            searched = i
            found = True
            break
    if found:
        while True:
            x = input(f'Znalazłem {searched} czy chcesz wyświetlić? Y/N: ')
            if check_dict(x, YN):
                if x.upper() == "Y":
                    searched.play()
                    print('Tytuł został odtworzony - viewed +1')
                else:
                    break
    else:
        print('Nie znalazłem takiego tytułu.')


def generate_views():
    pick_title = random.choice(library)
    pick_title.viewed += random.randint(1, 100)


def g10():
    for i in range(10):
        generate_views()


def choose(lib):
    x = input('Film/Serial - F/S: ')
    return generate(x, lib)


def check_dict(x, y):
    return x.upper() in y


def check_int(x):
    while True:
        try:
            w = int(x)
        except ValueError:
            w = input('Podaj liczbę od 1 do 99: ')
        else:
            if w in range(1, 100):
                return w
            else:
                x = input('Podaj liczbę od 1 do 99: ')


def generate(x, lib):
    title = input('Podaj tytuł: ')
    release_year = input(f'Podaj rok premiery ({title}): ')
    while True:
        check_genre = input(
            f'Podaj gatunek dla tytułu ({title}) - (H)orror / (S)ci-Fi / (F)antastyka / (A)kcja / (D)ramat / (K)omedia: ').upper()
        if check_dict(check_genre, GENRE):
            genre = GENRE[check_genre]
            break
    if x.upper() == 'S':
        episode = str(check_int(input('Podaj numer odcinka: '))).zfill(2)
        season = str(check_int(input('Podaj numer sezonu: '))).zfill(2)
        new = Series(episode, season, title, release_year, genre)
    else:
        new = Movie(title, release_year, genre)
    lib.append(new)
    return lib

def next_operation(y, operation_type):
    while True:
        x = input(TEXT[operation_type].format(y))
        if check_dict(x, YN):
            return x.upper() == 'Y'


def add_new(lib):
    choose_bool = next_operation('', 0)
    while choose_bool:
        choose(lib)
        choose_bool = next_operation(' kolejną', 0)

    choose_bool = next_operation('', 1)
    if choose_bool:
        print('Dostępne filmy: ')
        [print(item) for item in get_movies()]
        print('\n')
        print('Dostępne seriale: ')
        [print(item) for item in get_series()]
        print('\n')


def top_titles(library_list):
    by_popularity = sorted(library_list, key=lambda movie: movie.viewed, reverse=True)
    most_popular = []
    for i in range(3):
        most_popular.append(by_popularity[i])
    return most_popular


if __name__ == "__main__":
    print('Biblioteka filmów')
    library = [Movie('Szklana Pułapka', 1988, 'Akcja'), Movie('Przekręt', 2000, 'Komedia'),
               Movie('Joker', 2019, 'Dramat'), Series('01', '01', 'South Park', 1996, 'Komedia')]
    add_new(library)
    search()
    generate_views()
    g10()

    print(f'\nNajpopularniejsze filmy i seriale dnia {date.today().day}-{date.today().month}-{date.today().year}: ')
    [print(f"{i + 1}. {top_titles(library)[i]}") for i in range(3)]
