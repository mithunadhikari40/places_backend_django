# places_backend_django

Steps used to create this app:
1. Run pip install django in a folder of your choice
2. Run django-admin startproject [app_name]
3. go inside that folder or app name you just created
4. poetry init, fill in all the details
5. mkvirtualenv [app_name] -- this step could be done at the begining
6. rename the [app_name]/[app_name] to [app_name]/config
7. search  for the occurance and replace those with config
8. create a apps/utils/timestamp directory
9. to put the resuable timestamp code in apps/utils/timestamp run python manage.py startapp timestamp apps/utils/timestamp
10. Make modification to apps/utils/timestamp/apps.py and put the relative path
11. Update the settings.py of config module to include the newly created app.
12. Now, in any model you want to use timestamp, extend TimeStamp class e.g class UserModel(TimeStamp)
