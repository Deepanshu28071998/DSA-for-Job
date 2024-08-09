class Max_element
{
    public static void main(String[] args) 
    {
        int[] arr = {5, 4, 3, 2, 8, 1};
        int max = arr[0];
        for (int i = 1; i < arr.length; i++)
        {
            if (arr[i] > max)
            {
                max = arr[i];
            }
        }
        System.out.println("Maximum element in array is: " + max);
    }
}