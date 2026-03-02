[app]
 title = Tasbih
 package.name = tasbih
 package.domain = org.exemple
 source.dir = .
 source.include_exts = py,png,jpg,kv,atlas,json,ttf
 version = 1.0.0
 requirements = python3,hostpython3,setuptools,kivy
 orientation = portrait
 fullscreen = 1
 android.presplash_color = #000000
 android.permissions = 

[buildozer]
 log_level = 2
 warn_on_root = 1

 android.api = 33
 android.minapi = 21
 android.ndk = 25b
 android.accept_sdk_license = True
 android.arch = arm64-v8a