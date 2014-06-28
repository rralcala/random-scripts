#include <iostream>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include "queue.cpp"

using namespace std;

class Node
{
	
	Node *child;
	Node *nextsibling;
	public:
int val;
	Node * operator[](int child);
	bool addChild(Node *);
	Node(int val);
	void dfs();
	void bfs();
};

	void Node::dfs()
	{
		cout << val << endl;
		Node *ptr = child;
		while(ptr != NULL)
		{
			ptr->dfs();
			ptr = ptr->nextsibling;
		}
	}

	void Node::bfs()
	{
		Queue<Node *> *q= new Queue<Node *>();
		Node *ptr = child;
		if(ptr != NULL)
		{
			q->push(this);
			while(q->first != NULL)
			{
				ptr = q->pop();
				cout << ptr->val << endl;
				ptr = ptr->child;
				while(ptr != NULL)
				{
					q->push(ptr);
					ptr = ptr->nextsibling;
				}
			}
		}
	
	}
	
	bool Node::addChild(Node *newChild)
	{
		if(child == NULL)
			child = newChild;
		else
		{
			Node *ptr = child;
			while(ptr->nextsibling != NULL)
			{
				ptr = ptr->nextsibling;
			}
			//newChild = ptr->nextsibling;
			ptr->nextsibling = newChild;
			
		}
		return true;
	}

	Node::Node(int newval)
	{
		nextsibling = child = NULL;
		// = NULL;
		val = newval;
	}

	Node *Node::operator[](int reqchild)
	{
		Node *ptr = child;
		for(int i = 0; (ptr != NULL) && i < (reqchild); i++)
		{
			ptr = ptr->nextsibling;
		}
		return ptr;
	}

	

int main(void)
{
	srand(time(NULL));

	Node * ptr, *root;
	ptr = root = new Node(rand());
/*int ctr = 0;
	for(int i = 0; i < 100; i++)
	{
		if(rand() % 2)
		{
			ptr->addChild(new Node(ctr++));
		}
		else
		{
			int child = rand() % 2;
			if((*ptr)[child] != NULL)
				ptr = (*ptr)[child];
		}
	}*/
	ptr->addChild(new Node(1));
ptr->addChild(new Node(2));
ptr->addChild(new Node(3));
ptr = (*ptr)[0];
//cout << (*ptr)[2]->val << endl;
ptr->addChild(new Node(4));
ptr->addChild(new Node(5));
ptr = (*ptr)[1];
ptr->addChild(new Node(6));
ptr->addChild(new Node(7));
ptr->addChild(new Node(8));
	root->bfs();
	


	return 0;
}
