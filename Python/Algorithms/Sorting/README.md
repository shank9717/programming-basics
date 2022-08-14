# Introduction to the most popular sorting algorithms

1. Bubble Sort 
   
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

**Worst and Average Case Time Complexity: O(N^2)** - The worst case occurs when an array is reverse sorted.

**Best Case Time Complexity: O(N)** - The best case occurs when an array is already sorted.

**Auxiliary Space: O(1)**

2. Selection Sort
   
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

**Time Complexity**: O(N^2)

**Auxiliary Space**: O(1)

3. Insertion Sort
   
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

**Time Complexity**: O(N^2)

**Auxiliary Space**: O(1)

4. Merge Sort
   
The Merge Sort algorithm is a sorting algorithm that is considered as an example of the divide and conquer strategy. So, in this algorithm, the array is repeatedly divided into two equal halves and then they are combined in a sorted manner.

**Time Complexity**: O(n logn), 

Time complexity can be expressed as following recurrence relation.
`T(n) = 2T(n/2) + θ(n)`

**Auxiliary Space**: O(n)

5. Quick Sort
   
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.

Time taken by QuickSort, in general, can be written as follows. 

` T(n) = T(k) + T(n-k-1) + O(n)`

**Average Time Complexity**: O(n Logn)

**Auxiliary Space**: O(n)

6. Heap Sort
   
Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the minimum element and place the minimum element at the beginning. We repeat the same process for the remaining elements.

**Time Complexity**: O(n logn)

7. Counting Sort
   
Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then do some arithmetic to calculate the position of each object in the output sequence. 

**Time Complexity**: O(n+k) where n is the number of elements in the input array and k is the range of input. 

**Auxiliary Space**: O(n+k)

8. Radix Sort
   
Counting sort is a linear time sorting algorithm that sort in O(n+k) time when elements are in the range from 1 to k. The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. Radix sort uses counting sort as a subroutine to sort.

**Time Complexity**: O((n+b) * logb(k)),  where b is the base for representing numbers, for example, for the decimal system, b is 10

**Auxiliary Space**: O(n+k)