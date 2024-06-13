name = input ('enter your user name plise : ' )
age = input ("enter your age : ")
email = input ("enter your email : ")
password = input ('enter pasword online : ')
if password == '55' :
    print ("hello " , name )
    print ("Welcome to my barktor and you are one of the elites ")
    opinte = name + "_data.txt"
    open (opinte , 'w')
    with open (opinte , 'w' , encoding='utf-8') as files :
        files.write(name)
        files.write(" ")
        files.write(age)
        files.write(" ")
        files.write(email)
        
else :
    print ("sorry " , name )
    print ("your password is incorrect You can't get in")