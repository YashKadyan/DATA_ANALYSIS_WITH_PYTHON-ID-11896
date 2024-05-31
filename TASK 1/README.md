## TITLE: 
Main Flow Services and Technologies Internship - Task Documentation: “Python Basics” Using Python (Jupyter Notebook).


## INTERN INFORMATION:

**Name:** Yash Sanjay Kadyan

**ID:** ID-11896


# INTRODUCTION

In the realm of programming, data structures are fundamental tools that enable efficient data management and manipulation. Understanding and utilizing these structures effectively is crucial for solving complex problems and optimizing code performance. This code provides a practical demonstration of basic operations on four essential data structures in Python: lists, dictionaries, sets, and tuples.

The list is a versatile and commonly used data structure that allows for dynamic resizing and supports a variety of operations, such as appending, removing, and modifying elements. The given code snippet showcases how to create a list, add an element using append, remove an element with remove, and modify an element by directly accessing its index.

Dictionaries, another key data structure, are ideal for storing data pairs and provide fast lookup times. The code illustrates how to create a dictionary, add a new key-value pair, remove an existing key, and modify the value of an existing key.

Sets are used for storing unique elements and support operations such as addition, removal, and set-specific methods like union and intersection. The code example demonstrates creating a set, adding an element with add, removing an element with remove, and modifying the set by removing and adding elements.

Lastly, tuples are immutable sequences, typically used to store collections of heterogeneous data. While they cannot be modified directly, this code shows how to access a tuple's element and update it by converting the tuple to a list, modifying the list, and converting it back to a tuple.

Through these examples, the code provides a comprehensive overview of basic operations on lists, dictionaries, sets, and tuples, equipping you with foundational skills for effective data manipulation in Python.


# Implementation

• Python Lists: Utilize Python's built-in list data structure for creating and manipulating ordered collections of items.

• Python Dictionaries: Use Python dictionaries to store and manage key-value pairs, enabling efficient data retrieval and updates.

• Python Sets: Implement Python sets for handling collections of unique items, providing efficient membership tests and set operations.

• Python Tuples: Employ Python tuples to store immutable sequences of elements, useful for fixed collections of items.


# CODE EXPLANATION



# Python Lists:

## Creating and Modifying Lists:

### • Creating a List:

my_list = [1, 2, 3, 4, 5]

• Initializes a list named my_list with elements 1, 2, 3, 4, and 5.

### • Adding an Element:

my_list.append(6)

• Adds the element 6 to the end of my_list.

### • Removing an Element:

my_list.remove(3)

• Removes the first occurrence of the element 3 from my_list.

### • Modifying an Element:

my_list[0] = 10

• Changes the first element of my_list from 1 to 10.

## Output:

print("Updated list:", my_list)

• Displays the updated list: [10, 2, 4, 5, 6].


# Python Dictionaries:

## Creating and Modifying Dictionaries:

### • Creating a Dictionary:

my_dict = {'name': 'John', 'age': 25, 'city': 'Delhi'}

• Initializes a dictionary named my_dict with keys 'name', 'age', and 'city'.

### • Adding a Key-Value Pair:

my_dict['gender'] = 'Male'

• Adds a new key-value pair 'gender': 'Male' to my_dict.

### • Removing a Key-Value Pair:

del my_dict['age']

• Removes the key-value pair with the key 'age' from my_dict.

### • Modifying a Value:

my_dict['city'] = 'Mumbai'

• Changes the value associated with the key 'city' from 'Delhi' to 'Mumbai'.

## Output:

print("Updated Dictionary:", my_dict)

• Displays the updated dictionary: {'name': 'John', 'city': 'Mumbai', 'gender': 'Male'}.


# Python Sets:

## Creating and Modifying Sets:

### • Creating a Set:

my_set = {1, 2, 3, 4, 5}

• Initializes a set named my_set with elements 1, 2, 3, 4, and 5.

### • Adding an Element:

my_set.add(6)

