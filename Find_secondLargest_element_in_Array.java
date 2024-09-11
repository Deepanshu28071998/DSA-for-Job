// package Array;

class SecondLargest
{
    public static void main(String[] args)
    {
        int[] arr = {1, 6, 3, 9, 10, 7, 4};
        int n = arr.length;
        int max = 0;
        int secondMax = 0;

        if (arr[0] >= arr[1])
        {
            max = arr[0];
            secondMax = arr[1];
        }
        else
        {
            max = arr[1];
            secondMax = arr[0];
        }
        for (int i = 2; i < n; i++)
        {
            if (arr[i] > max)
            {
                secondMax = max;
                max = arr[i];
            }
            else if (arr[i] > secondMax && arr[i] != max)
            {
                secondMax = arr[i];
            }
        }
        System.out.println("Second largest element is " + secondMax);
    }
}
