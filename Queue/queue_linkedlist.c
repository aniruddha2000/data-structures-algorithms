#include <stdio.h>
#include <stdlib.h>

struct Node
{
  int data;
  struct Node *next;
};

typedef struct Node *NODEPTR;

NODEPTR front = NULL;
NODEPTR rear = NULL;

NODEPTR getnode()
{
  NODEPTR new;
  new = (NODEPTR)malloc(sizeof(struct Node));
  return new;
}

void enqueue(int val)
{
  NODEPTR newNode;
  newNode = getnode();
  newNode->data = val;
  newNode->next = NULL;
  if (front == NULL)
  {
    front = newNode;
    rear = newNode;
  }
  else
  {
    rear->next = newNode;
    rear = newNode;
  }
}

void dequeue()
{
  if (front == NULL)
  {
    printf("Queue is empty\n");
  }
  NODEPTR tmp;
  tmp = front;
  if (front == rear)
  {
    front = NULL;
    rear = NULL;
  }
  else
  {
    front = front->next;
  }
  free(tmp);
}

void display()
{
  if (front == NULL)
  {
    printf("Queue is empty\n");
  }
  else
  {
    NODEPTR tmp = front;
    while (tmp->next != NULL)
    {
      printf("%d ->\t", tmp->data);
      tmp = tmp->next;
    }
    printf("NULL\n");
  }
}

int main()
{
  display();
  enqueue(19);
  enqueue(14);
  enqueue(10);
  enqueue(8);
  display();
  dequeue();
  display();
  return 0;
}
