### Functional programming hash
***
Create a function `hash_names` what takes a list of strings and returns a list of their (strings) hashes.
The function has to be implemented in functional style instead of imperative one -
it is not allowed to use `for`, `while` loops etc.
The following example shows the logic in the imperative style with `for` loop
```python
names = ['Alexey', 'Ivan', 'Petr']
for i in range(len(names)):
    names[i] = hash(names[i])

print(names)
```
Do not forget about function documentation!