#Lab 2

##Хід роботи
1. Встановив *pipenv* та створив ізольоване середовище для *Python*:
```bash
pip install pipenv
pipenv --python 3.8
pipenv shell
```
2. Встановив бібліотеки *requests, ntplib*:
```bash
pipenv install requests
pipenv install ntplib
```
3. Створив файл *app.py*, скопіював у нього код програми з репозиторію, програма працює правильно.
4. Встановив бібліотеку *pytest* та запустив тести, всі тести виконались успішно:
```bash
pipenv install pytest
pytest tests/tests.py
```
5. Дописав у програмі функцію, що перевіряє час доби на AM/PM та відповідно друкувати "Доброго дня/ночі". Також написав тест який перевіряє правильність роботи функції.
6. Перенаправив результат виконання функції та тестів у файл *results.txt*:
```bash
pipenv run pytest tests/tests.py >> results.txt
pipenv run python app.py append >> results.txt
```

