"""Testataan book-luokkaa"""
import unittest
from entities.book import Book

class TestBook(unittest.TestCase):
    """Testiluokka Book -luokalle
    """
    def test_full_imput_prints_correctly_with_full_info(self):
        """Testaa että luokka tulostuu oikein kun kaikkiin tietoihin annetaan jokin tulos
        """
        book = Book(
            12,
            "Thunder diary",
            "Jhon B. Elton II",
            "ISBN-1891202818201",
            "A long forgotten masterpiece",
            "12-12-2021"
        )
        self.assertEqual(
            book.__str__(),
            f"\033[1;37;44mBook {12: <51}\033[0;0;0m\n" \
            f"\033[0;34;47mName: \033[0;30;47m{'Thunder diary': <50}\033[0;0;0m\n" \
            f"Author: {'Jhon B. Elton II'}\n" \
            f"ISBN: {'ISBN-1891202818201'}\n" \
            f"Description: " \
            f"{'A long forgotten masterpiece'}\033[0;0;0m\n" \
            f"Read: {'12-12-2021'}\n"
        )
        self.assertEqual(
            book.short_form(),
            f"Book {12}: {'Thunder diary'} by {'Jhon B. Elton II'}"
        )

    def test_partial_imputs_prints_correctly(self):
        """Testataan, että tulostaa oikein, kun ei anneta kaikkia tietoja
        """
        book = Book(
            12,
            "Thunder diary",
            "Jhon B. Elton II"
        )
        self.assertEqual(
            book.__str__(),
            f"\033[1;37;44mBook {12: <51}\033[0;0;0m\n" \
            f"\033[0;34;47mName: \033[0;30;47m{'Thunder diary': <50}\033[0;0;0m\n" \
            f"Author: {'Jhon B. Elton II'}\n" \
            f"ISBN: {'Unknown'}\n" \
            f"Description: " \
            f"{'None'}\033[0;0;0m\n" \
            f"Read: {'Not read'}\n"
        )
        self.assertEqual(
            book.short_form(),
            f"Book {12}: {'Thunder diary'} by {'Jhon B. Elton II'}"
        )
