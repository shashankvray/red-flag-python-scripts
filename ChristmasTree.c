#include<stdio.h>
void right(int);
void left(int);

int K=1;
int Q=1;
int y;

int main()
{
  int i,m;
  printf("Enter the height: ");
  scanf("%d",&m);
  printf("%d\n",m);
  y=m;
  for(i=1;i<m;i++)
  printf(" ");
  printf("*\n");
  right(m);
}

void right(int m)
{
  int i;
  Q++;
  K++;
  if(K>=(m+1))  return;
  else
  {
   for(i=1;i<m;i++)
   printf(" ");
   for(i=0;i<Q;i++)
   printf("*");
   printf("\n");
   left(m);
  }
}

void left(int m)
{
  int i;
  K++;
  Q++;
  y-=2;
  if(K>=(m+1))  return;
  else
  {
   for(i=1;i<y;i++)
   printf(" ");
   for(i=0;i<Q;i++)
   printf("*");
   printf("\n");
   right(m);
  }
}