info = ""
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
# inner_function() #  - эту функцию тут вызвать нельзя, т.к. она является локальной, для функции test_function
