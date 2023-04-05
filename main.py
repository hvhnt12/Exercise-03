# TASK1
def count_vowels(text):
    if not isinstance(text, str):
        return 42
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count


# TASK2
def hamming(text1, text2):
    if len(text1) != len(text2):
        return 0
    hamming_dist = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            hamming_dist += 1
            return hamming_dist


# TASK3
from abc import ABC


class Vehicle(ABC):
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}"


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return f"{super().__str__()}, Doors: {self.doors}"


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return f"{super().__str__()}, Passengers: {self.passengers}"


# TASK4
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f" {self.name}, {self.author}"


# TASK5

class BookShelf:
    def __init__(self):
        self.books = []

    def add_book_list(self, books):
        for book in books:
            if isinstance(book, Book):
                self.books.append(book)

    def books_by_author(self, author):
        books_by_author = []
        for book in self.books:
            if book.author == author:
                books_by_author.append(book.name)
        return books_by_author

    def get_books(self):
        books = []
        for book in self.books:
            books.append(book.name)
        return books

    def clear_shelf(self):
        self.books = []
