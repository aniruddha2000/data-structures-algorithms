#include <stdio.h>
#include <stdlib.h>

struct Node
{
  int data;
  struct Node *next;
};

typedef struct Node *NODEPTR;

NODEPTR head = NULL;

NODEPTR getnode()
{
  NODEPTR new;
  new = (NODEPTR)malloc(sizeof(struct Node));
  return new;
}

void push(int val)
{
  NODEPTR newNode;
  newNode = getnode();
  newNode->data = val;
  newNode->next = head;
  head = newNode;
}

void pop()
{
  if (head == NULL)
  {
    printf("Stack is empty\n");
  }
  NODEPTR tmp;
  tmp = head;
  head = head->next;
  free(tmp);
}

void display()
{
  if (head == NULL)
  {
    printf("Stack is empty\n");
  }
  else
  {
    NODEPTR tmp;
    tmp = head;
    while (tmp != NULL)
    {
      printf("%d -> \t", tmp->data);
      tmp = tmp->next;
    }
    printf("NULL\n");
  }
}

int main()
{
  display();
  push(19);
  push(14);
  push(10);
  push(8);
  display();
  pop();
  display();
  return 0;
}
