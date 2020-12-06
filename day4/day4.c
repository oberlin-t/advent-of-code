#include <stdio.h>
#include <string.h>

#define CHARZ 21172

int main()
{
  FILE *fp; 
  fp = fopen("./input.txt", "r");  
  int parts, total, len, blah,blah2;
  total = 0;
  blah2 = blah = 0;
  char string[CHARZ];

  while (fgets (string, CHARZ, fp) != NULL){
    len = strlen(string);
    for (int i = 0; i < len; ++i){
      if (string[i] == ':'){
        if (string[i - 3] == 'b'){
          ++parts;
        }
        if (string[i - 3] == 'i')
          ++parts;
        if (string[i - 3] == 'p')
          ++parts;
        if (string[i - 3] == 'e'){
          if (string[i - 2] == 'c')
            ++parts;
          if (string[i - 2] == 'y')
            ++parts;
        }
        if (string[i - 3] == 'h'){
          if (string[i - 2] == 'g'){
            ++parts;
          }
          if (string[i - 2] == 'c'){
            ++parts;
          }
        }
      }
    }
  
    if (blah == 1)
      ++blah2;
    if (*string == '\n'){
      if (parts == 7){
        ++total;
      }
      parts = 0;
    }
    }

  if (parts == 7){
    ++total;
  }
  parts = 0;
  printf("%d\n%d\n",total);
  return 0;
}
