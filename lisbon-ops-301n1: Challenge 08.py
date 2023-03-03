#!/bin/python


#Script         Ops Challenge: Class 08 - Python Collections
#Purpose        Create a Python script that prints and manipulates strings from a list
#Why            Learn how to make a list, print elements contained within and manipulate it

# Creating a list of fruits
fruits = ["Apple","Banana","Pear","Orange","Pineapple","Strawberry","Grapefruit","Pomegranate","Blueberry","Grape"]

# Prints the third element of the list
print(fruits[3])

# Prints elements 5 to 9
print(fruits[5:9])

# Replace element number 6 for the string "Onion"
fruits[6] = "Onion" 
print(fruits[6])

# append() - Adds an element to the end of the list
fruits.append("Kiwi")
print(fruits)

# copy() - Returns a copy of the list
fruits = ["Apple", "Banana", "Pear", "Orange", "Pineapple", "Strawberry", "Grapefruit", "Pomegranate", "Blueberry", "Grape"]
fruits_copy = fruits.copy()
print(fruits_copy)

# count() - Returns the number of occurrences of an element in the list
print(fruits.count("Grape"))

# extend() - Adds elements from another list to the end of the current list
even_more_fruits = ["Mango", "Papaya", "Watermelon"]
fruits.extend(even_more_fruits)
print(fruits)

# index() - Returns the index of the first occurrence of an element in the list
print(fruits.index("Pear"))

# insert() - Inserts an element at a specific position in the list
fruits.insert(2, "Cherry")
print(fruits)

# pop() - Removes and returns the last element from the list
last_fruit = fruits.pop()
print(last_fruit)
print(fruits)

# remove() - Removes the first occurrence of an element from the list
fruits.remove("Pineapple")
print(fruits)

# reverse() - Reverses the order of the elements in the list
fruits.reverse()
print(fruits)

# sort() - Sorts the elements in the list in ascending order
fruits.sort()
print(fruits)

# sort() - Sorts the elements in the list in descending order
fruits.sort(reverse=True)
print(fruits)

# clear() - Removes all elements from the list
fruits.clear()
print(fruits)

# Create a tuple
tuple = ("apple", "banana", "cherry")
print(tuple)

# Create a set
set = {"apple", "banana", "cherry"}
print(set)

# Create a dictionary
dict = {
  "Fruit Name": "Watermelon",
  "Scientific Name": "Citrullus lanatus",
  "Family": "Cucurbitaceae"
}
print(dict)