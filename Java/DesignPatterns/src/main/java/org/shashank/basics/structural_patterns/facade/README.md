The facade design patterns allows us to provide a 
very simple and minimal interface and abstract away
the complex library behind.

This reduces the overall complexity of the application.

A facade internally uses other packages/classes to 
get most of the work done, and they usually manage the 
complete lifecycle of the object that is passed.

In the example given, the MessageFacade provides a simple
interface to send a message to a given chat ID and message.
The facade then fetches the chat with given chat ID, finds
the format of chat (image/text), and then sends the message
to the given Chat with appropriate formatting based on if it
is an image or text.