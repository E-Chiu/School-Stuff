/*
Cmput 201 lab 9
Date: Oct 31, 2020:
Refrences: stackoverflow how to generate random float
Lab Section: D01
Name: Ethan Chiu
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

struct point {
   float x;
   float y;
   struct point *next;
};

struct point *generate(int n) {
   // generates shapes with n random points
   struct point *tempPoint1 = malloc(sizeof(struct point)); // first point
   struct point *head = tempPoint1; // head point
   struct point *tempPoint2; // middle point(s)
   tempPoint1->x = 1 + ((float)rand()/(float)(RAND_MAX/1000));
   tempPoint1->y = 1 + ((float)rand()/(float)(RAND_MAX/1000));
   for(int i = 0; i < n - 1; i++) {
      tempPoint2 = malloc(sizeof(struct point)); // middle point(s)
      tempPoint2->x = 1 + ((float)rand()/(float)(RAND_MAX/1000));
      tempPoint2->y = 1 + ((float)rand()/(float)(RAND_MAX/1000));
      tempPoint1->next = tempPoint2; // point to next point
      tempPoint1 = tempPoint1->next; // move to next point
   }
   tempPoint1->next = NULL; // set last point to point to NULL
   return head; // return address of first point
}

void printing(struct point *shape) {
   // print shape
   printf("<");
   while (shape != NULL) {
      printf("(%.3f, %.3f)", shape->x, shape->y);
      if(shape->next != NULL) {
         printf(", ");
      }
      shape = shape->next;
   }
   printf(">\n");

}

void freeMem(struct point *shape) {
   // free allocated memory
   struct point *temp;
   while(shape != NULL) {
      temp = shape;
      shape = shape->next; // move to next shape
      free(temp); // free previous
   }
}

struct point *index_sample(struct point *shape, int k) {
   struct point *copyPoint = shape; // copy head of shape
   int n = 0;
   // find n
   while(copyPoint != NULL) {
      n++;
      copyPoint = copyPoint->next; // add to counter and go next
   }
   // make sample
   struct point *sample1 = malloc(sizeof(struct point));
   struct point *sampleHead = sample1; // copy head pointer
   int index, currentInd = 0; // casting to int should floor it
   sample1->x = shape->x;
   sample1->y = shape->y; // copy x and y values of head
   struct point *sample2;
   for (int i = 0; i < k - 2; i++) {
      index = ((i + 1) * n) / (k - 1);
      index -= currentInd; // subtract current index to see how much is needed to travel
      for(int j = 0; j < index; j++) {
         shape = shape->next; // travel to needed index
      }
      sample2 = malloc(sizeof(struct point));
      sample2->x = shape->x;
      sample2->y = shape->y; // copy x and y values
      sample1->next = sample2; // point to next sample point
      sample1 = sample1->next; // go to next point
   }
   while(shape->next != NULL) { // go to last point
      shape = shape->next;
   }
   sample2 = malloc(sizeof(struct point));
   sample2->x = shape->x;
   sample2->y = shape->y; // copy points of tail
   sample2->next = NULL; // tail points to null
   sample1->next = sample2; // point to tale
   return sampleHead; // return first point
}

float sample_distance(struct point *shape1, struct point *shape2, int k) {
   // calculates and returns sample distance
   // make samples
   struct point *sample1 = index_sample(shape1, k);
   struct point *sample2 = index_sample(shape2, k);
   // copy heads for freeing memory later
   struct point *sample1Head = sample1;
   struct point *sample2Head = sample2;
   // print samples
   printf("%d-sample of Shape1: ", k);
   printing(sample1);
   printf("%d-sample of Shape2: ", k);
   printing(sample2);
   // find total distance
   float dist = 0, xDiff, yDiff, temp;
   for(int i = 0; i < k; i++) {
      xDiff = sample1->x + sample2->x;
      xDiff = powf(xDiff, 2); // calculate x difference
      yDiff = sample1->y + sample2->y;
      yDiff = powf(yDiff, 2); // calculate y difference
      temp = yDiff + xDiff;
      temp = sqrtf(temp); // get length
      dist += temp; // add to total
      sample1 = sample1->next;
      sample2 = sample2->next; // go to next point(s)
   }
   // free memory
   freeMem(sample1Head);
   freeMem(sample2Head);
   return dist; // return sample distance when done
}

int main() {
   srand(time(NULL)); // seed random 

   /* PART 1 */
   // make shapes  
   int n1, n2;
   printf("Enter two integers in [1, 1000]: "); // print representation
   scanf("%d%d", &n1, &n2);
   struct point *shape1 = generate(n1);
   struct point *shape2 = generate(n2);
   // print shapes
   if (n1 == 1) {
      printf("Shape1 with 1 point: ");
   } else {
      printf("Shape 1 with %d points: ", n1);
   }
   printing(shape1);
   if (n2 == 1) {
      printf("Shape2 with 1 point: ");
   } else {
      printf("Shape 2 with %d points: ", n2);
   }
   printing(shape2);

   /* PART 2 - PARTS COMMENTED OUT SINCE IT IS TO BE DONE IN PART 3*/
   int k;
   printf("Enter an integer in [2, 1000]: ");
   scanf("%d", &k);
   /*
   struct point *sample1 = index_sample(shape1, k);
   struct point *sample2 = index_sample(shape2, k);
   // print samples
   printf("%d-sample of Shape1: ", k);
   printing(sample1);
   printf("%d-sample of Shape2: ", k);
   printing(sample2);
   */
   
   /* PART 3 */
   float dist = sample_distance(shape1, shape2, k); // find sample distance
   printf("The 3-sample distance is: %.3f", dist); // print result
   // free memory
   freeMem(shape1);
   freeMem(shape2);
   /*
   freeMem(sample1);
   freeMem(sample2);
   */
}
