# Course Module Tracker – Python OOP Example

## Overview

This project is a simple Python script that demonstrates the use of **Object-Oriented Programming (OOP)** concepts to model a course learning module. The program represents a learning module that contains a title, learning content, and a completion status.

The goal of this script is to show how **encapsulation, class methods, and data validation** can be used in Python to manage course progress within a learning system.

This example can serve as a basic building block for larger systems such as:

* Learning Management Systems (LMS)
* Online course platforms
* Student progress trackers
* Educational automation tools

---

## Features

The script includes the following functionality:

* Encapsulation using **private class attributes**
* Methods to **retrieve module information**
* Ability to **update module completion status**
* Methods to **mark modules as completed or incomplete**
* Input validation to ensure correct progress updates

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

---

## Project Structure

```
course_module.py
README.md
```

---

## Class Description

### `CourseModule`

The `CourseModule` class represents a single learning module in a course.

#### Attributes

| Attribute             | Description                                  |
| --------------------- | -------------------------------------------- |
| `__title`             | Stores the title of the course module        |
| `__content`           | Stores the learning content of the module    |
| `__completion_status` | Tracks whether the module has been completed |

The attributes are **private** to enforce encapsulation.

---

## Methods

### `get_title()`

Returns the title of the module.

### `get_content()`

Returns the content of the module.

### `get_completion_status()`

Returns the completion status of the module.

### `get_update_progress(completed)`

Updates the completion status of the module. The method checks if the value passed is a Boolean.

### `mark_completed()`

Marks the module as completed.

### `mark_incompleted()`

Marks the module as incomplete.

---

## Example Usage

```python
module = CourseModule(
    "Introduction to Machine Learning",
    "Learn about AI and how to write automation"
)

print(module.get_title())
print(module.get_completion_status())

module.get_update_progress(True)

print(module.get_completion_status())
```

---

## Expected Output

```
Introduction to Machine Learning
False
True
```

---

## Concepts Demonstrated

This project demonstrates several Python OOP concepts:

### Encapsulation

Private attributes are used to protect the internal state of the object.

### Data Validation

The script ensures that completion status can only be updated using Boolean values.

### Class-Based Design

The module is represented as an object with properties and behaviors.

---

## Possible Improvements

This simple script can be expanded in several ways:

* Add a **Student class** to track student progress
* Create a **Course class** containing multiple modules
* Implement **progress percentages**
* Store modules in **lists or dictionaries**
* Connect the system to a **database**
* Build a **web interface using Flask or Django**

---

## Author

Collins Akoja Nathaniels
Python Programmer | Data Enthusiast | Educational Technology Builder

---

## License
MIT License
This project is open-source and can be used for educational purposes.
