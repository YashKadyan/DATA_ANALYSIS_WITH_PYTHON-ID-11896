#!/usr/bin/env python
# coding: utf-8

# In[1]:


# creating a list
my_list = [1, 2, 3, 4, 5]

# adding an element to the list
my_list.append(6)

# removing an element from the list
my_list.remove(3)

# modifying an element in the list
my_list[0] = 10

print("Updated list:", my_list)

# output
Updated list: [10, 2, 4, 5, 6]

# In[2]:


# creating dictionary
my_dict = {'name' : 'John', 'age' : 25, 'city' : 'Delhi'}

# adding
my_dict['gender'] = 'Male'

# removing
del my_dict['age']

# modifying
my_dict['city'] = 'Mumbai'

print('Updated Dictionary:', my_dict)

# output
Updated Dictionary: {'name': 'John', 'city': 'Mumbai', 'gender': 'Male'}

# In[3]:


# creating a set
my_set = {1, 2, 3, 4, 5}

# adding
my_set.add(6)

# removing
my_set.remove(3)

# modifying
my_set.discard(1)
my_set.add(10)

print("Updated Set:", my_set)

# output
Updated Set: {2, 4, 5, 6, 10}

# In[9]:


# creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# accessing
print(my_tuple[2])

# output
3

# In[10]:


# updating
new_my_tuple = list(my_tuple)
new_my_tuple[1] = 6
my_tuple = tuple(new_my_tuple)
print("Updated Tuple:", my_tuple)

# output
Updated Tuple: (1, 6, 3, 4, 5)