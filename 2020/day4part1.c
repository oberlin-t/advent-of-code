#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define STRINGSIZE 400

int year(char[],char[],int,int);
int hgt(char[]);
int hcl(char[]);
int ecl(char[]);
int pid(char[]);

int year(char instr[],char pattern[], int min, int max)
{
  char *p;
  int yr;
  if ((p = strstr(instr,pattern)) == NULL)
    return 0;
  yr = ((*(p+4)-'0') * 1000) + ((*(p+5)-'0') * 100) + ((*(p+6)-'0') * 10) + (*(p+7)-'0');

  if(yr >= min && yr <= max)
    return 1;

  return 0;
}

int hgt(char instr[])
{
  char *p;
  int i;
  int distance = 1;
  int height;
  
  if ((p = strstr(instr,"hgt")) == NULL)
    return 0;
  
  for (i = 4 ;; ++i){
    if (*(p+i) == 'i' && *(p+i+1) == 'n'){
        while (*(p+i-distance) != *p){
          ++distance;
        }
        if (distance == 6){
          height = ((*(p+4)-'0') * 10) + (*(p+5)-'0');
        }
        if (distance == 7){
          height = ((*(p+4)-'0') * 100) + ((*(p+5)-'0') * 10) + (*(p+6)-'0');
        }
        if (height >= 59 && height <= 76)
          return 1;
    } else if(*(p+i) == 'c' && *(p+i+1) == 'm'){
      while (*(p+i-distance) != *p){
        ++distance;
      }
        if (distance == 6){
          height = ((*(p+4)-'0') * 10) + (*(p+5)-'0');
        }
        if (distance == 7){
          height = ((*(p+4)-'0') * 100) + ((*(p+5)-'0') * 10) + (*(p+6)-'0');
        }
        if (height >= 150 && height <= 193)
          return 1;
        
    } else if(*(p+i) == ' ' || *(p+i) == '\n')
      break;
  }
  return 0;
}

int hcl(char instr[])
{
  char *p;
  int i;
  if ((p = strstr(instr,"hcl:#")) == NULL)
    return 0;

  for (i = 5; i<=10; i++){
    if (!((*(p+i) >= 'a' && *(p+i) <= 'f') || isdigit(*(p+i) ))){
      return 0;
    } 
  }
  
  return 1;
}

int ecl(char instr[])
{
  if (strstr(instr,"amb") != NULL)
    return 1;
  if (strstr(instr,"blu") != NULL)
    return 1;  
  if (strstr(instr,"brn") != NULL)
    return 1;
  if (strstr(instr,"gry") != NULL)
    return 1;  
  if (strstr(instr,"grn") != NULL)
    return 1;  
  if (strstr(instr,"hzl") != NULL)
    return 1;
  if (strstr(instr,"oth") != NULL)
    return 1;
  return 0;
}

int pid(char instr[])
{
  char *p;
  int i;
  
  if ((p = strstr(instr,"pid:")) == NULL)
    return 0;

  for (i = 4; i <= 12; ++i){
    if (!isdigit(*(p+i)))
      return 0;
  }
 
  if (*(p+13) != ' ')
    if (*(p+13) != '\n')
      return 0;
    
  return 1;
}


int main(int argc, char *argv[])
{
  char instr[STRINGSIZE];
  int c;
  int j;
  int i = 0;
  int total = 0;
  char temp = 1;

  FILE *fp;
  fp = fopen(argv[1], "r");

  while (c != EOF){
    while ((c = getc(fp)) != EOF){
      if (c == '\n' && temp == '\n'){
        if (year(instr,"byr",1920,2002) && year(instr,"iyr",2010,2020) && year(instr,"eyr",2020,2030) && hgt(instr) && hcl(instr) && ecl(instr) && pid(instr))
          ++total;
        for (j=0; j<STRINGSIZE; j++){
          instr[j] = 0;
        }
        i = 0;
        break;
      }
      temp = c;
      instr[i] = c;
      i++;
    }
  }
  printf("%d\n",total);
  return 0;
}
