package main;

import java.io.IOException;
import java.net.ServerSocket;

/**
 * @author Markus Reichl
 * @version 19.12.2016
 *
 * Server to host the hangman application
 */

public class Server {
    public static void main(String[] args) throws IOException {
        int PORT = 12345;
        // Handle Arguments
        try {
            PORT = Integer.parseInt(args[0]);
        } catch (NumberFormatException e) {
            System.out.println("Port is not a number!");
            System.out.println("Falling back to default port!");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Not enough arguments given!");
        }
        // Setup Server
        try (
                ServerSocket serverSocket = new ServerSocket(PORT)
        ) {
            System.out.println("Server running on " + serverSocket.getLocalSocketAddress());

            while (!serverSocket.isClosed()) {
                new ClientHandler(serverSocket.accept()).start();
            }
        } catch (IOException e) {
            System.out.println("Socket Error!");
            System.exit(-1);
        }
    }
}