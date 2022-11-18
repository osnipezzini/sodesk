Push-Location flutter ; flutter pub get ; Pop-Location
~/.cargo/bin/flutter_rust_bridge_codegen --rust-input src/flutter_ffi.rs --dart-output flutter/lib/generated_bridge.dart
python build.py --portable --hwcodec --flutter