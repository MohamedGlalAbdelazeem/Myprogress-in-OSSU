"""
Making Face
"""
# make function called convert 
def convert(str):
    str = str.replace(":)" , "😀")
    str = str.replace(":(" , "😥")
    return str

# make a func called main 
def main():
    userInpu = input("Please Enter your text:")
    convertText = convert(userInpu)
    print (convertText)

main()
