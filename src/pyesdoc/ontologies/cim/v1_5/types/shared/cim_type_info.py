"""
.. module:: cim.v1_5.types.shared.cim_type_info.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1.5 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-04-17 17:20:28.693935.

"""

# Module imports.
import datetime
import types
import uuid



class CimTypeInfo(object):
    """A concrete class within the cim v1.5 type system.

    Encapsulates cim type information.
    """

    def __init__(self):
        """Constructor"""
        super(CimTypeInfo, self).__init__()
        self.package = str()                         # type = str
        self.schema = str()                          # type = str
        self.type = str()                            # type = str
        self.type_display_name = str()               # type = str


    def as_dict(self):
        """Returns a deep dictionary representation.

        """
        def append(d, key, value, is_iterative, is_primitive, is_enum):
            if value is None:
                if is_iterative:
                    value = []
            elif is_primitive == False and is_enum == False:
                if is_iterative:
                    value = map(lambda i : i.as_dict(), value)
                else:
                    value = value.as_dict()
            d[key] = value

        # Populate a deep dictionary.
        d = dict()
        append(d, 'package', self.package, False, True, False)
        append(d, 'schema', self.schema, False, True, False)
        append(d, 'type', self.type, False, True, False)
        append(d, 'type_display_name', self.type_display_name, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm
