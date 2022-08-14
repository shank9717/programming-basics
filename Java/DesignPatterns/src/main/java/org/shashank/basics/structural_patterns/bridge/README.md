Bridge is a structural design pattern that 
divides business logic or huge class into 
separate abstractions or hierarchies that can be 
developed/implemented independently.

In the example here, we could create 4 different concrete classes as below:

1. AndroidBasicSettings
2. IOSBasicSettings
3. AndroidAdvancedSettings
4. IOSAdvancedSettings

Instead, we can split the mobile type into a separate hierarchy and independently
add more mobile types, and parallely, we can have settings as a separate hierarchy
and add more types of settings independently. Adding more settings in the former
method requires us to create 2 more classes, but here it would just be adding 
a single class which extends Settings. This becomes extremely useful with more
implementations