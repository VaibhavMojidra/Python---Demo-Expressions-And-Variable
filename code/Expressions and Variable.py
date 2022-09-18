print("Hello World") #Prints Hello World
print(type("Vaibhav Mojidra")) #Prints data type of "Vaibhav Mojidra"
print(type(12)) #Prints data type of 12
print(type(12.54)) #Prints data type of 12.54


##In Python, text in between quotes -- either single or double quotes -- is a
##string data type. An integer is a whole number, without a fraction, while a float is
##a real number that can contain a fractional part. For example, 1, 7, 342 are all
##integers, while 5.3, 3.14159 and 6.0 are all floats. When attempting to mix incompatible
##data types, you may encounter a TypeError. You can always check the data type of
##something using the type() function.



#Variables

#Variables are use to store values

##First, you shouldn't use as variable names any of the key words or functions
##that Python reserves for its own, like print. Using these reserved terms will make
##your program confusing to read and will result in errors. Python also has some
##restrictions on the characters you can use to define a variable. Variable names can't have
##any spaces and they must start with either a letter or an underscore. Also, they
##can only be made up of letters, numbers and underscores.


length=2 #int variable
breath=5.2 #float variable
area=breath*length #Implicit Conversion as both are numbers
areaText="Area is "

##Some data types can be mixed and matched due to implicit conversion. Implicit
##conversion is where the interpreter helps us out and automatically converts one data type
##into another, without having to explicitly tell it to do so.
##By contrast, explicit conversion is where we manually convert from one data
##type to another by calling the relevant function for the data type we want to
##convert to. We used this in our video example when we wanted to print a number
##alongside some text. Before we could do that, we needed to call the str() function to
##convert the number into a string. Once the number was explicitly converted to a
##string, we could join it with the rest of our textual string and print the result.


#print(areaText+area) #TypeError: can only concatenate str (not "float") to str

print(areaText+str(area)) #Explicit Conversion - converting float to String data type
