Strategy patterns let us define the interface of an interchangeable 
family of algorithms, put the algorithm implementation details in 
derived classes and let the client couple itself strictly to the 
interface only.


In the given example, the mobile attempts to open a URL. There are
3 different strategies (apps) available to open the URL. Depending on
user choice, we can open the hyperlink in corresponding application.