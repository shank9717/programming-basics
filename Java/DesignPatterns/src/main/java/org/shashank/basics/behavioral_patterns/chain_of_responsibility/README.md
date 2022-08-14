Chain of Responsibility is used to pass a request
through a chain of handler objects and each handler
can process the request, and pass on to the next handler,
or reject the request.

In the given example, we have multiple interceptors (Authentication
and DOS Protection). The server first registers all the handlers
(interceptors) and when the client code sends a login request
to the server, with the username and password, the server sends the
request through all the registered interceptors. At each stage it can
either pass or flow through and finally accept the request to login.