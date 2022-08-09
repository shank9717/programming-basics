Flyweight pattern aims to reduce memory consumption
in a memory heavy application. This will be used 
excessively in graphic rendering, when multiple
objects (in thousands or millions) of same Class 
but with different properties have to be rendered.
We can cache most common properties and reuse them,
by moving these properties into a separate class that
can be created only once.