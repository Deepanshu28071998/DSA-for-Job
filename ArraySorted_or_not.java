class ArraySorted_or_not
{
    public static boolean is_sort(int[] arr)
        {
            

            for (int i = 0; i<arr.length-1; i++)
            {
                if (arr[i] <= arr[i+1])
                {
                    continue;

                }
                else
                {
                    return false;
                }
            }
            return true;

        }

        public static void main(String[] args) {
            int[] arr = {1, 2, 3, 4, 5};
            System.err.println(is_sort(arr));
        }
}