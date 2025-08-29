[app]
title = BCC
package.name = bcccontrol
package.domain = org.example
source.dir = .

source.include_exts = py,png,jpg,kv,atlas,txt,jpeg,db
source.include_patterns = Pages/*,*.db,CEET.png

version = 1.0
requirements = python3,kivy,kivymd,pillow
icon.filename = %(source.dir)s/CEET.png

[buildozer]
log_level = 2

[android]
api = 34
minapi = 21
ndk = 25b
sdk = 34
android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
orientation = all
android.orientation = all
