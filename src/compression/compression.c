#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getBits(int s, char *array) {
  // itoa(s, bitarray, 2);
  sprintf(array, "%x", s); // converts to hexadecimal base.
}

int compress(int s) {}

int main() {
  char bitarray[32 + 1];
  getBits(4, bitarray);
  printf("%s", bitarray);
}