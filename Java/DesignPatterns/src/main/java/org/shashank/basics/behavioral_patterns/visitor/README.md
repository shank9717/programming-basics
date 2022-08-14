Visitor pattern lets us separate algorithms from the objects on which they operate.
It uses a technique called Double-Dispatch to execute the right method on the object, 
where the choice is given to the object called the method instead of the client. Each
class accepts a visitor and the class then decides which method has to be called on 
the visitor. The visitor will have corresponding methods that accept each class and 
perform some action.

We can take the example of MessagingApplication and chats as mentioned in Composite
pattern. We have different types of chats - personal, group or broadcast. We want to
export a group of different chats. Rather than writing the export algorithm in each
of the 3 classes of chats, we can have a ExportChatVisitor class that has 3 different
methods to export each type of chat. We can then iterate over each chat and then call
the corresponding export chat method in the visitor. If the client has to iterate 
over each type of chat, it will have to perform type-check and then call the necessary
method. Instead of this, we can add a simple accept() method in each chat class, 
where it accepts one visitor and then calls the necessary method on the visitor.
This way, the chat class itself can decide which method has to be called. Now the client
can simply iterator over each chat class object and call the accept method without doing
any type check.