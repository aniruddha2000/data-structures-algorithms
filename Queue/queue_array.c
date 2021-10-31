#include <stdio.h>

#define SIZE 10

int queue[SIZE], front = -1, rear = -1;

void enqueue(int val)
{
  if (rear + 1 == SIZE)
  {
    printf("Overflow\n");
  }
  else
  {
    if (front == -1 && rear == -1)
    {
      front = 0;
      rear = 0;
    }
    else
    {
      rear += 1;
    }
    queue[rear] = val;
  }
}

void dequeue()
{
  if (front == -1 || front > rear)
  {
    printf("Underflow\n");
  }
  else
  {
    if (front == rear)
    {
      front = rear = -1;
    }
    else
    {
      front += 1;
    }
  }
}

void display()
{
  if (front == -1 || rear == -1)
  {
   printf("Queue is empty\n");
  }
  else
  {
    printf("Queue elements are:\n");
    for (int i = front; i <= rear; i++)
    {
      printf("%d\t", queue[i]);
    }
    printf("\n");
  }
}


void main()
{
  display();
  enqueue(16);
  enqueue(10);
  enqueue(14);
  display();
  dequeue();
  display();
}
