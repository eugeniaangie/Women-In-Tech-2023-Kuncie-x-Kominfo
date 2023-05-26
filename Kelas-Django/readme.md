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
![image](https://github.com/eugeniaangie/Women-In-Tech-2023-Kuncie-x-Kominfo/assets/62442475/1a64aa08-0ee6-4ae3-bdc0-c00d3c5efcc4)

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

![image](https://github.com/eugeniaangie/Women-In-Tech-2023-Kuncie-x-Kominfo/assets/62442475/164822c7-18b0-4c0b-9fa4-2ac62f1da870)

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

![image](https://github.com/eugeniaangie/Women-In-Tech-2023-Kuncie-x-Kominfo/assets/62442475/231f3456-f0ec-4ec7-bb22-2fbdc1e0f08a)

```bash
py manage.py migrate
```
## DBeaver Installation
to manage your db install the [DBeaver](https://dbeaver.io/download/) (recomended) or you can use any other database tool.

DBeaver page

![image](https://github.com/eugeniaangie/Women-In-Tech-2023-Kuncie-x-Kominfo/assets/62442475/b970c5af-6e4e-439a-88a8-67663c2de478)


download based on your os (me:windows)

![image](https://github.com/eugeniaangie/Women-In-Tech-2023-Kuncie-x-Kominfo/assets/62442475/d1129f00-3c7b-4ac0-837f-9870cc2ab9cc)

after finish installation, choose SQLlite (we try with sqllite first)

![image](https://github.com/eugeniaangie/Women-In-Tech-2023-Kuncie-x-Kominfo/assets/62442475/27165059-88fc-44c9-9c3d-a26d8df641e8)

just download

![image](https://github.com/eugeniaangie/Women-In-Tech-2023-Kuncie-x-Kominfo/assets/62442475/4359ce28-5cdb-47e0-9e48-9d392cc20e17)

choose open and go to the 'db.sqlite3' in your django project

![image](https://github.com/eugeniaangie/Women-In-Tech-2023-Kuncie-x-Kominfo/assets/62442475/5c93ed73-c338-41e8-b36f-ce90b8c55622)

![image](https://github.com/eugeniaangie/Women-In-Tech-2023-Kuncie-x-Kominfo/assets/62442475/046e9904-654d-4d85-a90b-e96843d6868c)


you can see this then

![image](https://github.com/eugeniaangie/Women-In-Tech-2023-Kuncie-x-Kominfo/assets/62442475/2be45ac1-358b-4bdc-8464-418436a402fa)


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
ctrl c to exit from for loop

exit() to exit from django shell

to see the data that you just create
```bash
Pengguna.objects.all()
```
or
```bash
Pengguna.objects.all().values()
```
or see through DBeaver

![image](https://github.com/eugeniaangie/Women-In-Tech-2023-Kuncie-x-Kominfo/assets/62442475/f945c6bc-d90c-4f30-a924-f2846a576bc6)

![image](https://github.com/eugeniaangie/Women-In-Tech-2023-Kuncie-x-Kominfo/assets/62442475/6c4f2ab3-f19a-4b92-b317-ba13dc21f128)



#### Thank you! Happy Learning :))
