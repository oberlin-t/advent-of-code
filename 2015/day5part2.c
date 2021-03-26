#include <stdio.h>
#include <string.h>

#define STRINGLENGTH 16

int checkPair (char[]);
int checkBetween (char[]);

int checkPair (char a[])
{
  int i;
  int j;
  for (i = 0; i < STRINGLENGTH; i++){
    for (j = 0; j < STRINGLENGTH - 1; j++){
      if (a[i] == a[j] && a[i+1] == a[j+1]){
        if (i != j && i != j+1 && i != j-1){
          return 1;
           }
      }
    }
  }
  return 0;
}

int checkBetween (char a[])
{
  int i;
  for (i = 0; i < (STRINGLENGTH - 2); i++){
    if (a[i] == a[i + 2]){
      return 1;
    }
  }
  return 0;
}

int main(int argc, char *argv[])
{
  int c;
  int goodStrings = 0;
  char instr[STRINGLENGTH] = { 0 };
  
  FILE *fp;
  fp = fopen(argv[1], "r");

  while ((fscanf(fp, "%s\n", &instr)) == 1){
    if (checkPair(instr) && checkBetween(instr)){
      goodStrings++;
      printf("%s\n",instr);
    }
  }
  
  printf("%d\n",goodStrings);
  return 0;
}

