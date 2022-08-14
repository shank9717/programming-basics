Observer patterns allow classes to look for any
new changes in state (events) of another state object, 
without tightly coupling both the classes. The classes 
have to subscribe to the state objects and the state 
object updates all of its subscribes whenever there 
is some change in the state.

In given example, the ChatServer produces two kinds of events.
1st is the UpdateMessages event, which means that there are 
new messages sent in a particular chat. 2nd is the NumberChange
event, which notifies that some chat has their contact number
modified.

There are 2 listeners, NotificationBar and ChatClient. ChatClient
listens to both events and does necessary action to update messages
in client or to display the new contact number.

Notification bar listens to only new messages notification to notify
users of new messages.

The server just publishes the events, and the event manager forwards
the notification to all subscribed listeners.