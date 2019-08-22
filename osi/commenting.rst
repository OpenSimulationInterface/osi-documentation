.. _commenting:

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
Doxygen will interpret a comment consisting just of one single line as a brief description.
However to keep the style of the documentation coherent there should not be any brief description when commenting on fields and enums. That is why adding one more empty line when commenting just one line becomes necessary.

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

.. _commenting-with-rules:

Commenting on fields with rules
--------------------------------
When adding rules to \*.proto files make sure that the rules are encapsulated between the ``\rules`` and ``\endrules`` tags. The rule ``is_set`` needs always to be provided.

.. code-block:: proto
    
    // Description ExampleMessage
    //
    message ExampleMessage
    {
        // Description ExampleField
        //
        // \rules
        // is_set
        // is_greater_than_or_equal_to: 3
        // is_less_than_or_equal_to: 10
        // \endrules
        // 
        optional int ExampleField = 1;
    }
    
The rule defintion must follow the syntax which is defined by a regex search which you can see below:

.. code-block:: python
    
    'is_greater_than':              r'\b(is_greater_than)\b: \d+(\.\d+)?'               # is_greater_than: 1
    'is_greater_than_or_equal_to':  r'\b(is_greater_than_or_equal_to)\b: \d+(\.\d+)?'   # is_greater_than_or_equal_to: 1
    'is_less_than_or_equal_to':     r'\b(is_less_than_or_equal_to)\b: \d+(\.\d+)?'      # is_less_than_or_equal_to: 10
    'is_less_than':                 r'\b(is_less_than)\b: \d+(\.\d+)?'                  # is_less_than: 2
    'is_equal':                     r'\b(is_equal)\b: \d+(\.\d+)?'                      # is_equal: 1
    'is_different':                 r'\b(is_different)\b: \d+(\.\d+)?'                  # is_different: 2
    'is_global_unique':             r'\b(is_global_unique)\b'                           # is_global_unique
    'refers':                       r'\b(refers)\b'                                     # refers
    'is_iso_country_code':          r'\b(is_iso_country_code)\b'                        # is_iso_country_code
    'first_element':                r'\b(first_element)\b: \{.*: \d+\.\d+\}'            # first_element: {is_equal: 0.13, is_greater_than: 0.13}
    'last_element':                 r'\b(last_element)\b: \{.*: \d+\.\d+\}'             # last_element: {is_equal: 0.13, is_greater_than: 0.13}
    'is_optional':                  r'\b(is_optional)\b'                                # is_optional
    'check_if':                     r'\b(check_if)\b: \{.*: \{.*: \[.*\]\}\}'           # check_if: {is_different: {do_check: [is_set, is_equal]}}
    'is_set':                       r'\b(is_set)\b'}                                    # is_set

You can check the correctness of these regular expression on `regex101 <https://regex101.com/r/6tomm6/14>`_.

.. is_greater_than: 2
.. is_greater_than: 2.23
.. is_greater_than_or_equal_to: 1
.. is_greater_than_or_equal_to: 1.12
.. is_less_than_or_equal_to: 10
.. is_less_than_or_equal_to: 10.123
.. is_less_than: 2
.. is_less_than: 2.321
.. is_equal: 1
.. is_equal: 1.312
.. is_different: 2
.. is_different: 2.2122
.. is_global_unique
.. refers
.. is_iso_country_code
.. first_element: {is_equal: 3, is_greater: 2}
.. first_element: {is_equal: 0.13, is_greater: 0.13}
.. last_element: {is_equal: 3, is_greater: 2}
.. last_element: {is_equal: 0.13, is_greater: 0.13}
.. check_if: {is_different: {do_check: [is_set, is_equal]}}
.. is_set
 

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

