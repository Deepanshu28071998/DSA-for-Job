
class Tower_of_Hanoi
{
    public static void TOH(int n, char A, char B, char C)
    {
     if (n == 1)
     {
        System.out.println("Move 1 from " + A + " to " + C);
        return;
     }
     
     TOH(n - 1, A, C, B);
     System.out.println("Move " + n + " from " + A + " to " + C);
     TOH(n - 1, C, B, A);
    }

    public static void main(String[] args)
    {
        int n = 3;
        char A = 'A';
        char B = 'B';
        char C = 'C';
        TOH(n, A, C, B);
    }
    
}


// // JAVA recursive function to
// // solve tower of hanoi puzzle
// import java.io.*;
// import java.math.*;
// import java.util.*;
// class GFG {
//     static void towerOfHanoi(int n, char from_rod,
//                              char to_rod, char aux_rod)
//     {
//         if (n == 0) {
//             return;
//         }
//         towerOfHanoi(n - 1, from_rod, aux_rod, to_rod);
//         System.out.println("Move disk " + n + " from rod "
//                            + from_rod + " to rod "
//                            + to_rod);
//         towerOfHanoi(n - 1, aux_rod, to_rod, from_rod);
//     }

//     // Driver code
//     public static void main(String args[])
//     {
//         int N = 3;

//         // A, B and C are names of rods
//         towerOfHanoi(N, 'A', 'C', 'B');
//     }
// }

// // This code is contributed by jyoti369

