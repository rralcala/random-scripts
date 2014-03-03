#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Crappy on IO but PIPE compatible 
   Nice on memory.
*/


char *readline(FILE *fp, size_t size)
{
  char *buff = (char *)malloc(size * sizeof(char));
  size_t times = 1;
  if(fgets(buff, size, fp) == NULL)
    return NULL;
  while((strlen(buff) == size-1) && buff[size-2] != '\n')
  {
    buff = (char *)realloc(buff, ++times*size*sizeof(char));
    if( fgets(buff + (times - 1)*size - 1,size, fp) == NULL ) 
      break;
  }
  
  return buff;
}

char **tail(FILE *fp, size_t n, size_t buffsize, int *pos)
{
   char **lines;
   size_t current = 0;
   lines = (char **)calloc(n, sizeof(char *));
   char *newline;
   while((newline = readline(fp, buffsize)) != NULL)
   { 
     if ( lines[current % n] != NULL )
     { 
       free(lines[current % n]); 
     }
     lines[current++ % n] = newline;
   }
   *pos = current % n;
   return lines;
}

int main(int argc, char **argv)
{
  char **lines;
  int n, i;
  int pos = 0;

  if(argc < 2 || (n = atoi(argv[1])) < 1)
  {
    printf("You should enter the number of lines as the first paramenter.\n");
    exit(1);
  }
  lines = tail(stdin, n, BUFSIZ, &pos);

  for(i = 0; i < n; i++)
  {  
    if(lines[(pos + i) % n] != NULL)
       printf("%s", lines[(pos + i) % n]);
  }
  exit(0);
}

