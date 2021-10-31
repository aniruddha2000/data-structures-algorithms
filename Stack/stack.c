#include <stdio.h>

#define SIZE 10

int stack[SIZE], top = -1;

int main()
{
  display();
  push(19);
  push(34);
  display();
  push(6);
  push(17);
  display();
  pop();
  display();
  return 0;
}

void push(int value)
{
  if (top == SIZE - 1)
  {
    printf("Stack is full!\n");
  }
  else
  {
    top++;
    stack[top] = value;
  }
}

void pop() {
  if (top == -1)
  {
    printf("Stack is empty!\n");
  }
  else
  {
    top--;
  }
}

void display()
{
  if (top == -1)
  {
    printf("Stack is empty\n");
  }
  else
  {
    printf("Stack elements are:\n");
    for (int i = 0; i <= top; i++)
    {
      printf("%d\t", stack[i]);
    }
    printf("\n");
  }
}
