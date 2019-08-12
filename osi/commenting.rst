Commenting
===========

During the building process of open simulation interface (using the `proto2cpp <https://github.com/OpenSimulationInterface/proto2cpp>`_ filter), doxygen is creating a documentation processing all comments written in the code of the interface. In order to do that doxygen needs the comments to be written in a certain way. Please follow these rules to achieve that the documentation is created correctly. You will find further information on doxygen `here <http://www.doxygen.nl/manual/docblocks.html>`_.

For any additional comment styles see `list <http://www.doxygen.nl/manual/commands.html>`_ of doxygen commands.

Commenting with block syntax
-----------------------------
Please start every comment with ``//`` and do not use ``///``.


Commenting on messages
------------------------
When writing comments specifying messages please use the following template:

.. code-block:: protobuf

    // <Add your single line comment like this>
    //
    message ExampleMessage
    {
    ...
    }


Commenting on fields and enums
---------------------------------
Doxygen will interpret a comment consisting just of one single line as a brief description. However to keep the style of the documentation coherent there should not be any brief description when commenting on fields and enums. That is why adding one more empty line when commenting just one line becomes necessary.

.. code-block:: proto

    // <Add your single line comment like this>
    //
    message ExampleMessage
    {
    ...
    }


There is no need for an extra empty line if you are commenting more than one line anyways.

.. code-block:: proto
    
    // <If you write two or more lines of comments...>
    // <... you do not need to add an empty line>
    message ExampleMessage
    {
    ...
    }


Commenting with doxygen references
------------------------------------
If you need to reference to another message etc., you can achieve that by just using the exact same name of this message (upper and lower case sensitive) in your comment and put '\c' in front of the message name.

.. code-block:: proto

    // A reference to \c GroundTruth message.

If you want to reference a nested message, use '::' instead of '.' as separators in comments.

If you want to reference message fields and enums add '#' to the enum/field name.

.. code-block:: proto

    // A reference to a enum e.g. \c #COLOR_GREEN.

Commenting with links
----------------------
With ``[<add name of your link>](<add url of your link>)`` you can integrate a link to a certain homepage while commenting.

Commenting with images
----------------------
To include images write your comment similar to this ``// \image html <Add name of your image> "<Add optional caption here>"``
Please place all your included images in ``./open-simulation-interface/docs/images``.
