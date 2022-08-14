State pattern allows an object to change its own behavior
when some state of the object has been modified. The state
related behaviors are extracted to a separate classes, and the
state specific work is performed by these classes. It is useful
when the object has a lot of possible states, and the behavior
of the object is different in each state.

In the given example, we have a mobile class having 3 states for handling
incoming calls. If set to SilentState, and if the mobile receives a call,
it will ask the state to perform the ring action. The silent state will
silently ring by just displaying caller ID. If set to VibrateState, on
receiving a call, the mobile will ask the current state to handle the call.
The VibrateState will call the vibrate method on the mobile and show the 
called ID as well.