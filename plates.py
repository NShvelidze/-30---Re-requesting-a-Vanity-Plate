not_allowed = [" ","!","@","#","$","%",
               "^","&","*","(",")","-","_","=","+",
"[","]",";",":","'","\"",
 "<",",",".",">","/","?","\\","|"]

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s[0:2].isalpha() == False:
        return False
    if len(s) < 2 or len(s) > 6:
        return False

    i = 0
    count = 0
    while count < len(s):
        if s[i] == "0" and s[i_previous].isalpha():
            return False
        i += 1
        count += 1
        i_previous = i - 1

    for i in s:
        if i in not_allowed:
            return False
        if s[-1].isalpha() == True and i.isdigit() == True:
            return False

    else:
        return True

if __name__ == "__main__":
    main()
    