• Adds the element 6 to my_set.

### • Removing an Element:

my_set.remove(3)

• Removes the element 3 from my_set.

### • Modifying the Set:

my_set.discard(1)
my_set.add(10)

• Discards the element 1 and adds the element 10 to my_set.

## Output:

print("Updated Set:", my_set)

• Displays the updated set: {2, 4, 5, 6, 10}.


# Python Tuples:

## Creating and Modifying Tuples:

### • Creating a Tuple:

my_tuple = (1, 2, 3, 4, 5)

• Initializes a tuple named my_tuple with elements 1, 2, 3, 4, and 5.

### • Accessing an Element:

print(my_tuple[2])

• Prints the third element of my_tuple: 3.

### • Updating a Tuple:

new_my_tuple = list(my_tuple)
new_my_tuple[1] = 6
my_tuple = tuple(new_my_tuple)

• Converts my_tuple to a list, modifies the second element to 6, and converts it back to a tuple.

## Output:

print("Updated Tuple:", my_tuple)

• Displays the updated tuple: (1, 6, 3, 4, 5).


# USAGE

**Adding an Element to the List:** Users can add an element to the list my_list by using the append method, which places the new element at the end of the list.

**Removing an Element from the List:** Users can remove an element from the list my_list by using the remove method, which deletes the first occurrence of the specified element.

**Modifying an Element in the List:** Users can change an existing element in the list my_list by accessing the element via its index and assigning a new value.

**Adding a Key-Value Pair to the Dictionary:** Users can add a new key-value pair to the dictionary my_dict by assigning a value to a new key.

**Removing a Key-Value Pair from the Dictionary:** Users can delete an existing key-value pair from the dictionary my_dict by using the del statement with the key they want to remove.

**Modifying a Value in the Dictionary:** Users can change the value associated with an existing key in the dictionary my_dict by reassigning the value to that key.

**Adding an Element to the Set:** Users can add an element to the set my_set by using the add method, which ensures the element is unique within the set.

**Removing an Element from the Set:** Users can remove an element from the set my_set by using the remove method, which deletes the specified element if it exists in the set.

**Modifying the Set:** Users can modify the set my_set by discarding an element using the discard method and adding a new element with the add method.

**Accessing an Element in the Tuple:** Users can access an element in the tuple my_tuple by using its index to retrieve the value.

**Updating a Tuple:** Since tuples are immutable, users can update a tuple my_tuple by converting it to a list, modifying the desired element, and converting it back to a tuple.



# CONCLUSION

In conclusion, this Python code example effectively demonstrates the basic operations on four fundamental data structures: lists, dictionaries, sets, and tuples. By providing clear and concise examples of how to create, modify, and manipulate these data structures, the code serves as a valuable resource for both beginners and experienced programmers looking to reinforce their understanding of these essential concepts. Through the use of Python's versatile built-in functions and methods, users can efficiently manage and manipulate data, laying the groundwork for more complex and advanced programming tasks. With continued practice and exploration of these data structures, programmers can enhance their coding proficiency and develop robust, efficient solutions to a wide range of problems.

# OUTPUT

![Python List and Dictionary Data Structure and its Operations](https://github.com/YashKadyan/PYTHON-BASICS-ID-11896/assets/66464974/926668dc-9636-4975-baca-22aded76c862)

![Python Dictionary and Set Data Structure and its Operations](https://github.com/YashKadyan/PYTHON-BASICS-ID-11896/assets/66464974/6ae9bdee-0cf1-4567-aaca-5fe4e40d5da4)

![Python Set and Tuple Data Structure and its Operations](https://github.com/YashKadyan/PYTHON-BASICS-ID-11896/assets/66464974/4f88e7a9-346a-494f-9144-9d898364b933)

![Python Tuple Data Structure and its Operations](https://github.com/YashKadyan/PYTHON-BASICS-ID-11896/assets/66464974/c8a39c36-0ba0-42f7-8547-85257db03958)
