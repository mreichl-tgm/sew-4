package stream;

/**
 * Base for classes decorating TextReader instances
 */
abstract class TextReaderDecorator implements TextReader {
    TextReader textReader;

    TextReaderDecorator(TextReader textReader) {
        this.textReader = textReader;
    }
}
