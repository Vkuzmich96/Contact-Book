# Red-Black Tree Console Interface

This is a console-based implementation of a Red-Black Tree data structure in Python. It provides a user-friendly
interface to interact with the Red-Black Tree, allowing users to add records, delete records, search for records, 
display all records, and exit the program.

## Implementation Details

The Red-Black Tree is implemented using the following classes:
- `Node`: Represents a node in the Red-Black Tree. Each node stores a key-value pair, color information, and references to its children and parent nodes.
- `RedBlackTree`: Represents the Red-Black Tree data structure. It provides methods for insertion, deletion, search, and other operations on the tree.

The console interface, `RedBlackTreeConsoleInterface`, encapsulates the functionality of the Red-Black Tree and provides a menu-driven interface for users to interact with the tree.

## Instructions

1. Ensure that you have Python 3 installed on your system.

2. Download the `contacts.py` file, which contains the implementation of the Red-Black Tree and the console interface.

3. Open a terminal or command prompt and navigate to the directory where the `contacts.py` file is located.

4. Run the following command to execute the code: python contacts.py

5. The console interface will be displayed, presenting a menu of options. Enter the corresponding number for the action you wish to perform.

6. Follow the prompts on the screen to provide the required inputs for each action.

7. You can add records, delete records, search for records, display all records, and exit the program by selecting the corresponding options from the menu.

8. Continue interacting with the Red-Black Tree until you choose to exit the program.

## Example Usage

Here's an example of how you can use the Red-Black Tree console interface:

Menu:

Add a record
Delete a record
Search for a record
Display all records
Exit
Enter your choice (1-5): 1

Add a Record
Enter the name for the record: John
Enter the phone number for the record: 555-1234
Record added successfully.

Menu:

Add a record
Delete a record
Search for a record
Display all records
Exit
Enter your choice (1-5): 3

Search for a Record
Enter the name to search: John
Record found: Name: John, Phone: 555-1234

Menu:

Add a record
Delete a record
Search for a record
Display all records
Exit
Enter your choice (1-5): 4

Display Records
Name: John, Phone: 555-1234

Menu:

Add a record
Delete a record
Search for a record
Display all records
Exit
Enter your choice (1-5): 5

Exiting...
