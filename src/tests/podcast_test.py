import unittest
from entities.podcast import Podcast

class TestPodcast(unittest.TestCase):
    """Testiluokka Book -luokalle
    """
    def test_full_imput_prints_correctly_with_full_info(self):
        """Testaa että luokka tulostuu oikein kun kaikkiin tietoihin annetaan jokin tulos
        """
        podcast = Podcast(
            12,
            "Tales of Dark",
            "Hiding in the Shadows",
            "http//somewhere.com/Episode_12",
            "Scary Stuff",
            "12-12-2021"
        )
        self.assertEqual(
            podcast.__str__(),
                f"\033[1;37;45mPodcast {12: <48}\033[0;0;0m\n" \
                f"\033[0;35;47mName: \033[0;30;47m{'Tales of Dark': <50}\033[0;0;0m\n" \
                f"Episode: {'Hiding in the Shadows'}\n" \
                f"URL: {'http//somewhere.com/Episode_12'}\n" \
                f"Description: " \
                f"{'Scary Stuff'}\033[0;0;0m\n" \
                f"Listened: {'12-12-2021'}\n"

        )
        self.assertEqual(
            podcast.short_form(),
            f"Podcast {12}: {'Tales of Dark'} episode {'Hiding in the Shadows'}"
        )
    
    def test_partial_imputs_prints_correctly(self):
        podcast = Podcast(
            12,
            "Tales of Dark",
            "Hiding in the Shadows"
        )
        self.assertEqual(
            podcast.__str__(),
                f"\033[1;37;45mPodcast {12: <48}\033[0;0;0m\n" \
                f"\033[0;35;47mName: \033[0;30;47m{'Tales of Dark': <50}\033[0;0;0m\n" \
                f"Episode: {'Hiding in the Shadows'}\n" \
                f"URL: {'Unknown'}\n" \
                f"Description: " \
                f"{'None'}\033[0;0;0m\n" \
                f"Listened: {'Not listened'}\n"
        )
        self.assertEqual(
            podcast.short_form(),
            f"Podcast {12}: {'Tales of Dark'} episode {'Hiding in the Shadows'}"
        )