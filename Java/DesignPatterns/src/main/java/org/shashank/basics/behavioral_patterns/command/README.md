Command pattern is used to encapsulate all information 
needed to perform an action or trigger an event at a 
later time. This information includes the method name, 
the object that owns the method and values for the 
method parameters.

There is an Invoker class which knows how to execute a 
command, so it refers to the Command class to perform
a command. The command object in turn invokes a method
of the receiver.

The Invoker may also be performing bookkeeping of 
all the commands executed so that it can amend any 
execution at a later stage.