#include <stdio.h>

#define POINTCACHE 10000

int points[POINTCACHE];
int n = 0;
int houses = 0;

  struct {
    int x;
    int y;
  } location = {0};

void storepoint(int, int);
int searchpoint(int, int);
void action(void);

void storepoint(int x, int y)
{
  extern int n;
  extern int points[];
  points[n] = x;
  points[n+1] = y;
  n += 2;
}

int searchpoint(int x, int y)
{
  extern int n;
  extern int points[];
  int i;
  for (i = 0; i < n; i += 2){
    if (points[i] == x)
      if (points[i+1] == y)
        return 0;
  }
  return 1;
}

void action(){
  if (searchpoint(location.x,location.y)){
    ++houses;
    storepoint(location.x, location.y);
  }
}

int main(int argc, char *argv[])
{
  int c;
  
  FILE *fp;
  fp = fopen(argv[1], "r");

  action();
  
  while ((c = getc(fp)) != EOF){
    switch (c){
    case 'v':
      --location.y;
      action();
      break;
    case '^':
      ++location.y;
      action();
      break;
    case '>':
      ++location.x;
      action();
      break;
    case '<':
      --location.x;
      action();
      break;
    }
  }
  
  printf("%d\n",houses);
  return 0;
}

