Singleton design pattern is used to ensure that
only one instance of a class gets created and that 
instance is shared through the complete application.
First time, a new object will be created of that 
particular class, but subsequent creation attempts 
will just return the instance which is already created
the first time.

To achieve this, we need to first hide the constructor
to ensure a new object cannot be created each time.
Next, we need to give access to a static method to get
an instance of the class. This method will create a 
new object the first time and on subsequent calls, 
we will return the existing object which is created
on the initial call.

A common issue with the naive-approach is that this may 
not quite work in a multi-threaded environment.
If Thread-1 and Thread-2 both call the getInstance()
method simultaneously, and if the constructor takes time
to initialize, it may so happen that from both the threads
it will think that no object of that class is yet created
and may try to initialize an object of the class twice (once
from each thread) and we may end up in multiple objects of same
class. To avoid this, we need to use a thread-safe way as shown
in the example, by using a mutex lock, enclosing the logic of 
object creation in a synchronized block and performing
double checked-lock.