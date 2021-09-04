#include <stdio.h>

#define STRSIZE 10
#define ROWS 127
#define COLUMNS 7

int getid(char []);

int getid(char instr[]){
  struct {
    int min;
    int max;
  } row, column;
  
  row.max = ROWS;
  row.min = 0;
  column.max = COLUMNS;
  column.min = 0;
  int i;
  
  for (i = 0; i < STRSIZE; ++i){
    
    switch(instr[i]){
    case 'F':
      row.max = ((row.max - row.min) / 2) + row.min;
      //printf("F min:%d max:%d\n",row.min,row.max);
      break;
    case 'B':
      row.min = ((row.max - row.min) / 2) + 1 + row.min;
      //printf("B min:%d max%d\n",row.min,row.max);
      break;
    case 'L':
      column.max = ((column.max - column.min) / 2) + column.min;
      break;
    case 'R':
      column.min = ((column.max - column.min) / 2) + 1 + column.min;      
      break;
    }
  }

  if(row.min != row.max){
    printf("oof\n");
  }
  
  return (row.min * 8) + column.min;
}

int main(int argc, char *argv[])
{
  int c;
  int highest = 0;
  char instr[STRSIZE];

  FILE *fp;
  fp = fopen(argv[1], "r");

  while ((fscanf(fp,"%s\n",&instr)) == 1){
    printf("%d\n",getid(instr));
    if (getid(instr) > highest){
      highest = getid(instr);
    }
  }
  printf("%d\n",highest);
  return 0;  
}
