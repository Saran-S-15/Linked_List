Linked List Implementation in Python

Overview

This project implements a Singly Linked List in Python, providing basic operations like adding, deleting, and traversing nodes. The code is structured with two classes: Node for representing each node and LinkedList for managing the list.

Features

Operations on the Linked List:
	1.	Add Operations:
	•	add_begin(data): Add a node at the beginning of the linked list.
	•	add_end(data): Add a node at the end of the linked list.
	•	add_after(data, x): Add a node after the node containing data x.
	•	add_before(data, x): Add a node before the node containing data x.
	2.	Delete Operations:
	•	delete_begin(): Remove the first node of the linked list.
	•	delete_end(): Remove the last node of the linked list.
	•	delete_value(x): Remove the node containing data x.
	3.	Print the Linked List:
	•	printLL(): Traverse and print all the nodes in the linked list.

Code Structure

Node Class

Represents a single node in the linked list:
	•	data: The value stored in the node.
	•	next: Pointer to the next node in the list.

LinkedList Class

Manages the linked list:
	•	head: The starting node of the list.
	•	Includes methods for adding, deleting, and printing nodes.

Usage

Example Operations

# Create a new linked list
ll = LinkedList()

# Add nodes
ll.add_begin(20)     # Add 20 at the beginning
ll.add_begin(10)     # Add 10 at the beginning
ll.add_end(30)       # Add 30 at the end
ll.add_after(500, 20) # Add 500 after the node with data 20
ll.add_before(1000, 30) # Add 1000 before the node with data 30

# Delete nodes
ll.delete_begin()    # Delete the first node
ll.delete_end()      # Delete the last node
ll.delete_value(1000) # Delete the node with data 1000

# Print the linked list
ll.printLL()

Output Example

20 ---> 500 ---> 30 ---> 

Notes
	•	Edge cases, such as trying to delete or add around non-existent nodes, are handled with appropriate messages.
	•	If the linked list is empty, deletion methods display a message.

Enhancements
	•	Add support for doubly linked lists.
	•	Include a search operation for finding nodes.
	•	Implement reverse traversal.

Feel free to modify and extend the functionality!
