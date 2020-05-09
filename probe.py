print ("hello?")
age = input('Сколько тебе лет: ')
#if bool(age.isdigit()):

if age.isdigit():
    print(age + " тебе лет")
    print(type(age))
    print("преобразую в int!!!")
    age_int = int(age)
    print(type(age_int))
else:
    print("Эт самое")
    age = input('введите  число: ')
print('Ура, товарищи!')
