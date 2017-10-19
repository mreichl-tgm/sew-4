package main;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

/**
 * @author Markus Reichl
 * @version 20.12.2016
 *
 * A Runnable class used to handle a client
 */

class ClientHandler extends Thread {
    private Socket socket = null;

    ClientHandler(Socket socket) {
        super("ClientHandler");
        this.socket = socket;
    }

    @Override
    public void run() {
        try (
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))
        ) {
            String inputLine, outputLine;

            HangmanProtocol hp = new HangmanProtocol();
            outputLine = hp.processInput("");
            out.println(outputLine);

            while ((inputLine = in.readLine()) != null) {
                outputLine = hp.processInput(inputLine);
                out.println(outputLine);

                if (inputLine.equals("/quit")) break;
            }

            socket.close();
            System.out.println("Client socket closed!");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    void receive(String msg) {
        try (
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true)
        ) {
            System.out.println(msg);
            out.println(msg);
            System.out.println(in.readLine());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}