# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string
import requests

class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid,
           given the Game's grid"""
        grid = self.grid.copy()
        for letter in word:
            if letter not in grid:
                return False
            grid.remove(letter)
        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']
