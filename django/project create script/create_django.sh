echo "making project for $1"
django-admin startproject $1
cd $1
mkdir apps
cd apps
touch __init__.py
