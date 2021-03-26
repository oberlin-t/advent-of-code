#include <stdio.h>

#define POINTCACHE 10000

int points[POINTCACHE];
int n = 0;
int houses = 0;

struct {
  int x;
  int y;
} location = {0}, robo = {0};



void storepoint(int, int);
int searchpoint(int, int);
void action(int,int);

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

void action(int x,int y){
  if (searchpoint(x,y)){
    ++houses;
    storepoint(x,y);
  }
}

int main(int argc, char *argv[])
{
  int c, n = 0;
  
  FILE *fp;
  fp = fopen(argv[1], "r");

  action(location.x,location.y);
  
  while ((c = getc(fp)) != EOF){
    switch (c){
    case 'v':
      if (n % 2 == 0){
        --location.y;
        action(location.x, location.y);
      } else {
        --robo.y;
        action(robo.x, robo.y);
      }
      break;
    case '^':
      if (n % 2 == 0){
        ++location.y;
        action(location.x, location.y);
      } else {
        ++robo.y;
        action(robo.x, robo.y);
      }
      break;
    case '>':
      if (n % 2 == 0){
        ++location.x;
        action(location.x, location.y);
      } else {
        ++robo.x;
        action(robo.x, robo.y);
      }
      break;
    case '<':
      if (n % 2 == 0){
        --location.x;
        action(location.x, location.y);
      } else {
        --robo.x;
        action(robo.x, robo.y);
      }
      break;
    }
    ++n;
  }
  
  printf("%d\n",houses);
  return 0;
}

