#include <stdio.h>

int smallest(int,int,int);
int secondsmallest(int, int, int);

int smallest(int a, int b, int c)
{
  if (a <= b){
    if (a <= c){
      return a;
    }
  }
  else if (b <= c){
    return b;
  }
  else {
    return c;
  }
}

int secondsmallest(int a, int b, int c)
{
  int i = smallest(a,b,c);
  if (a != i && ((a <= b) || (a <= c)))
    return a;
  else if (b != i && ((b <= a) || (b <= c)))
    return b;
  else if (c != i && ((c <= a) || (c <= b)))
    return c;
}


int main(int argc, char *argv[])
{
  int a,b,c,total = 0; 
  
  FILE *fp;
  fp = fopen(argv[1], "r");
  
  while ((fscanf(fp,"%dx%dx%d\n",&a,&b,&c)) == 3){
    total += (2 * (a * b)) + (2 * (b * c)) + (2 * (a * c)) + (smallest(a,b,c) * secondsmallest(a,b,c)); 
  }
    printf("%d\n",total);
    return 0;
}
