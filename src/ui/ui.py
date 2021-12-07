"""Yksinkertainen tekstikäyttöliittymä.
"""
from entities.blog import Blog
from entities.book import Book
from entities.podcast import Podcast
from entities.video import Video
from repositories.db_interface import DatabaseInterface
from ui.console_io import ConsoleIO

class UI:
    """Käyttöliittymäluokka, joka pystyy lisäämään ja
    näyttämään lukuvinkkejä.
    Args:
        data: tietokanta
        console_io: io
    """

    def __init__(self, database: DatabaseInterface, console_io: ConsoleIO):
        self._actions = {
            "a": "add a new item",
            "v": "view your items",
            "m": "mark item as read",
            "r": "remove an item",
            "q": "exit program"
        }
        self._types = {
            "1": "add book",
            "2": "add blog",
            "3": "add podcast",
            "4": "add video"
        }

        self._io = console_io
        self.database = database

    def start(self):
        """Käyttöliittymälooppi. Kysyy toimintaa ja kutsuu
        sen perusteella toiminnan käsittelevää metodia.
        """
        self._io.write("Reading tips")

        while True:
            self.print_actions()
            action = self._io.read()

            if action == "v":
                self._view_items()
            elif action == "a":
                self._add_item()
            elif action == "m":
                self._mark_item_as_read()
            elif action == "r":
                self._remove_item()
            elif action == "q":
                break
            else:
                self._io.write("\ncommand not found\n")
                continue

    def print_actions(self):
        """Tulostaa vaihtoehdot
        """
        self._io.write("\nchoose action:")
        for key, item in self._actions.items():
            self._io.write((f"\"{key}\": {item}"))


    def _add_item(self):
        """Kysyy lukuvinkin tiedot ja lisää sen listaan
        """
        self.print_types()

        selection = self._io.read("selected type: ")
        self.handle_type_command(selection)

    def _mark_item_as_read(self):
        """Kysyy lukuvinkin indeksin ja merkkaa luetuksi
        """
        for item in self.database.read():
            self._io.write(item)

        selection = int(self._io.read("\nmark which item as read?(Item number)\n"))
        self.database.mark_as_read(selection)

        self._io.write("\ndone")

    def print_types(self):
        """Kysyy lukuvinkin tyyppiä
       """
        self._io.write("\nwhich type you want to add?")
        for key, item in self._types.items():
            self._io.write((f"\"{key}\": {item}"))


    def handle_type_command(self, tip_type):
        """Käsittelee lukuvinkin tyypin ja kysyy tarvittavat tiedot
        """
        if tip_type == "1":
            self._ask_book()
        if tip_type == "2":
            self._ask_blog()
        if tip_type == "3":
            self._ask_podcast()
        if tip_type == "4":
            self._ask_video()

    def _ask_book(self):
        name = self._io.read("name of the book (mandatory): ")
        author = self._io.read("author (mandatory): ")
        isbn = self._io.read("ISBN (voluntary): ")
        description = self._io.read("description (voluntary): ")

        item = Book(name, author, isbn, description)
        self.database.add_book(item)

        self._io.write(f"\nitem {item} added \n")

    def _ask_blog(self):
        name = self._io.read("name of the blog (mandatory): ")
        author = self._io.read("author(mandatory): ")
        url = self._io.read("url (mandatory): ")
        title = self._io.read("title of blogpost (voluntary): ")
        description = self._io.read("description (voluntary): ")

        item = Blog(name, author, url, title, description)
        self.database.add_blog(item)

        self._io.write(f"\nitem {item} added \n")

    def _ask_podcast(self):
        name = ""
        while name == "":
            name = self._io.read("name of podcast (mandatory): ")

        episode = ""
        while episode == "":
            episode = self._io.read("name of episode (mandatory): ")

        url = self._io.read("url (voluntary): ")
        description = self._io.read("description (voluntary): ")

        podcast = Podcast(name, episode, url, description)
        self.database.add_podcast(podcast)

        self._io.write(f"\nitem {podcast} added\n")

    def _ask_video(self):
        name = ""
        while name == "":
            name = self._io.read("name of video (mandatory): ")

        url = ""
        while url == "":
            url = self._io.read("url (mandatory): ")

        channel = self._io.read("name of channel (voluntary): ")
        description = self._io.read("description (voluntary): ")

        video = Video(name, url, channel, description)
        self.database.add_video(video)

        self._io.write(f"\nitem {video} added\n")


    def _view_items(self):
        """Näyttää listan lukuvinkit
        """
        tip_type = int(self._io.read(
            "\nview which tips: \n1: book\n2: blog\n3: podcast\n4: video\n5: all\n"))

        self._io.write("")
        if tip_type == 5:
            for item in self.database.read():
                self._io.write(item)
            return

        type_helper = ["", "Book:", "Blog:", "Podcast:", "Video:"]
        for item in self.database.read():
            if item.split()[1] == type_helper[tip_type]:
                self._io.write(item)

    def _remove_item(self):
        """Poistaa yhden lukuvinkin
        """
        for item in self.database.read():
            self._io.write(item)

        try:
            index = int(self._io.read("\nClear which item?(Item number)\n"))
        except:
            self._io.write("Invalid selection")
            return

        self.database.remove_tip(index)
