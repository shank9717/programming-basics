Abstract factory is used to create a family of objects
using a "Factory" class, without worrying about concrete
implementation class.

Instead of creating each object of a class manually,
the complete task of creation of objects is given
to the factory class.

In the example given here, we want to create apps,
menus and settings for a given mobile. The mobile
could have Android OS or Apple IOS. 

We create AndroidApp/IOSApp, AndroidMenu/IOSMenu, 
etc, separately, and we finally create factory
classes AndroidFactory and IOSFactory. These
factory classes in-turn handle creation of all
the mobile features like Android/IOSApps , menus etc,
according to the mobile type.

In our Mobile class, we accept one kind of factory,
and leave the job of creating apps, menus and settings 
for the mobile to the factory.

