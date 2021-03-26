#include <stdio.h>

int main(int argc, char *argv[])
{
  int c, total = 0, pos = 0;
  
  FILE *fp;
  fp = fopen(argv[1], "r");

  while ((c = getc(fp)) != EOF){
   
    if (total < 0){
      printf("%d\n",pos);
      return 0;
    }

    ++pos;

    if (c == '(')
      ++total;

    if (c == ')')
      --total;
  }
}
