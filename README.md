# HashMap Implementations

This repository contains implementations of a basic HashMap in both C and Python. These implementations provide basic functionalities like initializing the map, adding entries, and retrieving values.

## C Implementation

The C version of the HashMap uses a simple hash function based on the modulo operation and linked lists to handle collisions. The implementation includes functions to initialize the map, add key-value pairs, retrieve values, and free the allocated memory.

### Files

- `hashmap_structs.h`: Header file defining the `ListNode` and `HashMap` structures.
- `hashmap.c`: Implementation file with all the functions required to manipulate the hashmap.

### Functions

- `void initHashMap(HashMap *map, int size)`: Initializes the hashmap with the given size.
- `void put(HashMap *map, int key, int value)`: Adds a key-value pair to the hashmap.
- `int *get(HashMap *map, int key)`: Retrieves the value associated with the given key.
- `void freeHashMap(HashMap *map)`: Frees all allocated memory used by the hashmap.

## Python Implementation

The Python version uses a list of lists to handle collisions and provides a simpler and more Pythonic API. It uses Python's built-in `hash` function for hashing.

### File

- `hashmap.py`: Contains the Python class `HashMap` with methods to manipulate the hashmap.

### Methods

- `__init__(self, size)`: Constructor to initialize the hashmap with the specified size.
- `insert(self, key, value)`: Inserts a key-value pair into the hashmap.
- `__getitem__(self, key)`: Returns the value associated with the key using bracket notation.

## Usage

### C

Compile the C code using a C compiler, e.g., `gcc`:

```bash
gcc -o hashmap hashmap.c
```

Run the executable:

```bash

./hashmap

```

### Python

Run the Python script directly if you have Python installed:

```bash

python hashmap.py

```

Contributions

Contributions to this project are welcome. Please feel free to fork the repository, make improvements, and open a pull request.

Feel free to modify this README according to the specifics of your project structure and personal preferences.
