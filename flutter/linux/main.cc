#include <dlfcn.h>
#include "my_application.h"

#define SODESK_LIB_PATH "libsodesk.so"
// #define SODESK_LIB_PATH "/usr/lib/sodesk/libsodesk.so"
typedef bool (*RustDeskCoreMain)();

bool flutter_sodesk_core_main() {
   void* libsodesk = dlopen(SODESK_LIB_PATH, RTLD_LAZY);
   if (!libsodesk) {
     fprintf(stderr,"load libsodesk.so failed\n");
     return true;
   }
   auto core_main = (RustDeskCoreMain) dlsym(libsodesk,"sodesk_core_main");
   char* error;
   if ((error = dlerror()) != nullptr) {
       fprintf(stderr, "error finding sodesk_core_main: %s", error);
       return true;
   }
   return core_main();
}

int main(int argc, char** argv) {
  if (!flutter_sodesk_core_main()) {
      return 0;
  }
  g_autoptr(MyApplication) app = my_application_new();
  return g_application_run(G_APPLICATION(app), argc, argv);
}
