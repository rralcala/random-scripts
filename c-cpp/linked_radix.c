#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define list_entry(ptr, type, member) ((type *)((char *)(ptr)-(unsigned long)(&((type *)0)->member)))
#define ARR_SIZE 2048

/* Kernel style doubly linked list */
struct list_head 
{
	struct list_head *next;
	struct list_head *prev;
};

/* Dumb struct */
struct int_list
{
	int val;
	struct list_head list;	
};

/* Un link an element */
static inline void _list_del(struct int_list *cur)
{
	cur->list.prev->next = cur->list.next;
	cur->list.next->prev = cur->list.prev;
}

/* Remove an element from the list */
void list_del(struct int_list *cur)
{
	_list_del(cur);
	free (cur);
}

/* Link an element to a list */
static inline struct int_list *_list_add(struct int_list *cur, struct int_list *prev, struct int_list *next)
{
	cur->list.prev = &prev->list;
	cur->list.next = &next->list;
	
	prev->list.next = &cur->list;
	next->list.prev = &cur->list;
	return cur;
}

/* Create an uninitialized element at the specified position */
static inline struct int_list *list_add(struct int_list *prev, struct int_list *next)
{
	return _list_add(malloc(sizeof(struct int_list)), prev, next);
}

struct int_list *radix_sort(struct int_list *arr)
{
	int i,j, pos = 10;
	struct int_list *head, *next_element, *digits[10];
	
	for(i = 0; i < 10; i++)
	{
		digits[i] = NULL;
	}
	
	for(j = 0; j < 10; j++)
	{
		/* Group Phase */
		for(i = 0; i < ARR_SIZE; i++)
		{
			next_element = list_entry(arr->list.next, struct int_list, list);
			
			if(digits[(arr->val % pos) / (pos / 10)] == NULL)
			{
				digits[(arr->val % pos) / (pos / 10)] = arr;
				_list_del(arr);
				_list_add(arr, arr, arr);
			}
			else
			{				
				_list_del(arr);
				_list_add(arr, list_entry(digits[(arr->val % pos) / (pos / 10)]->list.prev, struct int_list, list), digits[(arr->val % pos) / (pos / 10)]);
				
			}

			arr = next_element;
		}
		/* Merge phase */
		head = arr = NULL;
		for(i = 0; i < 10; i++)
		{
			if(digits[i] != NULL)
			{
				if(head == NULL) 
					head = digits[i];
				if(arr != NULL)
				{
					struct list_head *ap = arr->list.prev;
					arr->list.prev->next = &digits[i]->list; /* a'->next */
					arr->list.prev = digits[i]->list.prev; /* a->prev */
					digits[i]->list.prev->next = &arr->list; /*d'->next */
					digits[i]->list.prev = ap; /*d->prev */
					
				} else {
					arr = head; /* This is here because I want to skip the first loop. */
				}
				digits[i] = NULL;
			}
		} 
		pos *= 10;
	}
	return head;
}

int main(void)
{
	struct int_list *arr = NULL, *head = NULL;
	int i,j;
	int pos = 10; 

	/* Init Code */
	srand(time(NULL));


	/* Create de random Dumb list */
	head = malloc(sizeof(struct int_list));	
	arr = head;
	arr->list.next = &arr->list;
	arr->list.prev = &arr->list;
	for(i = 0; i < ARR_SIZE; i++)
	{
		arr->val = rand() % 1000;
		arr = list_add(arr, head);
	}

	
	/* Radix Sort */
	arr = head = radix_sort(head);

	/* Print Loop */
	for(i = 0; i < ARR_SIZE; i++)
	{
		printf("%d\n", arr->val);
		arr = list_entry(arr->list.next, struct int_list, list);
	}


	/* List Deletion */
	arr = head;
	for(i = 0; i < ARR_SIZE; i++)
	{
		arr = list_entry(arr->list.next, struct int_list, list);
		list_del(list_entry(arr->list.prev, struct int_list, list));
	}
	
	exit (0);
}
