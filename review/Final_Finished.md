# 🐍 Python Review Sheet

Use this guide to refresh your memory before the final exam.

---

## 1. Variables & Data Types

```python
# Integer
age = 17

# Float (decimal)
gpa = 3.85

# String (text)
name = "Alice"

# Boolean (True or False)
is_student = True
```

**Key rule:** Use `type()` to check what type a variable is.
```python
print(type(age))    # <class 'int'>
print(type(name))   # <class 'str'>
```

---

## 2. Operators

| Operator | Meaning        | Example       |
|----------|----------------|---------------|
| `+`      | Addition       | `3 + 2 = 5`   |
| `-`      | Subtraction    | `5 - 2 = 3`   |
| `*`      | Multiplication | `4 * 3 = 12`  |
| `/`      | Division       | `10 / 2 = 5.0`|
| `//`     | Floor Division | `10 // 3 = 3` |
| `%`      | Modulo (remainder) | `10 % 3 = 1` |
| `**`     | Exponent       | `2 ** 3 = 8`  |
| `==`     | Equal to       | `5 == 5` → True |
| `!=`     | Not equal      | `5 != 3` → True |

---

## 3. Conditionals

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")   # This runs
elif score >= 70:
    print("C")
else:
    print("F")
```

---

## 4. Loops

### `for` loop — use when you know how many times to repeat
```python
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### `while` loop — use when you repeat until a condition is False
```python
count = 0
while count < 3:
    print("Count:", count)
    count += 1
```

---

## 5. Functions

```python
def greet(name):           # Define the function
    return "Hello, " + name

message = greet("Alice")   
print(message)             
```

- `def` → defines a function
- Parameters go in the parentheses
- `return` sends a value back to the caller

---

## 6. Lists

```python
colors = ["red", "green", "blue"]

print(colors[0])       
print(colors[-1])     
colors.append("yellow")  # Add to end
colors.remove("red")     # Remove item
print(len(colors))       # Length: 3
```

---

## 7. Dictionaries

A dictionary stores **key-value pairs** (like a real dictionary: word → definition).

```python
student = {
    "name": "Alice",
    "grade": 11,
    "gpa": 3.9
}

print(student["name"])    # Alice
student["gpa"] = 4.0      # Update a value
student["school"] = "EHS" # Add a new key
```

---

## 8. String Methods

```python
text = "Hello, World!"

print(text.upper())        # HELLO, WORLD!
print(text.lower())        # hello, world!
print(text.replace("Hello", "Hi"))  # Hi, World!
print(text.split(", "))    # ['Hello', 'World!']
print(len(text))           # 13
print("World" in text)     # True
```

---

## 9. File I/O (Reading and Writing Files)

```python
# Writing to a file
with open("notes.txt", "w") as f:
    f.write("My secret notes\n")
    f.write("Line 2\n")

# Reading from a file
with open("notes.txt", "r") as f:
    contents = f.read()
    print(contents)

# Appending to a file (add without erasing)
with open("notes.txt", "a") as f:
    f.write("Added this line later\n")
```

**File modes:**
- `"r"` — Read (file must exist)
- `"w"` — Write (creates or overwrites)
- `"a"` — Append (adds to the end)

---

## 10. Quick Cheat Sheet

| Concept        | Keyword/Syntax       |
|----------------|----------------------|
| Print output   | `print()`            |
| Get input      | `input()`            |
| Define function| `def name():`        |
| Return value   | `return value`       |
| List           | `[item1, item2]`     |
| Dictionary     | `{"key": "value"}`   |
| For loop       | `for x in list:`     |
| While loop     | `while condition:`   |
| Open file      | `open("file", mode)` |
| Import module  | `import module_name` |
