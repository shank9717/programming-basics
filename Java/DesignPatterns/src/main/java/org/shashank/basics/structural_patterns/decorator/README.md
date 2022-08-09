Decorator pattern allows stacking of multiple classes
implementing same interface on top of each other, so 
that we can execute a function using different implementations
in a chained fashion. Decorators act like wrappers on another
class.


In the given example, if we want to create a notification class
to notify both Reddit and Discord, we would have to create a 
class called RedditAndDiscordNotifier. Instead, we can leverage
decorator pattern, to create RedditNotificationDecorator and have
it in turn call the DiscordNotificationDecorator or vice-versa. This
way we can execute something similar to a chain of commands.