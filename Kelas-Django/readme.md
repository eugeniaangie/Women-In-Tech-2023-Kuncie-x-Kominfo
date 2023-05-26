## Django Installation
#### note: if you already have the virtual environment before, just execute the './env/Scripts/activate' without create the virtual env

Use [django](https://www.djangoproject.com/) documentation to install django.

(for windows os)

make sure that Python is installed on your system
```bash
py --version
```
or
```bash
python --version
```
create the virtual environment
```bash
py -m venv env
```
open the current directory in Visual Studio Code (VS Code)
```bash
code .
```
activate the virtual env
```bash
./env/Scripts/activate
```
make sure that already in the virtual env
(pict)

#### install django
```bash
py -m pip install Django
```
create django project, you can replace the 'project_pertama' with your desired name
```bash
django-admin startproject project_pertama
```
check if the project running successfully
```bash
py manage.py runserver 
```
run the 'http://127.0.0.1:8000/' in your browser

(pict)

create django app, you can replace the 'pengguna' with your desired name
```bash
py manage.py startapp pengguna
```
see the code in Kelas-Django and you can try to run the server


## Creating Django Models

follow the code on models.py
```bash
py manage.py makemigrations
```
then in the migrations folder will be created a migration file, the name must be '0001_initial.py'

(pict)
```bash
py manage.py migrate
```
## DBeaver Installation
to manage your db install the [DBeaver](https://dbeaver.io/download/) (recomended) or you can use any other database tool.

DBeaver page

(pict)

download based on your os (me:windows)

(pict)

after finish installation, choose SQLlite (we try with sqllite first)

(pict)

just download

(pict)

choose open and go to the 'db.sqlite3' in your django project

(pict)

you can see this then

(pict)

data is doesn't exist

## Insert Data to the Database
(Insert multiple data at once)

using django shell
```bash
py manage.py shell
```
```bash
from pengguna.models import Pengguna
```
```bash
p1 = Pengguna(
        nama='angie',
        alamat='taman palem, jakarta',
        email='eugeniaangelas@yopmail.com'
    )
```

see the p2 and p3 in 'create_database.py' file
```bash
list_pengguna = [p1, p2, p3]
```
```bash
for i in list_pengguna:
```
give 1 space before i.save()
```bash
 i.save()
```
to see the data that you just create
```bash
Pengguna.objects.all()
```
or
```bash
Pengguna.objects.all().values()
```
or see through DBeaver

(pict)


#### Thank you! Happy Learning :))