Prototype pattern suggests that we leave the job
of copying (or cloning) an object belonging to a class
to the same class itself. Since the class is aware of
all of its properties, it can efficiently copy all of 
its properties into the new object and return a new
copy.

In the example given here, we have a constructor to 
create an object based on a pre-existing object.
The clone method in Bike class or Car class uses the constructor
to return a new object with all the properties intact.

We can efficiently create a deep-copy and return a new
object this way.
