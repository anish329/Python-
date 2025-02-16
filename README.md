Task Counter Application Description
This Python application, built using Tkinter for the graphical user interface (GUI), allows users to track tasks and their counts, saving progress to a JSON file for persistence.

Features:
Task Input: Users can enter a task name into a text entry field.
Counter Functionality:
Increment Button: Increases the task count by one.
Reset Button: Resets the task count to zero.
Data Persistence:
On startup, the application loads the task name and count from a counter_data.json file if it exists.
On exit, the application saves the current task name and count to the same JSON file.
How the Code Works:
Initialization (__init__ method):
Sets up the Tkinter window with labels, an entry field, and buttons.
Initializes the count from the JSON file using the load_count() method.
Counter Operations:
increment(): Increases the count and updates the display label.
reset_count(): Resets the count to zero and updates the display label.
update_label(): Refreshes the count label with the current value.
Saving Data:
save_and_exit(): Saves the task name and count to counter_data.json in JSON format and closes the application.
JSON File Operations:
load_count(): Reads task name and count from counter_data.json if the file exists.
File Structure:
counter_data.json: Stores task name and count as:
json
Copy
Edit
{
  "task": "Sample Task",
  "count": 5
}
Usage:
Run the script.
Enter a task name.
Click "Increment" to count.
Click "Reset" to restart counting.
Click "Save & Exit" to store the data and close the app.
