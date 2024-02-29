# def main():
#    number = get_number()
#    meow(number)

# def get_number():
#     while True:
#         n = int(input("what's n ?"))
#         if n > 0:
#             break
#     return n

# def meow(n):
#     for _ in range(n):
#         print("idk")    
# main()
# def convert_to_string(lst):
#     if lst == 0:
#         return "[]"
#     else:
#         new_str = "["
#         for i in lst:
#             new_str += str(i)  # Convert i to a string before concatenating
#         new_str += "]"  # Append "]" after the loop
#         return new_str  # Return new_str outside the loop
# print(type(convert_to_string([1, 2, 3])))

    

# students = ["ali","mohamed","glal","sayed"]
# for i in students:
#     print(i)



# students = ["ali","mohamed","glal","sayed"]
# for i in range(len(students)):
#     print( i,"-",students[i])

# for i in [0 ,1,2,3]:
#     print("idk")

# dictionaries ===> dics: are a data structure that allows you to associate on value to another 
# students = {
#     "name":"ali",
#      "Jop":"ahmed",
#      "age":22,
#      "id" :50654
# }
# for i in students:
#     print(i,":",students[i])

# def print_square(size):
#     for i in  range(size):
#             print("#" * size , end="")
             
# print_square(3)


# print("meow")
# print("meow")
# print("meow")

# first while loop
# list => [1,2,3] for i in  list 

# for i in [0, 1, 2]:
#     print("meow")

# for _ in range(3):
#     print("idk")

# print("idk" * 3 , end="")

# while True:
#     n = int(input("what is n?"))
#     if n < 0:
#         break
#     else:
#         continue
# for _ in range(n):
#     print("idk")

# def main():
#     meow(get_number())


# def get_number():
#     while True:
#         n = int(input("What's n? "))
#         if n > 1:
#             return n


# def meow(n):
#     for _ in range(n):
#         print("meow")


# main()



# my_list = ["ali" ,"mohamed" ,"glal"]

# for i in range(len(my_list)):
#     print(my_list[i]) 

# students = ["Hermoine", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])


# students = {
#     "Hermoine": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# for i in students:
#    print(i ,":", students[i]) 


students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
