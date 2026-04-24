#include <stdio.h>
#include <yak/config.h>
#include "test.h"

int main(int argc, char *argv[])
{
  #if CONFIG_TEST
  printf("Test is set!\n");
  #else
  printf("Test is unset!\n");
  #endif

  return 0;
}
