package main;

import stream.Authentication;
import stream.Scrambling;
import stream.TextReader;
import stream.Worker;

public class Main {

    /**
     * Creates an empty string to read from and write to using a TextReader stream
     * @param args Argument Array
     */
    public static void main(String[] args) {
		System.out.println( "Main.main >> Let's start!");
	    TextReader stream = new Authentication(new Scrambling(new Worker()));
	    String str = "";
	    str = stream.read(str);
	    System.out.println("Main.main >> " + str);
	    stream.write(str);
	}
}
