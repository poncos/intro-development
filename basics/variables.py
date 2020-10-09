
# Variable types
numeric_var = 5
string_var = "hello"
character_var = 'h'
numerical_array_var = [3, 4, 5, 6, 6]
string_array_var = ["hello", "how", "are", "you?"]
char_array_var = ['h', 'e', 'l', 'l', 'o']

numerical_sum = numeric_var + 5
string_sum = string_var + " bye"

print("numerical sum: ", numerical_sum)
print("string_sum:", string_sum)

# ================== Variable scope ==================
string_var = 15

print("string_var: ", string_var)


def my_function():
    # this variable belongs to the function scope
    string_var = 20
    print("internal string_var: ", string_var)


def another_function():
    # Here we are using the variable value defined in a wider sope
    print("another function string_var: ", string_var)

my_function()
another_function()
print("string_var: ", string_var)
# ==================  ==================

# ================== Type transformation ==================
numerical_sum = 5 + int("10")

print("numerical_sum with type transformation: ", numerical_sum)

string_sum = str(5) + "10"
print("string_sum with typee transformation: ", string_sum)


# ================== Arrays =================

