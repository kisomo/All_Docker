
/*

FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential


FROM gcc:latest 

COPY . /usr/src/c_test 

WORKDIR /usr/src/c_test

RUN  gcc -g C_prep.c -o C_prep

CMD ["./C_prep"]

*/



/*

sudo docker build . -t interview_prep:1.0.0

sudo docker images

sudo docker run -d -p 5000:5000 interview_prep:1.0.0
sudo docker run --rm -it interview_prep:1.0.0

*/



#include <string.h>
#include <malloc.h>
#include <stdlib.h>
#include <errno.h> //errno
#include <stdio.h>  //printf
#include <unistd.h> //sleep
#include <time.h>

#define NELEMS(x)  (int) (sizeof(x) /  sizeof((x)[0]))

int largestRange(int *array, int sz);
//int find_the_index(int array[], int element, int sz);
int max_array(int array[], int sz);
int min_array(int array[], int sz);

int find_index(int arr[], int n,int target);
int binary_search(int arr[], int n, int target);

int bubble_sort(int arr[], int sz, int target);

int main(int argc, char **argv)
{
    int array[] = {1,11,3,0,15,5,2,4,10,7,12,6};
    int sz = 12; //(int) NELEMS(array);

    /*
    int left_number ;
    int right_number ;
    int max_number ;
    int min_number ;
    */


    //largestRange(array,sz);
    
    int res = largestRange(array,sz);

    //int a = res[0];
    //int b = res[1];
    //fprintf(stderr, "%d\n",a);
    //fprintf(stderr, "%d\n",b);


    int arr[]  = {1,2,3,6,7,10,15};
    int res2 = find_index(arr,7,10);
    int res3 = binary_search(arr,7,10);
    printf("result one = %d\n",res2);
    printf("result two = %d\n",res3);
     
    int res4 = bubble_sort(arr,7,10);
    printf("result bubble = %d\n",res4);


    return 0;
}


int largestRange(int *array, int sz)
{

    int left_number ;
    int right_number ;

    // create a hash table
    //size_t array_size = sizeof(array)/sizeof(array[0]);
    //size_t array_size = (int) NELEMS(array);

    int max_number = max_array(array,sz);
    int min_number = min_array(array,sz);

    int number_indices[sz]; memset(number_indices,0,sz);

    int left =0; int right =0;

    for(int i=0;i<sz;i++)
    {
        if(number_indices[i] ==0)
        {
                left_number = array[i] -1; right_number = array[i] +1;

                while(left_number >= min_number)
                {
                    int index = find_index(array,sz,left_number); number_indices[index] =1; left_number -=1;
                }
                left_number+=1;

                while(right_number <= max_number)
                {
                    int index = find_index(array,sz,right_number); number_indices[index] =1; right_number +=1;
                }
                right_number-=1;

                //if ((right - left) <= (right_number - left_number)) { right = right_number; left = left_number; }
                

        }else { continue;}

         //if ((right - left) <= (right_number - left_number)) { right = right_number; left = left_number; }

    }
    if ((right - left) <= (right_number - left_number)) { right = right_number; left = left_number; }

    int res[] = {left,right};

    printf("min number = %d\n",min_number);
    printf("max number = %d\n",max_number);
    printf("left = %d\n",(int) left);
    printf("right = %d\n",(int) right);

    return 0;
}



/*
int find_the_index(int arr[], int element, int sz)
{
    int index;
    //size_t n = sizeof(arr)/sizeof(int);
    //size_t n = (int) NELEMS(arr);

    for (int i = 0; i <= sz; i++)
    {
        if (element == arr[i]) { index = i; } else {continue;}
    }

}
*/

// ---------------------------

int max_array(int arr[], int sz)
{
    int mx = arr[0];
    //size_t n = sizeof(arr)/sizeof(int);
    //size_t n = (int) NELEMS(arr);

   for(int i=0;i<=sz;i++) { if(arr[i] >= mx) {  mx = arr[i]; } else {continue;} }
   return mx;

}

// -------------------------


int min_array(int arr[], int sz)
{
    int mn = arr[0];
    //size_t n = sizeof(arr)/sizeof(int);
    //size_t n = (int) NELEMS(arr);
   for(int i=0;i<=sz;i++) { if(arr[i] <= mn) { mn = arr[i]; } else {continue;} }

   return mn;

}


// ###########################################################################################################################################################################


int getnthfib(int n)
{
    if (n ==1) {return 0;}
    else if (n <= 3) {return 1;}
    else 
    {
        int res = getnthfib(n-1) + getnthfib(n-2);
        return res;
    }
}


//printf("########################################################## INTERVIEW GOLDMAN SACHS ##########################################################################\n");

/*

#include <stdio.h>

//#define length_arr(x)

// To execute C, please define "int main()"

int find_index(int arr[], int n,int target);
int binary_search(int arr[], int n, int target);

int main() {
 
  int arr[]  = {1,2,3,6,7,10,15};
 
  int res = find_index(arr,7,10);
  int res2 = binary_search(arr,7,10);
 
  printf("result one = %d\n",res);
  printf("result two = %d\n",res2);
 
  return 0;
}

*/

int find_index(int arr[], int n,int target)
{
   int k =0;
   for(int i =0;i<n;i++)
   {
     if(arr[i] >= target)
     {
        k = i;
         break;
     }
   }
 
  return  k;
}


int binary_search(int arr[], int n, int target)
{
   int lower = 0;
  int upper = n;
  int x, res;
 
  while (lower < upper)
  {
    x = lower + (upper - lower)/2;
    res = arr[x];
    if (target ==res)
    {
      return x;
    } else if (target >res )
    {
      lower = x;
    } else if(target < res)
    {
       upper = x;
    }
  }
 
  return res;
}


int bubble_sort(int arr[], int sz)
{
  int res;
  for(int i=0;i<sz;i++)
  {
    if (target = arr[i])
     {
       res = i;
       return res;
     } else if (target = arr[i+1]) 
     {
       res = i+1;
       return res;
      }
    else {continue;}
  }
  return res;

}



//##############################

/*
newton raphson
linear search 
bubble sort 

https://www.geeksforgeeks.org/searching-algorithms/

https://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/


Most famous ones are : KMP (Knuth Morris Pratt) , Rabin Karp and Finite State Automaton.


https://www.geeksforgeeks.org/c-program-for-kmp-algorithm-for-pattern-searching-2/

https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

https://www.tutorialspoint.com/c-program-for-kmp-algorithm-for-pattern-searching


https://tutorialspoint.dev/language/c-and-cpp-programs/searching-for-patterns-set-3-rabin-karp-algorithm

https://www.geeksforgeeks.org/finite-automata-algorithm-for-pattern-searching/

https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

https://www.programiz.com/dsa/binary-search-tree

https://www.codesdope.com/blog/article/binary-search-tree-in-c/

*/






