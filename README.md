# LAB 1

## Хід роботи
1. Для клонування репозиторію була використана команда "git clone".
2. Хеш попереднього коміту: 8be317ca56751e354f1c1a3c1b533b724cf065c4. 
Для комміту було використано комманди: 
* "git add ."
* "git commit -m"
* "git push" 
3. Для створення та перелючення на нову гілку була використана команда "git checkout" з опцією "-b" 
4. Зміни не з'явились у гілці master через те, що коміт був зроблений у гілці "new_branch" яка не впливає на гілку  master 
```mermaid
graph LR
master --> 1
1((1 commit master)) --> branch
branch --> 2((2 commit branch))
1((1 commit master)) --> 3((3 commit master))