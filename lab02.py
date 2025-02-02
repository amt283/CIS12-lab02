import math

def main():
    print("Part 1: Variables and Assignments\n")

    # 1.1 - Create variables
    name = "Your Name"
    age = 20
    height = 5
    favorite_color = "Blue"

    # 1.2 - Printing Techniques for variable values:
    print("1.2.1 - Print one variable at a time: \n")
    print(name)
    print(age)
    print(height)
    print(favorite_color)

    print("\n1.2.2 - Print with one print statement and commas: \n")
    print(name, age, height, favorite_color, sep=", ")

    print("\n1.2.3 - Print with Python formats or format specifiers: \n")
    print(f" Hello, my name is {name}, I am {age} years old, I am {height}"
          f" feet tall and my favorite color is {favorite_color}")

    print("\n1.2.4 - Print with format specifiers within a multi-line string: \n")
    print(f""" 
    Name: {name} 
    Age: {age}
    Height: {height}"
    Favorite Color: {favorite_color}
    """)

    # 1.3 - Create a new variable
    radius = 5
    circle_area = math.pi * (radius ** 2)

    print(f"\n1.3 - The area of a circle with a radius of {radius} is {circle_area:.1f}")

    print("\nPart 2: Statements and Modules\n")

    # 2.2 - Calculate the square root
    age_sqrt = math.sqrt(age)

    print(f"2.2 - The square root of my age ({age}) is {age_sqrt:.1f}")

    # 2.3 - Calculate the sine and cosine
    height_sin = math.sin(height)
    height_cos = math.cos(height)

    print(f"""\n2.3 - The sine of my height ({height}) is {height_sin:.1f}.
        The cosine is {height_cos:.1f}.
    """)

    print("\nPart 3: Expressions and Operators\n")

    # 3.1 - Arithmetic operations
    age_sum = age + 5
    height_diff = height - 4
    age_prod = age * height
    height_quot = height / 2
    age_remainder = age % 3
    age_pow = age ** 2

    print(f"""
    3.2 - 
    Age Sum: {age_sum:.1f}
    Height Difference: {height_diff:.1f}
    Age-Height Product: {age_prod:.1f}
    Height Quotient: {height_quot:.1f}
    Age Remainder: {age_remainder:.1f}
    Age Power: {age_pow:.1f}
        """)

    print("\nPart 4: Temperature Conversion\n")

    # 4.1 - Create a temperature conversion program
    # How to print degree sign found here:
    # https://stackoverflow.com/questions/3215168/how-to-get-character-in-a-string-in-python
    farenheit = float(input("4.1 - Enter a temperature (in Farenheit): "))
    celcius = (farenheit - 32) * (5/9)
    degree_sign = u'\N{DEGREE SIGN}'

    print(f"Conversion: {farenheit}{degree_sign}F is {celcius:.1f}{degree_sign}C")

main()