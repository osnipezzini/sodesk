#include <dlfcn.h>
#include "my_application.h"

#define RUSTDESK_LIB_PATH "libsodesk.so"
// #define RUSTDESK_LIB_PATH "/usr/lib/rustdesk/libsodesk.so"
typedef bool (*RustDeskCoreMain)();

bool flutter_rustdesk_core_main() {
   void* libsodesk = dlopen(RUSTDESK_LIB_PATH, RTLD_LAZY);
   if (!libsodesk) {
     fprintf(stderr,"load libsodesk.so failed\n");
     return true;
   }
   auto core_main = (RustDeskCoreMain) dlsym(libsodesk,"rustdesk_core_main");
   char* error;
   if ((error = dlerror()) != nullptr) {
       fprintf(stderr, "error finding rustdesk_core_main: %s", error);
       return true;
   }
   return core_main();
}

int main(int argc, char** argv) {
  if (!flutter_rustdesk_core_main()) {
      return 0;
  }
  g_autoptr(MyApplication) app = my_application_new();
  return g_application_run(G_APPLICATION(app), argc, argv);
}
