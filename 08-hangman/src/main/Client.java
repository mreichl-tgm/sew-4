package main;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

/**
 * @author Markus Reichl
 * @version 19.12.2016
 *
 * Client used to play the hangman game
 */

public class Client {
    public static void main(String[] args) throws IOException {
        String HOST = "127.0.0.1";
        int PORT = 12345;
        // Startup
        try {
            HOST = args[0];
            PORT = Integer.parseInt(args[1]);
        } catch (NumberFormatException e) {
            System.out.println("Given port is not a number!");
            System.out.println("Falling back to default port: " + PORT);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Not enough arguments given!");
            System.out.println("Falling back to default host: " + HOST + ":" + PORT);
        }

        try (
                Socket socket = new Socket(HOST, PORT);
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                Scanner scanner = new Scanner(System.in)
        ) {
            String inputLine, outputLine;

            while ((inputLine = in.readLine()) != null) {
                System.out.println("Server: " + inputLine);

                if (inputLine.equals("/quit")) break;

                System.out.print(">> ");
                outputLine = scanner.nextLine();

                System.out.println("Client: " + outputLine);
                out.println(outputLine);
            }

            System.out.println("Disconnected!");
        } catch (IOException e) {
            System.out.println("Socket Error!");
            System.exit(1);
        }
    }
}
