package stream;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * Interface providing a BufferedReader to read system input and process it
 */
public interface TextReader {
	BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

    String read(String str);
	void write(String str);
}
