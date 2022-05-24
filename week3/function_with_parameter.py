print('inside python file before function')

#defile a function with a name and parameter greeting

def hello_function(greeting):
    print(f'{greeting} to everyone')

    #calling the function or invoke
    #typeerror: hello_function() missing 1 required positional argument: greeting
    #hello_function()


    #greeting = "hello" behind the scene
    hello_function('hello') # 'hello is an argument to hello_function
    hello_function2('markson','hello') #two argument
    hello_function2('hello','markson') #pay attention to the order
    #hello_function