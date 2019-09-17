# Advanced Calculator

Now that you've mastered the first calculator project, it's time to add some more advanced functionality to it!  

While the functions from the last calculator project required you pass 1-2 arguments (example:  add(x, y)), we will now be giving our mathematical functions the ability to pass unlimited arguments!  This will be done by passing _*args_ as a parameter of the respective functions.  

Example:  
```
def multiply_all_args_by_2(*args):
    for arg in args:
        print("{} is one of the *args!".format(arg))

multiply_all_args_by_2(5, 4, 3, 2, 1)

#Output:
5 is one of the *args!
4 is one of the *args!
3 is one of the *args!
2 is one of the *args!
1 is one of the *args!
```

With the power of _*args_, read the tests.py file and give functionality to the mathematical functions found in adv_calculator.py in order to get all the tests passing!

In order to run the tests, go into the subsection of the repository directory with tests.py and run 'python3 -m pytest tests.py'.  

As with many aspects of programming, there are multiple ways you can approach and implement these functions. 

**Note:**  To calculate variance you will need to reflect this pseudo code: 
Apply _(arg - mean) ** 2_ to each argument in _*args_ and add up their total.  Once you have that total, divide it by the length of the args!

**Note2:**  std will require the use of a square root function!
