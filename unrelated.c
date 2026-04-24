#include <yak/config.h>

void foo() {
  // this file does not include any C O N F I G _ T E S T variable even though it
  // includes the generated header
  #if CONFIG_TEST_UNRELATED
  #warning "unrelated!"
  #endif
}
