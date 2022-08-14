# Factory Method is a creational design pattern that provides an interface for creating objects in a superclass,
# but allows subclasses to alter the type of objects that will be created.

#  The Factory Method separates product construction code from the code that actually uses the product.
#  Therefore it’s easier to extend the product construction code independently from the rest of the code.
#
# For example, to add a new product type to the app, you’ll only need to create
# a new creator subclass and override the factory method in it.
