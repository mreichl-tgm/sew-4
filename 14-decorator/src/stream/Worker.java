package stream;

import java.io.IOException;

/**
 * A TextReader implementing some basic versions of read and write
 */
public class Worker implements TextReader {
    /**
     * @param str String to overwrite
     * @return String
     */
    public String read(String str) {
        System.out.print("Worker.read << ");

        try {
            str = in.readLine();
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }

        return str;
    }

    /**
     * @param str String to print out
     */
    public void write(String str) {
        System.out.println("Worker.write >> " + str);
    }
}
