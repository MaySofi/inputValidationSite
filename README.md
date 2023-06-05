# inputValidationSite
Django project: prevention of xss attacks 

<br />
Run the project:

Create new folder
```bash
mkdir <folder_name>
cd <folder_name>
```
Activate Virtual Environment
```bash
python -m venv env
source env/bin/activate
```
Install Django
```bash
pip install django
```
Clone the project
```bash
git clone https://github.com/MaySofi/inputValidationSite.git
cd inputValidationSite
```

Almost there!
Run the project
```bash
python manage.py migrate 
python manage.py runserver 
```

Our site:
open browser
URL path: http://127.0.0.1:8000/

<br />
Without input validation

open browser
URL path: http://127.0.0.1:8000/app

