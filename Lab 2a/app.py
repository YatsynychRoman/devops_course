#Перше завдання
print("First constant", True)
print("Second constant", NotImplemented)
print("Third constant", None)

#Друге завдання
arr = [1, 2, 3, 4, 5]

def filterFunction(obj):
    if obj >= 3:
        return True
    else:
        return False

filtered = list(filter(filterFunction, arr))

print(filtered)

#Третє завдання
for obj in arr:
    print(obj)

print(arr[0] if arr[0] != arr[1] else arr[1])

#Четверте завдання
arr1 = [1, 2, 3]
try:
    print(arr1[3])
except Exception as err:
    print(err)
finally:
    print("Error found")
    
#П'яте завдання
with open("text.txt", "w") as file:
    file.write("sample text")

#Шосте завдання
func = lambda a, b, c : a + b * c
print(func(1, 2, 3))

#lamda застосовується для створення анонімних функцій, аналог function expression з мови JavaScript
