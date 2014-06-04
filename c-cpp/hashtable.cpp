#include <iostream>
#include <cstdlib>
#include <cstring>
#define HASH_SIZE 100

using namespace std;

class Node
{
	public:
	char *key;
	int val;
	Node *next;

	Node();
};

class Hashtable
{

private:
	long createHash(char *);
	Node ** nodes;
	
public:
	Hashtable();
	const int operator [](char *);
	Node * find(char *key);
	bool put(char *key, int val);
 };

Node::Node()
{
	key = NULL;
	next = NULL;
}

Hashtable::Hashtable ()
{
	nodes = new Node*[HASH_SIZE];
	for(int i = 0; i < HASH_SIZE; i++)
	{
		nodes[i] = NULL;
	}
}

Node *Hashtable::find(char *key)
{
	long element = createHash(key);
	if(nodes[element] == NULL)
	{
		//cout << key << "not found" << endl;
		return NULL;
	}
	else
	{	// ACtually it needs to search for KEY within nodes!
		return nodes[element];
	}
}

const int Hashtable::operator[](char *key)
{
	return find(key)->val;
}

bool Hashtable::put(char *key, int val)
{
	if(find(key) != NULL)
		return false;
	else
	{
		Node *entry = new Node();
		entry->key = key;
		entry->val = val;
		entry->next = nodes[createHash(key)];
		nodes[createHash(key)] =  entry;
		return true;

	}

}


long Hashtable::createHash(char *key)
{
	long x = 0;
	for(unsigned int i = 0; i < strlen(key); i++)
	{
		x = (x << 3) ^ key[i];
	
	}
	return x % HASH_SIZE;
}

int main(void)
{
	Hashtable *x = new Hashtable();
	char *hola = "Hola";
	x->put(hola, 1);
	cout << (*x)[hola];



	return(0);
}
