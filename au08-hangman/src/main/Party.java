package main;

/**
 * Used as a model for the Hangman game
 */

class Party {
    String word;
    StringBuilder guess;
    String guessed;
    int hangman;

    Party(String word) {
        this.word = word;
        guess = new StringBuilder();
        guessed = "";
        hangman = 10;
    }
}
