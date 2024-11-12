AirBnB clone - The console
==========================

## Project Overview

Welcome to the AirBnB clone project! This project is the foundation of a larger project aiming to create a complete clone of the popular AirBnB platform. The primary focus here is to build a command interpreter that allows us to manage various AirBnB objects, laying the groundwork for future web applications. In this initial step, we focus on creating and managing data models that will be used across various components like HTML/CSS templates, databases, APIs, and front-end integrations.


## Features

This command interpreter enables us to:

* Create and manage essential AirBnB data models such as User, State, City, and Place.
* Implement a BaseModel class to handle instance initialization, serialization, and deserialization.
* Enable object persistence via a File Storage system, serializing instances to a JSON file and retrieving them as needed.
* Implement a comprehensive testing suite to ensure functionality and reliability of all classes and storage engines.


## Getting Started

### Prerequisites

To run this project, you need:

* Python 3.x installed on your machine
* Basic understanding of Python programming and command-line interfaces

### Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/AirBnB-clone.git
cd AirBnB-clone
```

2. Run the command interpreter:

```bash
./console.py
```

### Execution in interactive mode:

```shell
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

### Execution in non-interactive mode:

```shell
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

## Project Architecture

The AirBnB clone project relies on an organized hierarchy of classes, storage engines, and helper methods that interact to create a simple flow for object creation and persistence. Key components include:

- **BaseModel:** The parent class of all AirBnB-related classes, managing initialization, serialization, and deserialization.
- **Command Interpreter:** A command-line tool for creating, updating, deleting, and displaying AirBnB objects.
- **File Storage Engine:** A storage engine that saves object instances as JSON strings, allowing data persistence between sessions.
- **Unit Tests:** A set of tests validating functionality of classes, command interpreter commands, and storage mechanisms.

### Classes

#### BaseModel
The BaseModel class is the foundational class for all other data models in the project. It handles:

* Initialization and unique ID assignment
* Serialization (converting instances to JSON-compatible dictionaries)
* Deserialization (reloading instances from JSON strings)

#### Data Models
All models inherit from BaseModel, and currently include:

- **User:** Represents an individual user account.
- **State:** Represents a geographic area or region.
- **City:** Represents a city associated with a state.
- **Place:** Represents a rental listing, with fields for location, amenities, and pricing.

Each class contains attributes relevant to its purpose and is stored persistently within the file storage system.


## Command Interpreter Usage

The command interpreter, console.py, provides commands to create, manipulate, and delete objects in the system.

### Available Commands

- **create <class_name>:** Creates a new instance of <class_name> and saves it.
- **show <class_name> <id>:** Prints the string representation of a specific instance.
- **destroy <class_name> <id>:** Deletes a specific instance.
- **all [<class_name>]:** Prints all instances, optionally filtering by <class_name>.
- **update <class_name> <id> <attribute_name> <attribute_value>:** Updates an instance by setting <attribute_name> to <attribute_value>.


```shell
$ ./console.py
(hbnb) create User
(hbnb) show User 1234-5678-9101
(hbnb) all User
(hbnb) update User 1234-5678-9101 email "newemail@example.com"
(hbnb) destroy User 1234-5678-9101
(hbnb) quit
```

## File Storage System

This project implements a basic file storage engine that saves object data in a JSON file (file.json). The file storage engine:

1. Serializes objects as dictionaries, then converts them to JSON strings.
2. Stores all JSON data in file.json.
3. Deserializes data from file.json back into Python objects, enabling data persistence.

The file storage system abstracts the complexity of direct file manipulation, allowing object data to be created, read, updated, and deleted easily.

## Unit Testing

All classes, methods, and storage functions in this project are thoroughly tested using unittest, ensuring that:

* Object creation, serialization, and deserialization work correctly.
* The command interpreter can handle all defined commands.
* The file storage engine accurately saves and retrieves data.

#### To run the test suite, use the following command:

```bash
python3 -m unittest discover tests/
```


### Contributors

* Johnkennedy Umeh
