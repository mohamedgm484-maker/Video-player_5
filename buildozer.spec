[app]
title = Video Player
package.name = videoplayer
package.domain = org.myapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,android
orientation = portrait

android.permissions = READ_EXTERNAL_STORAGE,READ_MEDIA_VIDEO
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
