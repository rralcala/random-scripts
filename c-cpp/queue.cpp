#include <iostream>
using namespace std;
template <class T>
class Element
{
	public:
	T val;
	Element *next;
	Element(T newval);
};

template <class T>
Element<T>::Element(T newval)
{
	val = newval;
	next = NULL;
}

template <class T>
class Queue
{
public:
	Element<T> *first;
	Element<T> *last;
	int count;
	
	Queue();
	void push(T val);
	T pop();
	
};

template <class T>
Queue<T>::Queue()
{
	count = 0;
	first = last = NULL;
	 
}
template <class T>
void Queue<T>::push(T val)
{
	cout << "Pushing" << val << endl;
	Element<T> *ptr = new Element<T>(val);
	ptr->next = NULL;
	
	if(last != NULL)
		last->next = ptr;
	last = ptr;
	if(first == NULL)
		first = last;
}

template <class T>
T Queue<T>::pop( )
{

	if(first != NULL)
	{
		Element<T> *selected = first;
		T retval = first->val;
		first = selected->next;
		delete selected;
		
		return retval;
	}else
	{ cout << "first is null\n";}

	first = last;
	return NULL;
}

