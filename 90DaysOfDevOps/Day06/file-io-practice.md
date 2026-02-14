#### Linux File I/O Practice





##### 1\. Create a File



Command:

'touch notes.txt'



What it did:

Created an empty file named notes.txt.



##### 2\. Write Text (Overwrite Mode)



Command:

'echo "Day 06 – File practice started" > notes.txt'



What it did:

Created the first line and overwrote any previous content.



##### 3\. Append Text



Command:

'echo "Practicing redirection operators" >> notes.txt'



Command:

'echo "Learning how logs are handled" >> notes.txt'



What it did:

Appended new lines without deleting existing content.



##### 4\. Use tee (Write + Display)



Command:

'echo "tee writes and shows output together" | tee -a notes.txt'



What it did:

Displayed the line on terminal and appended it to the file.



##### 5\. Read Full File



Command:

'cat notes.txt'



Observation:

Displayed all lines in the file.



##### 6\. Read Partial File



Command:

'head -n 2 notes.txt'



What it did:

Displayed first 2 lines.



Command:

'tail -n 2 notes.txt'



What it did:

Displayed last 2 lines.

