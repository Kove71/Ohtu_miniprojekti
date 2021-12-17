"""Testataan blog-luokkaa
"""
import unittest
from entities.blog import Blog

class TestBlog(unittest.TestCase):
    """Testiluokka Blog -luokalle
    """
    def test_full_imput_prints_correctly_with_full_info(self):
        """Testaa että luokka tulostuu oikein kun kaikkiin tietoihin annetaan jokin tulos
        """
        blog = Blog(
            12,
            "My Lyfe",
            "Jhon B. Elton II",
            "blog.com",
            "Random happenings",
            "Not for the light of Heart",
            "12-12-2021"
        )
        self.assertEqual(
            blog.__str__(),
                f"\033[1;37;41mBlog {12: <51}\033[0;0;0m\n" \
                f"\033[0;31;47mName: \033[0;30;47m{'My Lyfe': <50}\033[0;0;0m\n" \
                f"Author: {'Jhon B. Elton II'}\n" \
                f"Blogpost title: {'Random happenings'}\n" \
                f"URL: {'blog.com'}\n" \
                f"Description: {'Not for the light of Heart'}\n" \
                f"Read: {'12-12-2021'}\n"
        )
        self.assertEqual(
            blog.short_form(),
            f"Blog {12}: {'My Lyfe'} by {'Jhon B. Elton II'}"
        )

    def test_partial_imputs_prints_correctly(self):
        """Testataan, että tulostaa oikein, kun ei anneta kaikkia tietoja
        """
        blog = Blog(
            12,
            "My Lyfe",
            "Jhon B. Elton II",
            "blog.com"
        )
        self.assertEqual(
            blog.__str__(),
                f"\033[1;37;41mBlog {12: <51}\033[0;0;0m\n" \
                f"\033[0;31;47mName: \033[0;30;47m{'My Lyfe': <50}\033[0;0;0m\n" \
                f"Author: {'Jhon B. Elton II'}\n" \
                f"Blogpost title: {'Unknown'}\n" \
                f"URL: {'blog.com'}\n" \
                f"Description: {'None'}\n" \
                f"Read: {'Not read'}\n"
        )
        self.assertEqual(
            blog.short_form(),
            f"Blog {12}: {'My Lyfe'} by {'Jhon B. Elton II'}"
        )
