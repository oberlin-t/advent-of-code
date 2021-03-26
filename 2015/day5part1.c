#include <stdio.h>
#include <string.h>

#define STRINGLENGTH 16

int checkVowel (char[]);
int checkRepeats (char[]);
int checkBadWords (char[]);

int checkVowel (char a[])
{
  int vowels = 0;
  int i;
  for (i = 0; i < STRINGLENGTH; i++){
    switch(a[i]){
    case 'a': case 'o': case 'e': case 'u':case 'i':
      vowels++;
      break;
    }
  }
  if (vowels >= 3){
    return 1;
  }
  return 0;
}

int checkRepeats (char a[])
{
  int i;
  char temp = a[0];
  for (i = 1; i < STRINGLENGTH; i++){
    if (a[i] == temp)
      return 1;
    temp = a[i];
  }
  return 0;
}

int checkBadWords (char a[])
{
  int i;
  char temp = a[0];
  for (i = 1; i < STRINGLENGTH; i++){
    if (a[i] == 'b' && temp == 'a'){
      return 0;
    }
    if (a[i] == 'd' && temp == 'c'){
      return 0;
    }
    if (a[i] == 'q' && temp == 'p'){
      return 0;
    }
    if (a[i] == 'y' && temp == 'x'){
      return 0;
    }
    temp = a[i];
  }
  return 1;
}

int main(int argc, char *argv[])
{
  int c;
  int goodStrings = 0;
  char instr[STRINGLENGTH] = { 0 };
  
  FILE *fp;
  fp = fopen(argv[1], "r");

  while ((fscanf(fp, "%s\n", &instr)) == 1){
    if (checkVowel(instr) && checkRepeats(instr) && checkBadWords(instr)){
      goodStrings++;
    }
  }
  printf("%d\n",goodStrings);
  return 0;
}

