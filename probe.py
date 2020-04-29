print ("hello?")

name = input('введите  число: ')
print(name.isnumeric())
if str(name.isnumeric()) == "False":
   print("Эт самое")
   name = input('введите  число: ')
else:
 print(name + " так тебя зовут")

 print(type(name))
 print("преобразую в int!!!")
 name_int = int(name)
 print(type(name_int))

