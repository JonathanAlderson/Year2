import java.io.*;
import java.net.*;
import java.lang.*;
import java.util.*;
import java.io.File;


public class Client {

    private Socket socket = null;
    private PrintWriter socketOutput = null;
    private BufferedReader socketInput = null;
    private BufferedWriter buffOut;
    private FileOutputStream fileOut;
    private File file;

    public int determineCommand(String cmdLineArg)
    {
      try
      {
        // check for list
        if(cmdLineArg.substring(0,4).equals("list") && cmdLineArg.length() == 4)
        {
          socketOutput.println("list"); // tells the server we need a list
          this.readFromServer(); // read what the server tells us
        }

        // check for get
        if(cmdLineArg.substring(0,3).equals("get"))
        {
          socketOutput.println(cmdLineArg); // passes the file name to be saved to
          this.readFileFromServer("clientFiles/"+cmdLineArg.substring(4,cmdLineArg.length()));
        }

        // check for put
        if(cmdLineArg.substring(0,3).equals("put"))
        {
          socketOutput.println(cmdLineArg); // passes the file name to be saved to
          this.sendFileToServer(cmdLineArg.substring(4,cmdLineArg.length()));
        }
      }
      catch(Exception e)
      {
        // helpful error message
        System.out.print("\nInvalid command line argument!\nTry: 'list', 'get file.txt' or 'put file.txt'\n\n\n\n");
        System.exit(0);
      }

      // an unknown message has been recieved
      return 0;
    }

    private static byte[] readFileToByteArray(File file){
        // reads a file into an array of bytes to be sent
        FileInputStream fileInput = null;
        byte[] bytes = new byte[(int) file.length()];
        try{
            fileInput = new FileInputStream(file);
            fileInput.read(bytes);
            fileInput.close();
        }
        catch(IOException e)
        {
            System.out.print("\nError reading file\nPlease ensure file is valid\n");
            System.exit(0);
        }
        return bytes;
    }


    public void readFileFromServer(String fileName)
    {
      try
      {
        String fromServer;

        // first we see if the file is valid before creating the file
        fromServer = socketInput.readLine();

        if(fromServer.equals("Error")) // server will send "Done" when everything has finished
        {
          System.out.print("\nFile not found on server\n\n");
          System.exit(1);
        }
        else
        {
          System.out.print("\n\nReading file from server\n");
        }

        int character;

        file = new File(fileName);
        buffOut = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
        fileOut = new FileOutputStream(file);

        while ((character = socketInput.read()) > -1)
        {
          // writes to the file
          fileOut.write(character);
        }
        System.out.print("Finished Writing\n\n");
      }
      catch(IOException e)
      {
        System.out.print("\n\nError while writing to file\n\n");
      }
    }

    public void sendFileToServer(String fileName)
    {
      try
      {
         buffOut = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
         // looks in the client files directory
         File file = new File("clientFiles/" + fileName);
         byte[] bytes = readFileToByteArray(file);
         int count;
         System.out.print("\nRead file\nlength: " + bytes.length);
         int fileSize = bytes.length;
         for (count = 0; count < bytes.length; count++)
         {
           // writes the bytes to the buffered output
           buffOut.write(bytes[count]);
         }
         buffOut.flush();
         System.out.print("\nFinished sending file to server");
         // closing all the connections
         buffOut.close();
         socketOutput.close();
         socketInput.close();
         socket.close();
         System.out.print("\nClosed all connections\n\n");
       }
       catch(IOException e)
       {
         System.out.print("\nFile not found\n");
       }
    }

    // this function is used at the start to connect to the server
    public void connectToServer()
    {
        try {
            // try and create the socket
            socket = new Socket( "localhost", 8888 );
            // chain a writing stream
            socketOutput = new PrintWriter(socket.getOutputStream(), true);
            // chain a reading stream
            socketInput = new BufferedReader(new InputStreamReader(socket.getInputStream()));

        }
        catch (UnknownHostException e) {
            System.err.println("Unknown host error.\n");
            System.exit(1);
        }
        catch (IOException e) {
            System.err.println("Couldn't get I/O for the connection to host.\n");
            System.exit(1);
        }
    }

    // reads a string that the server sends back
    // used in the list command
    public void readFromServer()
    {
      String fromServer;
      try {
        while ((fromServer = socketInput.readLine()) != null)
        {
            if(fromServer.equals("Done")) // server will send "Done" when everything has finished
            {
              break;
            }
            // print what server says
            System.out.println(fromServer);
        }
        System.out.print("\nServer completed sending message\n");
        socketOutput.close();
        socketInput.close();
        socket.close();
      }
      catch (IOException e) {
          System.err.println("I/O exception during execution\n");
          System.exit(1);
      }
    }

    public static void main(String[] args)
    {
      Client client = new Client();
      String arguments = String.join(" ", args);
      client.connectToServer();
      // see what the arguments were to see which function to run
      client.determineCommand(arguments);

    }

}
