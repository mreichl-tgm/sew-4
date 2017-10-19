package stream;

import encryption.Encryptor;

/**
 * A TextReaderDecorator using a the encryption.Encryptor class to encrypt communication
 */
public class Scrambling extends TextReaderDecorator {
    /**
     * Wraps a TextReader and calls its constructor
     * @param textReader Wrapped TextReader instance
     */
    public Scrambling(TextReader textReader) {
        super(textReader);
    }

    /**
     * @param str String to encrypt
     * @return String
     */
    @Override
    public String read(String str) {
        System.out.println("Scrambling.read >> Encryption successful!");
        return Encryptor.encrypt(textReader.read(str));
    }

    /**
     * @param str String to decrypt
     */
    @Override
    public void write(String str) {
        System.out.println("Scrambling.read >> Decryption successful!");
        textReader.write(Encryptor.decrypt(str));
    }
}
