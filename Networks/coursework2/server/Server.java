import java.net.*;
import java.io.*;
import java.util.concurrent.*;

public class Server {

	// As a demonstration, put everything into main(); obviously you would probably want
	// to use instance variables and break this up into separate methods for a real application.
    public static void main(String[] args) throws IOException {
        System.out.print("\n\nStarting server\n------------------\n");
        ServerSocket server = null;
        ExecutorService service = null;

		// Try to open up the listening port
        try {
            server = new ServerSocket(8888);
        } catch (IOException e) {
            System.err.println("Could not listen on port: 8888.");
            System.exit(-1);
        }

		// Initialise the executor.
		service = Executors.newFixedThreadPool(10);

		// For each new client, submit a new handler to the thread pool.
		while( true )
		{
			Socket client = server.accept();
			service.submit( new ClientHandler(client) );
		}
    }
}
