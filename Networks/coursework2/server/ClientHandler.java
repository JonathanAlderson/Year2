import java.net.*;
import java.io.*;
import java.util.*;
import java.io.File;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;

public class ClientHandler extends Thread {
    private Socket socket = null;
    private String localDirectory = "/home/csunix/sc17j3a/Desktop/modules/year2/Networks/coursework2/server/serverFiles";

    BufferedWriter buffOut;
    BufferedReader in;

    public ClientHandler(Socket socket)
    {
  		super("clientHandler");
  		this.socket = socket;
    }

    public static void appendStrToFile(String str)
     {
         String fileName = "log.txt";
         try
         {
             // Open given file in append mode.
             BufferedWriter out = new BufferedWriter( new FileWriter(fileName, true));
             out.write(str);
             out.close();
         }
         catch (IOException e)
         {
             System.out.println("exception occoured" + e);
         }
     }


     // this function just returns a list of all of the files
     // in a directory
     public String getFilesInDirectory()
     {
       File dir = new File(localDirectory);
       File[] listOfFiles = dir.listFiles();
       String allFilesList = "\n\nAll Files On Server\n------------\n\n";

       // will fail for invalid directory
       try
       {
         for (int i = 0; i < listOfFiles.length; i++)
         {
           if (listOfFiles[i].isFile())
           {
             allFilesList = allFilesList + listOfFiles[i].getName() + "\n";
           }
         }
       }

       catch(NullPointerException e)
       {
         System.out.print("\nInvalid Directory\n\n");
         System.exit(0);
       }
       return allFilesList;
     }

     // checks if the file name is valid, and we can actually send
     // the file
     public boolean isFileInDirectory(String fileName)
     {
       File dir = new File(localDirectory);
       File[] listOfFiles = dir.listFiles();
       // will fail for invalid directory
       try
       {
         for (int i = 0; i < listOfFiles.length; i++)
         {
           if (listOfFiles[i].isFile())
           {
             if(listOfFiles[i].getName().equals(fileName))
             {
               return true;
             }
           }
         }
       }

       catch(NullPointerException e)
       {
         System.out.print("\nInvalid Directory\n\n");
         System.exit(0);
       }
       return false;
     }

     private static byte[] readFileToByteArray(File file){
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

     // Sends a file to the user
     public void sendFileToClient(String fileName)
     {
       try
       {
          buffOut = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
          File file = new File(fileName);
          byte[] bytes = readFileToByteArray(file);
          int count;
          System.out.print("\nRead file\nlength: " + bytes.length + "\n");
          int fileSize = bytes.length;
          int character;
          for (count = 0; count < bytes.length; count++)
          {
            buffOut.write(bytes[count]);
          }
          buffOut.flush();
          buffOut.close();
        }
        catch(IOException e)
        {
          System.out.print("\nFile not found\n");
        }
     }

     public void readFileFromClient(String fileName)
     {
       try
       {
         int character;

         System.out.print("\nReading file from client");
         File file = new File(fileName);
         long length = file.length();
         FileOutputStream fileOut = new FileOutputStream(file);

         while ((character = in.read()) > -1)
         {
           fileOut.write(character);
         }
         System.out.print("\nFinished Writing\n\n");
         fileOut.close();
       }
       catch(IOException e)
       {
         System.out.print("\n\nError while writing to file\n\n");
       }
     }


    public void run() {

    	try {
          String fileToGet = "";
          String fileToReceive = "";
          DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd/MM/yyyy : HH:mm");
          LocalDateTime now = LocalDateTime.now();
    	    PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
    	    in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
          InetAddress inet = socket.getInetAddress();
          Date date = new Date();

          System.out.println("Connection made from " + inet.getHostName());

    	    String inputLine, outputLine;

    	    while ((inputLine = in.readLine()) != null)
          {
            System.out.print("Reading...");
            appendStrToFile(dtf.format(now) + " : " +inet.getHostName() + " : " +inputLine + "\n");
            // now do processing on the inputLine
            if(inputLine != null)
            {
              if(inputLine.equals("list"))
              {
                System.out.print("\nSending list to client");
                out.println(getFilesInDirectory());
                out.println("Done"); // sends a null to end client
                System.out.print("\nFinished sending list to client\n\n");
              }

              else if(inputLine.substring(0,3).equals("get"))
              {
                System.out.print("\nGiving file to client");
                fileToGet = inputLine.substring(4,inputLine.length());
                if(isFileInDirectory(fileToGet))
                {
                  out.println("Valid File");
                  out.flush();
                  sendFileToClient("serverFiles/" + fileToGet);
                  System.out.print("Finished sending file to client\n");
                }
                else
                {
                  System.out.print("\nFile not found on server");
                  out.println("Error");
                  out.flush();
                }
                break;
              }
              else if(inputLine.substring(0,3).equals("put"))
              {
                System.out.print("\nNow recieving file from client");
                fileToReceive = inputLine.substring(4,inputLine.length());
                readFileFromClient("serverFiles/" + fileToReceive);
              }
            }
    	    }
          buffOut.close();
    	    out.close();
    	    in.close();
    	    socket.close();
          System.out.print("Closed client socket\n\n");
    	}
      catch (IOException e)
      {
          System.out.print("\nThere was an error\n");
    	}
    }
}
