/*
cmput 201 l6q2
Date Oct 7, 2020
Refrences: stack overflow, geeksforgeeks, hackr.io, class slides, slides from cmput 175
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>

void swap(int *i1, int *i2) {
   // swaps two values in an array
   int temp = *i1;
   *i1 = *i2;
   *i2 = temp;
}

void bubbleSort(int len, int toSort[len], int *comp, int *moves) {
   // sort using insert sort
   printf("Bubblesort is deployed...\n");
   *comp += 1;
   *moves += 1;
   for (int i = 0; i < len - 1; i++) {
      for (int j = 0; j < len - 1; j++) { // end of the array will be sorted
         *comp += 1;
	 if (toSort[j] > toSort[j + 1]) { // swap a[j] and a[j+1]
            swap(&toSort[j], &toSort[j + 1]);
            *moves += 2;
         }
      }
   }
    return;
}

void insertionSort(int len, int toSort[len], int *comp, int *moves) {
   // sort using insertion sort
   printf("Insertionsort is deployed...\n");
   *comp += 1;
   *moves += 1;
   for (int i = 1; i < len; i++) {
         int temp = toSort[i]; // take current value
	 int j = 0;
         *comp += 1;
         for (j = i - 1; j >= 0 && temp < toSort[j]; j--) {
            *moves += 1;
            toSort[j + 1] = toSort[j]; // move everything up as you find a spot
         }
         *moves += 1;
         toSort[j + 1] = temp; // insert the value into new spot
   }
}
 
void mergeSort(int len, int toSort[len], int sorted[len], int left, int right, int *comp, int *moves) {
   if (right <= left) {
      return;
   }
   // sort using mergesort
   int mid = (left + right) / 2; // find middle
   // split into halves and sort
   mergeSort(len, toSort, sorted, left, mid, comp, moves);
   mergeSort(len, toSort, sorted, mid + 1, right, comp, moves);
   // put together
   int pLeft = left;
   int pRight = mid + 1;
   // put them back based off big or small
   for(int i = left; i <= right; i++) {
      *comp += 1;
      if (pLeft == mid + 1) { // if reached left cap sort right
         moves += 1;
         sorted[i] = toSort[pRight];
         pRight++;
      } else if (pRight == right + 1) { // if reached right cap sort left
         moves += 1;
         sorted[i] = toSort[pLeft];
         pLeft++;
      } else if (toSort[pLeft] < toSort[pRight]) { // if value is less swap
         *moves += 1;
         sorted[i] = toSort[pLeft];
         pLeft++;
      } else {
        *moves += 1;
         sorted[i] = toSort[pRight]; // if value is more swap
         pRight++;
      }
   }
   // copy array back
   for (int i = 0; i < (right - left) + 1; i++) {
      toSort[i] = sorted[i];
   }
}

int split(int len, int toSort[len], int left, int right, int *comp, int *moves) {
   int pivot = toSort[left]; // set pivot to be first index
   for (;;) {
      while (right> left && toSort[right] > pivot) {
          *comp += 1; 
           right--;
      } // swap values arount the pivot
      if (left == right) {
         break;
      }
      *moves+= 1;
      swap(&toSort[left++], &toSort[right]);
      while(right > left && toSort[left] <= pivot) {
         *comp += 1; 
          left++;
      } // swap values around the pivot
      if (left == right) {
         break;
      }
      *moves += 1;
      swap(&toSort[right--], &toSort[left]);
      }
      toSort[left] = pivot; // puts pivot to left
      return left;
}

void quickSort(int len, int toSort[len], int left, int right, int *comp, int *moves) {
   // sort using quicksort
   if (left >= right) {
      return;
   }
   int part = split(len, toSort, left, right, comp, moves); // split the array into two
   // sort each half
   quickSort(len, toSort, left, part - 1, comp, moves);
   quickSort(len, toSort, part + 1, right, comp, moves);
   return;
}

void printResults(int len, int sortedArr[len], int *comp, int *moves) {
   // print out the sorted array, # of moves, # of comparisonsa
   printf("In sorted non-decreasing order: ");
   for (int *p = &sortedArr[0]; p < &sortedArr[len]; p++) {
      printf("%d ", *p);
   }
   printf("\nNumber of comparisons: %d\nNumber of moves: %d\n", *comp, *moves);
   *comp = 0;
   *comp = 0;
}

int main() {
   int len, *p, comp = 0, moves = 0;
   char method;
   printf("Enter the length of the array: "); // get length
   scanf("%d", &len);
   // declare arrays
   int toSort[len];
   int sorted[len];
   printf("Enter %d integers to be sorted: ", len); // get array values
   for (p = &toSort[0]; p < &toSort[len]; p++) {
	scanf("%d", p);
   }
   printf("Select from (a)ll | (b)ubblesort | (i)nsertionsort | (m)ergesort | (q)uicksort: "); // ask for sorting method
   scanf(" %c", &method);
   if(method == 'a') { // jump to sortin method based offchosen method	
      bubbleSort(len, toSort, &comp, &moves);
      printResults(len, toSort, &comp, &moves);
      insertionSort(len, toSort, &comp, &moves);
      printResults(len, toSort, &comp, &moves);
      printf("Mergesort deployed...\n");
      mergeSort(len, toSort, sorted, 0, len, &comp, &moves);
      printResults(len, toSort, &comp, &moves);
      printf("Quicksort deployed...\n");
      quickSort(len, toSort, 0, len, &comp, &moves);
      printResults(len, toSort, &comp, &moves);
   } else if (method == 'b') {
      bubbleSort(len, toSort, &comp, &moves);
      printResults(len, toSort, &comp, &moves);
   } else if (method == 'i') {
      insertionSort(len, toSort, &comp, &moves);
      printResults(len, toSort, &comp, &moves);
   } else if (method == 'm') {
      printf("Mergesort deployed\n");
      mergeSort(len, toSort, sorted, 0, len, &comp, &moves);
      printResults(len, toSort, &comp, &moves);
   } else if (method == 'q') {
      printf("Quicksort deployed\n");
      quickSort(len, toSort, 0, len, &comp, &moves);
      printResults(len, toSort, &comp, &moves);
   }
}
