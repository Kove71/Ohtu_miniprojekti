import unittest
from entities.video import Video

class TestBlog(unittest.TestCase):
    """Testiluokka Book -luokalle
    """
    def test_full_imput_prints_correctly_with_full_info(self):
        """Testaa että luokka tulostuu oikein kun kaikkiin tietoihin annetaan jokin tulos
        """
        video = Video(
            12,
            "Crazy Stuff",
            "carzyland.tv/episode_12",
            "carzy Br0s",
            "Not for the light of Heart",
            "12-12-2021"
        )
        self.assertEqual(
            video.__str__(),
                f"\033[1;37;42mVideo {12: <50}\033[0;0;0m\n" \
                f"\033[0;32;47mName: \033[0;30;47m{'Crazy Stuff': <50}\033[0;0;0m\n" \
                f"URL: {'carzyland.tv/episode_12'}\n" \
                f"Channel: {'carzy Br0s'}\n" \
                f"Description: " \
                f"{'Not for the light of Heart'}\033[0;0;0m\n" \
                f"Watched: {'12-12-2021'}\n"
        )
        self.assertEqual(
            video.short_form(),
            f"Video {12}: {'Crazy Stuff'} url:{'carzyland.tv/episode_12'}"
        )
    
    def test_partial_imputs_prints_correctly(self):
        video = Video(
           12,
            "Crazy Stuff",
            "carzyland.tv/episode_12"
        )
        self.assertEqual(
            video.__str__(),
                f"\033[1;37;42mVideo {12: <50}\033[0;0;0m\n" \
                f"\033[0;32;47mName: \033[0;30;47m{'Crazy Stuff': <50}\033[0;0;0m\n" \
                f"URL: {'carzyland.tv/episode_12'}\n" \
                f"Channel: {'Unknown'}\n" \
                f"Description: " \
                f"{'None'}\033[0;0;0m\n" \
                f"Watched: {'Not watched'}\n"
    
        )
        self.assertEqual(
            video.short_form(),
            f"Video {12}: {'Crazy Stuff'} url:{'carzyland.tv/episode_12'}"
        )