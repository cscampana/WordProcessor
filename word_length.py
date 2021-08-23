#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Word Processor

In this Python application, the user inputs a file containing one word per line in a txt format,
and the program counts the length and the frequency of each word.
We use an object with a custom hash function to calculate the key in a dictionary, and read from it to a bar plot.

"""

# 3rd party libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

__author__ = "Caike Salles Campana"
__license__ = "CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"
__version__ = "0.1"
__maintainer__ = "Caike Salles Campana"
__email__ = "csallesc@ucsd.edu"
__status__ = "Development"


def load_words(file):
    """" Function used to load the file, it uses a try-except block to handle exceptions"""
    try:
        with open(file) as word_dictionary:
            words = set(word_dictionary.read().split())
        return words
    except FileNotFoundError:
        print("Not able to open the file!")
        main()


class WordClassifier:
    """
    This class is used for handling the words, at the moment its main purpose is to handle the custom
    hash function. But more word manipulation will be added in future releases.
    """

    def __init__(self, word):
        """Constructor that initializes the variable word."""
        self.word = word

    def __hash__(self):
        """Overrides the default implementation to aid in the word length frequency"""
        return len(self.word)

    def __eq__(self, other):
        """Custom equals function for future releases"""
        if not isinstance(other, self.__class__):
            return NotImplemented
        elif self.word == other.word:
            return True

        return False


def main():
    """
    Main function used to provide support for the code, currently it creates the logic behind the
    terminal user interface, provides the method calling and basic logic behind the word length counter
    and displays the graph with the result.
    """
    print("Welcome to Word length frequency counter")

    # Input treatment
    while True:
        file = input("Please input the file that contain the words: ")
        if file.strip().isdigit():
            continue
        else:
            break

    result = dict([(word, WordClassifier(word).__hash__()) for word in load_words(file)])

    frequency = {}
    for value in result.values():
        frequency[value] = frequency.get(value, 0) + 1

    print("The maximum length of a word is {} characters".format(max(frequency)))
    print("The minimum length of a word is {} characters".format(min(frequency)))
    print("Most words are {} characters in length".format(max(frequency.keys(), key=lambda r: frequency[r])))

    # Plotting
    frequency_df = pd.DataFrame.from_dict(frequency, orient='index', columns=["length"])
    sns.set_theme(font_scale=1.7, style="darkgrid")
    fig, ax = plt.subplots()
    fig.set_size_inches(17.7, 10)

    sns.barplot(data=frequency_df.reset_index(), x="index", y="length", palette="magma", ax=ax)
    ax.set_title("Word length frequency", fontsize=25)
    ax.set_xlabel("Word length", fontsize=20)
    ax.set_ylabel("Count", fontsize=20)
    ax.set_ylim(0, max(frequency.values()))

    plt.show()


if __name__ == "__main__":
    main()
