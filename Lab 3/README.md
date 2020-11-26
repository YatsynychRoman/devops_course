# Lab 3
## Хід роботи

1. За допомогою *Django Framework* створив заготовку проекту.
```
pipenv run django-admin startproject test_site
    
        mv test_site/test_site/* test_site/
        mv test_site/manage.py ./

```

2. Запустив сервер та переконався шо він працює

```
November 26, 2020 - 09:18:06
Django version 3.1.3, using settings 'my_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```
3. Створив темплейт додатку

```
pipenv run python manage.py startapp main
```

4. Створив `main.html` та `urls.py`
