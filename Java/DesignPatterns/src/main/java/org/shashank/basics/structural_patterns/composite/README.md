Composite structural pattern suggests we compose
multiple classes into tree structures and work 
with these structures. When a task is to be performed,
we call this task to be performed on the composite 
class and that in turn asks each child to perform
the same task.

In the given example, Chat is the basic class, with
Personal and Group chats as leaf classes. BroadCast chat
is a composite class which may contain one or more group chats
or personal chats. MessagingApplication manages both simple
and composite classes together to perform common operations.

Broadcast chat takes simple commands like sendMessage() and 
delegates it to all of its children recursively.