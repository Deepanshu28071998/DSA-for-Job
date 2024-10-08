import java.util.Scanner;

public class Generates_subsets 
{
    public static void subsets(String s, String curr, int i)
    {
        if (i == s.length())
        {
            System.out.println(curr);
            return;
        }
        subsets(s, curr, i+1);
        subsets(s, curr + s.charAt(i), i+1);
    }
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        String curr = "";
        int i = 0;
        subsets(s, curr, i);
        subsets(s, curr + s.charAt(i), i+1);
        // System.out.println(res);
    }
}
