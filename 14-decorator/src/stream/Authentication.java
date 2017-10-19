package stream;

import java.io.IOException;

/**
 * A TextReaderDecorator using a password to verify the user
 */
public class Authentication extends TextReaderDecorator {
    private String pw;

    /**
     * Wraps a TextReader and calls its constructor
     * @param textReader Wrapped TextReader instance
     */
    public Authentication(TextReader textReader) {
        super(textReader);
        pw = "default";
    }

    /**
     * @param str Text to set a password on
     * @return String
     */
    @Override
    public String read(String str) {
        System.out.print("Authentication.read << ");
        try {
            pw = in.readLine();
            System.out.println("Authentication.write >> Password set!");
        } catch (IOException e) {
            e.printStackTrace();
        }

        return textReader.read(str);
    }

    /**
     * @param str String to authenticate on
     */
    @Override
    public void write(String str) {
        System.out.print("Authentication.write << ");
        try {
            String input = in.readLine();

            if (input.equals(pw)) {
                textReader.write(str);
                System.out.println("Authentication.write >> Login successful!");
            } else {
                System.out.println("Authentication.write >> Wrong password!");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
