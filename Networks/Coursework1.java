14:15
import java.net.InetAddress;
import java.net.Inet4Address;
import java.net.Inet6Address;
import java.util.*;
import java.io.IOException;
import java.net.UnknownHostException;

// the class for coursework1, with just a main function
// which outputs infomation about the IP addresses
public class Coursework1 {


    private InetAddress address;
    private int[][] allIPs;// 2d array of all IP addresses
    private String[] thisSplitIP;// this is split up into a string
    private String thisIP;// the current IP being looped through
    private int ipCounter;// counts how many IP addressses we have
    private int heirarchy;

    public Coursework1()
    {
      allIPs = new int[10][4]; // 2d array of all IP addresses
      ipCounter = 0;               // counts how many IP addressses we have
      //return this.address;
    }

    // gets the current host address
    public String getHostAddress()
    {
      return this.address.getHostAddress();
    }

    // gets the current host name
    public String getCanonicalHostName()
    {
      return this.address.getCanonicalHostName();
    }

    // finds out if address is reachable
    public boolean isReachable(int timeout) throws IOException
    {
      return this.address.isReachable(timeout);
    }

    // gets the current instances address
    public InetAddress getAddress()
    {
      return this.address;
    }

    // when given a host name, will print out all the
    // information about it
    public void resolve(String url)
    {
      try
      {
        address = address.getByName(url);
      }
      catch(UnknownHostException e)
      {
        System.out.print("\n\n\nInvalid address name\n\n\n");
        System.exit(0);
      }
      System.out.println("\n\n\n\n" + url + "\n-----------------");
      System.out.println("IP Address: " + this.getHostAddress());
      System.out.println("Canonical Host Name: " + this.getCanonicalHostName());
      try
      {
        if (this.isReachable(200)) {
          System.out.println("Host Is Reachable");
        }
        else {
          System.out.println("Host Is Not Reachable");
        }
        if (this.address instanceof Inet4Address) {
          System.out.println("Address Is IPv4\n");
        }
        else if (this.address instanceof Inet6Address) {
          System.out.println("Address Is IPv6\n");
        }
      }
      catch(IOException e)
      {
        System.out.print("\n\n\nInvalid address name\n\n\n");
        System.exit(0);
      }
    }

    // goes through the 2d array of IP addresses and
    // returns an int for how many of the bytes are the same
    private int findLevelOfHeirarchy()
    {
      // check the order of the addresses
      int heirarchy = 0;
      int valid = 0; // when set to 1 it is invalid
      int i;

      while(valid == 0 && heirarchy < 4)
      {
        for(i=0; i < this.ipCounter; i++)
        {
          if(this.allIPs[0][heirarchy] != this.allIPs[i][heirarchy])
          {
            valid = 1;
          }
        }
        if(valid == 0)
        {
          heirarchy++;
        }
      }
      return heirarchy;
    }

    // prints onto the screen the level of heirarchy shared by
    // all of the IP addresses in the ..*.* form
    private void printLevelOfHeirarchy()
    {
      // output the highest level of heirarchy
      for(int i=0; i < this.heirarchy; i++)
      {
        System.out.print(this.allIPs[0][i]);
        if(i < 3) // this is to make the formatting correct
        {
          System.out.print(".");
        }
      }
      for(int i=this.heirarchy; i < 4; i++)
      {
        System.out.print("*");
        if(i < 3)  // stops the addresses ending like ..*.*.
        {
          System.out.print(".");
        }
      }
    }

    // this function, outputs the info for each hostname and shows
    // the highest level of heirarchy shared by all IP addresses
    public static void main(String[] args) throws Exception {

      Coursework1 coursework1 = new Coursework1();
      System.out.print("\033[H\033[2J"); // clears the screen

      // turn all IP addresses into integers and
      // put into a 2d array
      for (String url: args) {
        try
        {
          coursework1.address = InetAddress.getByName(url);
        }
        catch(Exception e)
        {
          System.out.print("\n\n\nInvalid address name\n\n\n");
          System.exit(0);
        }
        coursework1.address = InetAddress.getByName(url);
        coursework1.thisIP = coursework1.getAddress().getHostAddress();
        coursework1.thisSplitIP = coursework1.thisIP.split("\\.");
        // convert from string to integers
        for(int i=0; i < coursework1.thisSplitIP.length; i++)
        {
          coursework1.allIPs[coursework1.ipCounter][i] = Integer.parseInt(coursework1.thisSplitIP[i]);
        }
        coursework1.ipCounter = coursework1.ipCounter + 1;
      }

      coursework1.heirarchy = coursework1.findLevelOfHeirarchy();

      // output the info for each hostname
      for (String url: args) {
        coursework1.resolve(url);
      }

      System.out.println("\n\n\nThe Highest Level of Heirarchy Shared by All IP's is:");
      coursework1.printLevelOfHeirarchy();
      System.out.print("\n\n\n\n");
    }

}
