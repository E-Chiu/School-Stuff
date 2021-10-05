// partner: ntang

import java.util.Arrays;
import java.lang.Math;
import java.util.Scanner;

class BinarySearch {
    static int binarySearch(int[] arr, int x, int low, int high) {
        int mid  = low + (high -  low) / 2;
        if(low <= high) {
            if (arr[mid] == x) {
                return mid;
            } else if(x > arr[mid]) {
                return binarySearch(arr, x, mid + 1, high);
            } else if(x < arr[mid]) {
                return binarySearch(arr, x, low, mid - 1);
            }
        }
        return -1;
    }

    static int findIndex(int[] arr, int x, int n) {
        if (n > arr.length) {
            n = arr.length;
        }

        if (n == 0) {
            return -1;
        }

        int[] subArr = Arrays.copyOfRange(arr, 0, n+1);

        return binarySearch(subArr, x, 0, n);
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        System.out.println("Array (Numbers delimited by comma): ");
        String arr = scan.nextLine();
        int[] array = Arrays.stream(arr.split(","))
            .mapToInt(Integer::parseInt)
            .toArray();

        int x;
        System.out.println("Number: ");
        x = scan.nextInt();
        
        int n;
        System.out.println("Range: ");
        n = scan.nextInt();
        scan.close();
        
        int result = findIndex(array, x, n);
        System.out.println("Result: \n" + result);
        
    }
}