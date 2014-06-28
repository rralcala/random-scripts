#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define list_entry(ptr, type, member) ((type *)((char *)(ptr)-(unsigned long)(&((type *)0)->member)))
#define ARR_SIZE 100

static inline void swap(int *a, int *b)
{
	int tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}


void heapify(int *arr, int size, int pos)
{
	int l1 = -1, l2 = -1;
	if(pos > size)
		return;
	if((2*pos + 1)  <= size)
	{
		l1 = (2*pos) + 1 ;
	}

	if((2*pos +2) <= size)
	{
		l2 = (2*pos) + 2;
	}
	if(l1 >= 0 && arr[l1] > arr[pos] && arr[l1] > arr[l2])
	{
		printf("L1 Swap = %d R%d %d\n",pos,arr[pos],arr[l1]);
		swap(&(arr[l1]),&(arr[pos]));

		heapify(arr, size, l1);

	} else
	if( l2 >= 0 && arr[l2] > arr[pos])
	{
		printf("L2 Swap = %d R%d %d\n",pos,arr[pos],arr[l2]);
		swap(&(arr[l2]),&(arr[pos]));
		heapify(arr, size, l2);
	}
}

void print_tree(int *arr, int level)
{
	int i;
	for(i = level - 1; i < (level*2 - 1); i++)
	{
		if(i >= ARR_SIZE) 
			break;
		printf(" %d",arr[i]);
	}
	printf("\n%d\n",level); if(i == (level*2 - 1))
	print_tree(arr, level * 2);
}


void build_heap(int *arr)
{
	int i;
	for(i=ARR_SIZE/2;i>=0;i--)
	{
		
		heapify(arr,ARR_SIZE,i);
	}
}

void heap_sort(int *arr)
{
	int i = 0;
	build_heap(arr);
	for(;i<ARR_SIZE;i++)
	{
		swap(&(arr[0]),&(arr[ARR_SIZE-i-1]));
		heapify(arr,ARR_SIZE-i-2,0);
	}
}

int main(void)
{
	int i;
	int *arr;
	/* Init Code */
	srand(time(NULL));


	/* Create de random Dumb list */
	arr = malloc(sizeof(int)*ARR_SIZE);	
	for(i = 0; i < ARR_SIZE; i++)
	{
		arr[i] = rand() % 1000;
	}

	
	/* Radix Sort */
	i = 0;
	
	/* Print Loop */
	print_tree(arr, 1);
	heap_sort(arr);

	print_tree(arr, 1);


	/* List Deletion */
	free(arr);
	
	exit (0);
}
