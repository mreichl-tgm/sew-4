package main;

import java.util.LinkedList;

/**
 * @author Markus Reichl
 * @version 20.12.2016
 *
 * Class used to communicate between sockets
 */

class HangmanProtocol {
    private static LinkedList<Party> parties = new LinkedList<>();

    private Party party;
    private boolean first;

    HangmanProtocol() {
        first = true;
        party = null;
    }

    String processInput(String inputLine) {
        String outputLine = inputLine;

        if (first) {
            first = false;
            return "Welcome to Hangman! Use /new?word to create a new game or /join to join one!";
        }

        if (inputLine.contains("/help")) {
            return help();
        }

        if (party == null) {

            if (inputLine.contains("/join")) {
                if (parties.size() == 0) return "No party available!";
                else {
                    party = parties.getLast();
                    return "Joined a party!";
                }
            }

            if (inputLine.contains("/new?")) {
                party = new Party(inputLine.substring(5).toUpperCase());
                parties.add(party);

                for (int i = 0; i < party.word.length(); i++) {
                    party.guess.append("_");
                }

                outputLine = "New word: " + party.guess;
            }
        } else {
            if (inputLine.toUpperCase().equals(party.word)) {
                outputLine = "You win!";
                parties.remove(party);
                party = null;
            } else if (inputLine.length() == 1) {
                char c = inputLine.toUpperCase().charAt(0);

                if (party.guessed.indexOf(c) > -1) {
                    outputLine = c + " has already been guessed..";
                } else {
                    party.guessed += c;

                    if (party.word.indexOf(c) > -1) {
                        for (int i = 0; i < party.word.length(); i++) {
                            if (party.word.charAt(i) == c) party.guess.setCharAt(i, c);
                        }

                        outputLine = party.guess.toString();

                        if (party.word.equals(party.guess.toString())) {
                            outputLine += " All letters guessed! You win!";
                        }
                    } else {
                        outputLine = c + " is not contained!";
                        outputLine += hang();
                    }
                }
            } else {
                outputLine = inputLine + " was not the word..";
                outputLine += hang();
            }
        }

        return outputLine;
    }

    private String help() {
        return "[/help], [/new?word], [/join], [/quit]";
    }

    private String hang() {
        party.hangman--;
        String outputLine = " Only " + (party.hangman) + " more tries!";

        if (party.hangman == 0) {
            outputLine = " You lost! The word was " + party.word;
            parties.remove(party);
            party = null;
        }

        return outputLine;
    }
}