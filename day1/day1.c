#include <stdio.h>
#include <math.h>

#define NUMUVNUMZ 200

int input [NUMUVNUMZ];
int ans1;
int ans2;

int main(){
  FILE* data = fopen("./input.txt", "r");

  for (int l = 0; l < 200; ++l) {
    fscanf(data, "%d", &input[l]); 
  }
  
  for(int i = 0; i < NUMUVNUMZ; ++i){
    for(int j = 0; j < NUMUVNUMZ; ++j){
      if (input[i] + input[j] == 2020){
        ans1 = i;
        ans2 = j;
        break;
      }
    }
  }
  int finan = input[ans1] * input[ans2];
  printf("%d\n",finan);
  return 0;
}
