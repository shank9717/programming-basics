Mediator pattern allows indirect communication between
classes using a Mediator class. Direct communication
between classes is reduced and most if not all communication
has to go via Mediator. This will allow us to decouple 
tightly coupled classes.

In the given example, we have two users, UserA and UserB,
both who want to communicate with each other. If we write
methods to send messages to each other directly, it would 
be very tightly coupled, and we cannot use UserA as a generic
class elsewhere. Hence, we create a chat server, which both 
users have access to. UserA and UserB can user this ChatServer
as a mediator to communicate. When UserA has to call sendMessage
it forwards the request to the mediator and asks the mediator 
to check the request and perform necessary action of sending
message to UserB.