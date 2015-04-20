Assuming you have all the dependencies

rm -f db.sqlite3

python2 manage.py migrate
python2 manage.py createsuperuser
python2 manage.py runserver
