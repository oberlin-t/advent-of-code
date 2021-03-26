#include <stdio.h>
#include <string.h>
#define NA 0
#define NOW 1



int main(){
  FILE* data = fopen("./input.txt", "r");
  char string[20882];
  int c,doit,i,min, max;
  int bn = 0;
  int firstLen;
  int secLen;
  char searchChar;
  int localCount = 0;
  int total = 0;
  int count = 0;
  
  for (i = 0; fscanf(data, "%s", &string) != EOF; ++i ){
    int len = strlen(string);
    for(int j = 0; j < len; ++j){
      if (string[j] == '-'){ //this matches with (*)
        firstLen = j;
        secLen = len - j - 1;
        
        if (firstLen == 1){
          min = string[j-1] - '0';
                }
        if (secLen == 1){
          max = string[j+1] - '0';
                }
        if (firstLen == 2){
          min = ((string[j-2] - '0') * 10) + (string[j-1] - '0');
                }
        if (secLen == 2){
          max = ((string[j+1] - '0') * 10) + (string[j+2] - '0');
                } 
        doit = NA;
        } // this matches with (*)
        if(string[j] == ':'){
          searchChar = string[j-1];
        doit = NA;
                }

        
        
        //        printf("%c\n",string[1]);
        /*
        if (string[j] ){
          if((string[min] != searchChar && string[max] == searchChar) || (string[min] == searchChar && string[max] != searchChar))
            if(string[min+1] != ':')
              ++total;
        */
        //  }
    }
      if (doit == NOW)
        if ((string[min-1] != searchChar && string[max-1] == searchChar) || (string[min-1] == searchChar && string[max] != searchChar))
          ++total;
      doit = NOW;
    
    
    
    }
printf("%d\n",total);
  return 0; 
  }
 

 

