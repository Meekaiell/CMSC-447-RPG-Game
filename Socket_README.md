Socket_README

The two main classes are *Socket_SKT* and *Client_SKT* which direct sent and receieved 
data between the client and server programs. 

These classes are a bit tricky to test as they require two files to communicate within a local environment. A test server program and two identical client programs have been provided to test
communications between server and multiple clients. The best way to run this through multiple terminal sessions with a program dedicated to each. The server should be run first with the 
clients started after.

The next phases will be to transition this local setup to an online environment to communicate with a local prorgram.
