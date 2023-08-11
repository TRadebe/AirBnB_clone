# AirBnB Clone Project README

## Background Context

Welcome to the AirBnB clone project! Before you dive in, make sure to read the AirBnB concept page to understand the project's context.

## Project Overview

This project marks the beginning of creating a full web application – the AirBnB clone. It's a crucial step as the foundation you build here will be used in subsequent projects, including HTML/CSS templating, database storage, API, and front-end integration.

In this step, you will:

- Develop a parent class called `BaseModel` responsible for instance initialization, serialization, and deserialization.
- Establish a simple serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> file.
- Create classes for AirBnB objects (User, State, City, Place, etc.) that inherit from `BaseModel`.
- Implement the first abstracted storage engine for the project: File storage.
- Write comprehensive unit tests to validate your classes and storage engine.

## Command Interpreter

Think of the command interpreter as a specialized shell for your project. It allows you to:

- Create new objects (e.g., User, Place)
- Retrieve objects from files or databases
- Perform operations on objects (count, compute stats, etc.)
- Update object attributes
- Delete objects

## Resources

Make sure to familiarize yourself with the following resources:

- [cmd module](https://docs.python.org/3/library/cmd.html)
- [cmd module in depth](https://pymotw.com/3/cmd/)
- [Python packages concept page](https://realpython.com/python-modules-packages/)
- [uuid module](https://docs.python.org/3/library/uuid.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [args/kwargs](https://realpython.com/python-kwargs-and-args/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
- [cmd module wiki page](https://en.wikipedia.org/wiki/Cmd.exe)
- [python unittest](https://docs.python.org/3/library/unittest.html)

## Learning Objectives

By the end of this project, you should be able to explain:

**General:**

- Creating a Python package
- Building a command interpreter in Python using the cmd module
- Implementing Unit testing in a large project
- Serializing and deserializing a Class
- Reading and writing JSON files
- Managing datetime in Python
- Understanding UUIDs (Universally Unique Identifiers)
- Using *args and **kwargs in function definitions
- Handling named arguments in functions

**Copyright - Plagiarism:**

- Coming up with your solutions to meet project tasks and learning objectives
- Avoiding plagiarism and not copying others' work
- Not publishing any content from this project

## Requirements

**Python Scripts:**

- Use editors like vi, vim, emacs
- Compatibility: Ubuntu 20.04 LTS, Python 3.8.5
- Files should end with a new line
- First line of files should be `#!/usr/bin/python3`
- Mandatory README.md file at the root
- Code should adhere to pycodestyle (version 2.8.*)
- All files must be executable
- Document all modules, classes, and functions
- Modules should have comprehensive documentation explaining their purpose

**Python Unit Tests:**

- Test files should end with a new line
- Tests should be within a 'tests' folder
- Use the unittest module for testing
- Test files and folders should start with 'test_'
- Organize test files to mirror your project's structure
- Execute tests using `python3 -m unittest discover tests`

**GitHub:**

- Each group should have a unique project repository
- Cloning, forking, or using a repository with the same name before the second deadline results in a 0% score

## Execution

Your shell should function like this:

Interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

Non-interactive mode (similar to the Shell project in C):
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should pass in non-interactive mode:
```bash
$ echo "python3 -m unittest discover tests" | bash
```

Remember, working together on test cases can help catch all edge cases.
