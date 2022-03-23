### Decorators Factory

Create a decorators factory (decorator itself).
The factory accepts a function (`lambda`) as an input and returns a decorator
that will return the result of the function as the first argument,
the result of the decorated function is passed. 
The function which the factory accepts (in the example below it is a `lambda`) can take one positional parameter only.

For example:
```python
@apply(lambda user_id: user_id + 1)
def return_user_id():
    return 42

>>> return_user_id()
43
```
