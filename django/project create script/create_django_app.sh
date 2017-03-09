echo "name of the app $1"
python ../manage.py startapp $1
cd $1
mkdir -p "templates/$1/"
touch "templates/$1/index.html"
mkdir -p "static/$1/css"
touch "static/$1/css/styles.css"
mkdir -p "static/$1/js"
touch "static/$1/js/main.js"
mkdir -p "static/$1/images"
touch urls.py
cd ../../
python manage.py runserver
