Adapter design pattern is used to make 2 different
types of objects compatible with each other, by sitting
in between both these classes, and basically converting 
the data communicated from 1st class into a format 
understandable by the other class.

In the given example, we have a round hole class, and
we want to figure out if any arbitrary object can fit
into the hole. Since the hole is round, the class is
designed to accept cylindrical objects by default.

If we want to check a cube will fit in this hole, 
we cannot directly pass the cube object into the 
hole, as it doesn't accept non-cylindrical objects.
Hence, we can use a Cube-To-Cylinder Adapter to
calculate the maximum radius cylinder which can 
completely encapsulate the given cube, and in turn
pass that radius to the round hole and the round 
hole can check if the new object will fit in the
hole. Since the adapter extends or implements the
cylindrical shape, it will accept the adapter 
object to be passed to the hole.

The adapter acts a wrapper between the objects.