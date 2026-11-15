
print("Enter marks obtained in 4 subjects: ")
math = int(input("maths:"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))


sum = math+english+science+hindi
print("sum of math,english,sience and hindi = ",sum)

prec = (sum/400)*100

print(end="percentage mark = ")
print(prec)