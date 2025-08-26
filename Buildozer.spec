[app]

# Application basic info
title = BCC Control Software
package.name = bcccontrol
package.domain = org.ceet.drm

# Source configuration
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,jpeg,db
source.include_patterns = Pages/*,*.db,CEET.png

# Version info
version = 1.0
version.regex = __version__ = ['"](.+)['"]
version.filename = %(source.dir)s/main.py

# Dependencies
requirements = python3,kivy==2.1.0,kivymd==1.1.1,pillow,sqlite3

# Icon and presplash
icon.filename = %(source.dir)s/CEET.png
presplash.filename = %(source.dir)s/CEET.png

# Orientation
orientation = portrait

# Services
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# OSX Specific
#
# author = © Copyright Info

# Android specific
#

[buildozer]

# Buildozer log level (int): 1 = error, 2 = info, 3 = debug
log_level = 2

# Path to build artifact storage, for debug builds
# (default: ./bin)
# bin_dir = bin

[android]

# Android API to use
api = 34

# Minimum API your APK / AAB will support.
minapi = 21

# Android NDK version to use
ndk = 25b

# Android SDK version to use
sdk = 34

# Target Android API, should be API-1 lower than api for Google Play compatibility.
# android.api = 33

# Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# Android app theme, default is ok for Kivy-based app
# android.theme = @android:style/Theme.NoTitleBar

# List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# Android AAB application bundle format, default is False
android.release_artifact = apk

# Dependencies that the app might need
# android.gradle_dependencies =

# Java language level, default is 1.7, can be 1.6, 1.7, 1.8 or higher
android.gradle_java_version = "1.8"

# Android logcat filters to use
#android.logcat_filters = *:S python:D

# Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# Android architecture to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# You can set many archs, to build multiple APKs.
android.archs = arm64-v8a, armeabi-v7a

# Allow backup of app data via adb backup
android.allow_backup = True

# Permissions that the app needs
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Form factor (choices: phone, tablet, tv, wear)
android.form_factor = phone

# Adaptive launcher icon
#android.adaptive_icon = true

# Location of adaptive launcher icon background and foreground images
#android.adaptive_icon.background = adaptive-icon/background.png
#android.adaptive_icon.foreground = adaptive-icon/foreground.png

# Name of the certificate file to use for signing the app
#android.certificate = your_certificate.p12

# Password for the certificate file
#android.certificate.password = your_password

# Application name in the launcher
android.name = BCC Control

# Whitelist file patterns for the packager
#android.whitelist =

# (str) Android app category. (default: '')
# Choices are: None, launcher, browser, communication, contacts, entertainment,
# finance, health, maps, media, medical, news, photography, productivity,
# shopping, social, sports, tools, transportation, travel, weather
android.category = tools

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (bool) enables Android backup rules (Android API >=31)
android.backup_rules = False

# (str) XML file for backup rules (Android API >=31)
#android.backup_rules_file =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This property takes a map of key-value pairs. (via a string)
# Usage example : android.manifest_placeholders = key:value, key2:value2
#android.manifest_placeholders =

# (bool) Skip byte compile for .py files
#android.skip_byte_compile =

# (str) Python interpreter for the Android app, python2 or python3, default is python3
android.python = python3

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android app package, useful if you need to set a different package name
# than the one set in title
#android.app_package = org.ceet.drm.bcccontrol

# (str) Android app icon description (for accessibility)
android.icon_description = "BCC Control Software Logo"

# (str) Android app icon background color
# Formats are #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuschia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.icon_background_color = #FFFFFF

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars =

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAB application bundle format, default is False
# android.bundle_format = aab

# (str) The format used to package the app for release mode (aab or apk or aar).
android.release_artifact = apk

# (str) The format used to package the app for debug mode (apk or aar).
android.debug_artifact = apk

# iOS specific
#

[ios]

# (str) Path to a custom entitlements file
#ios.entitlements =

# (list) Custom frameworks dependency
#ios.frameworks =

# Darwin/macOS specific
#

[osx]

# change the major version of python used by the app
python_version = 3

# Kivy version to use
kivy_version = 2.1.0

# Author of this package
# osx.python_version = 3

# App author & category
# osx.info.name = %(title)s
# osx.info.version = %(version)s
# osx.info.author = © Copyright 2024, CEET-DRM
# osx.info.copyright = Copyright (c) 2024 CEET-DRM
# osx.info.category = public.app-category.utilities
