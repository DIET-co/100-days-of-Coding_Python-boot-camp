def explain_function_types():
    """
    Explains different types of functions in Python with syntax examples.
    """
    print("\n**Types of Functions in Python:**")

    print("- **Built-in Functions:**")
    print("    - Syntax: `function_name(arguments)`")
    print("    - Example: `len('hello')`") 

    print("- **User-defined Functions:**")
    print("    - **Without Arguments:**")
    print("        - Syntax: `def function_name():`")
    print("        - Example:")
    print("""
        def greet():
            print("Hello!")
        """)

    print("    - **With Arguments:**")
    print("        - Syntax: `def function_name(arg1, arg2, ...):`")
    print("        - Example:")
    print("""
        def greet_person(name):
            print("Hello, " + name + "!")
        """)

    print("    - **With Return Value:**")
    print("        - Syntax: `def function_name(arg1, arg2, ...):`")
    print("            - `return value`")
    print("        - Example:")
    print("""
        def add(x, y):
            return x + y
        """)

    print("    - **With Default Arguments:**")
    print("        - Syntax: `def function_name(arg1, arg2=default_value, ...):`")
    print("        - Example:")
    print("""
        def greet_with_default(name, greeting="Hello"):
            print(greeting + ", " + name + "!")
        """)

    print("    - **With Variable-length Arguments:**")
    print("        - **Arbitrary positional arguments:**")
    print("            - Syntax: `def function_name(*args):`")
    print("            - Example:")
    print("""
        def sum_all(*args):
            total = 0
            for num in args:
                total += num
            return total
        """)
    print("        - **Arbitrary keyword arguments:**")
    print("            - Syntax: `def function_name(**kwargs):`")
    print("            - Example:")
    print("""
        def print_kwargs(**kwargs):
            for key, value in kwargs.items():
                print(f"{key}: {value}")
        """)

def explain_control_flow():
    """
    Explains control flow statements in Python with syntax examples.
    """
    print("\n**Control Flow Statements:**")
    print("- **if-elif-else:**")
    print("    - Syntax:")
    print("""
        if condition1:
            # code to execute if condition1 is True
        elif condition2:
            # code to execute if condition1 is False and condition2 is True
        else:
            # code to execute if all previous conditions are False
        """)
    print("    - Example:")
    print("""
        num = 10
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")
        """)

    print("- **for loop:**")
    print("    - Syntax:")
    print("""
        for item in iterable:
            # code to execute for each item
        """)
    print("    - Example:")
    print("""
        for i in range(5):
            print(i) 
        """)

    print("- **while loop:**")
    print("    - Syntax:")
    print("""
        while condition:
            # code to execute as long as condition is True
        """)
    print("    - Example:")
    print("""
        count = 0
        while count < 5:
            print(count)
            count += 1
        """)

    print("- **and/or Operators:**")
    print("    - **and:** Returns True if both conditions are True.")
    print("    - **or:** Returns True if at least one condition is True.")
    print("    - Example:")
    print("""
        x = 10
        y = 5
        if x > 5 and y < 10:
            print("Both conditions are True")
        """)

def explain_string_array():
    """
    Explains how to operate on strings and arrays in Python with syntax examples.
    """
    print("\n**String Operations:**")
    print("- **Concatenation:**")
    print("    - Syntax: `string1 + string2`")
    print("    - Example: `'Hello' + ' ' + 'world!'`")

    print("- **Slicing:**")
    print("    - Syntax: `string[start:end]`")
    print("    - Example: `'Hello'[1:4]`") 

    print("- **Indexing:**")
    print("    - Syntax: `string[index]`")
    print("    - Example: `'Hello'[0]`") 

    print("- **Methods:**")
    print("    - `upper()`: Converts to uppercase.")
    print("    - `lower()`: Converts to lowercase.")
    print("    - `split()`: Splits the string into a list.")
    print("    - `join()`: Joins elements of an iterable with a separator.")
    print("    - `find()`: Finds the index of a substring.")
    print("    - Example:")
    print("""
        my_string = "Hello, world!"
        print(my_string.upper()) 
        print(my_string.split(',')) 
        """)

    print("\n**Array Operations:**")
    print("- **Creating Arrays:**")
    print("    - `list()` constructor:")
    print("        - Syntax: `my_list = list([element1, element2, ...])`")
    print("        - Example: `my_list = list([1, 2, 3])`")
    print("    - List comprehension:")
    print("        - Syntax: `my_list = [expression for item in iterable]`")
    print("        - Example: `my_list = [x * 2 for x in range(5)]`")

    print("- **Accessing Elements:**")
    print("    - Syntax: `my_list[index]`")
    print("    - Example: `my_list[0]`") 

    print("- **Modifying Elements:**")
    print("    - Syntax: `my_list[index] = new_value`")
    print("    - Example: `my_list[0] = 10`")

    print("- **Adding/Removing Elements:**")
    print("    - `append()`: Adds an element to the end.")
    print("    - `insert()`: Inserts an element at a specific index.")
    print("    - `remove()`: Removes the first occurrence of an element.")
    print("    - `pop()`: Removes and returns the element at a specific index (or the last element).")
    print("    - Example:")
    print("""
        my_list = [1, 2, 3]
        my_list.append(4)
        my_list.insert(1, 5)
        my_list.remove(2)
        print(my_list) 
        """)

# Example usage:
explain_function_types()
explain_control_flow()
explain_string_array()