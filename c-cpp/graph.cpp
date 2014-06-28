#include <iostream>
#include <cstdlib>


using namespace std;

class Vertex;

class Node
{
private:
	Node();

public:
	int val;
	Vertex *adjacent;
	Node(int val);
	bool	AddPath(Vertex *, Node *, int );
};


class Vertex
{
	Vertex();
public:	
	Vertex(int newWeight);
	Vertex *next;
	int weight;
	Node *destination;
};

Vertex::Vertex(int newWeight) : weight(newWeight)
{
	next = NULL;
	destination = NULL;
}

class Graph
{
private:
	Graph();
	int maxNode;
	int maxVertex;
	int curVertex;
	int curNode;
public:
	Vertex **vertices;
	Node **nodes;
	Graph(int maxVert, int maxNodes);	
	bool AddNode(Node *n);
};

Graph::Graph(int maxVert, int maxNodes) : maxNode(maxNodes), maxVertex(maxVert)
{
	vertices = new Vertex*[maxVert]();
	nodes = new Node*[maxNodes]();
	curNode = curVertex = 0;

}


Node::Node()
{

}

bool Node::AddPath(Vertex *v, Node *dest, int w)
{
	v->weight = w;
	v->destination = dest;
	if(adjacent == NULL)
	{
		adjacent = v;
	}
	else
	{
		Vertex *ptr; 
		for(ptr = adjacent; ptr->next != NULL ; ptr = ptr->next)
		{}
		ptr->next  = v;
		v->next = NULL;
	}
	return true;
}

Node::Node(int newVal): val(newVal)
{
	cout << "Hola" << endl;
	adjacent = NULL;	
	
}

bool Graph::AddNode(Node *n)
{
	if(curNode < (maxNode -1))
	{
		nodes[curNode++] = n;

	}
	else
	{
		cout << "Error" << endl;
	}	
	return true;
}


int main(void)
{
	Graph *g = new Graph(128,32);
	g->AddNode(new Node(1));
	g->AddNode(new Node(2));
	g->AddNode(new Node(3));
	g->nodes[1]->AddPath(new Vertex(12), g->nodes[2], 2);
	return 0;
}

