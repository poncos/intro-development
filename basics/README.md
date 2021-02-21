# Introduction to Programming

## Types, Objects, Variables, Operators and Sentences

Every programming language has the concept of *types* of data, like numerical or scalar types, alphanumeric or strings type.

In Python we will talk of **object** and types instead of data and types. Basically things like numbers and strings are objects in Python
and each object has a type which is important because it will tell us the kind of operations we can do with that object.

The different basic types available in Python are:

- Integer
- Float
- Bool
- String 

### Expression

A expression is defined as any unit or entity of code that can be evaluated to determine the expression value (which in the casee
of Python is an object). It is a combination of objects and operators.

Operators 

A basic classification is to devide the types of expressions in two categories: 1) Assignment, those expressions that assign
a value to a variable, and 2) those expressions that simply has a value. In the following examples, the first two expressions
belong to the second category, and the third one to the first category. 

- 5 + 3. This expression is a Integer expression because its value is a *intiger*.
- 5.0 + 3.0. This is a *float* expression.
- x = 5 + 3. This is a integer expression where the value is assigned to the variable *x*.

There are as well, **boolean expression** that evaluate to a *bool* value, and **string expressions**.

Operators behaviour depends on the types they are applied to, for example for the expression *5 + 3* the operator *+* is
the usual sum witch is evaluated to 8, but for other data types could behave different or even fail because the operator 
might not be defined for the data types being used.

![](../static/screenshots/operators.png)

The previous image is an example (making use of the Python command line interpreter) of how operators behave different
for different data types. The second expression in the image shows the operator '+' used with two string arguments, and the
outcome is the two strings concatenated. The last expression results in a error, because the operator '+' does not
work with one argument being a *string* and another one being an *integer*.


### Variables

A variable is like a label, a label pointing to a value or a object using Python terminology.

```python
pi = 3.14
radius = 20
area = pi * (radius**2)

print(area)
```

In the example above, we have assigned the value 39 to the variable called *area*, and then we have made use of that
variable using the Python function *print* to show the value of that variable in the screen.

The action of assign a variable to an object is called **binding**, we are binding the variable or the name or
the label *pi* to the object *3.14*, which in reality will be placed in a memory position in the computer. Basically
the variables contain the **memory address** of the object, that is the memory position where the object is located.

The reasons to use variables is clear but let's mention them.

- **Code re-use**. In the example above, the expression 'pi * (radius**2)' is executed once and the result is stored in 
the variable *area*, therefore later in the code we can use it as many times as we need without having to execute the same
expression again. For example in the *print* operation, we just use the value pre-calculated available in the variable value.

- **Self-documented code**.


## Branching programming


## Iterations


## Basic data structures


### Arrays

### Multi-dimensional Arrays


### Dictionaries


### Functions  
