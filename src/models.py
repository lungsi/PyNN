"""
Base classes for cell and synapse models, whether "standard" (cross-simulator)
or "native" (restricted to an individual simulator).

:copyright: Copyright 2006-2011 by the PyNN team, see AUTHORS.
:license: CeCILL, see LICENSE for details.
"""

import copy
from pyNN import errors, descriptions

class BaseModelType(object):
    """Base class for standard and native cell and synapse model classes."""
    default_parameters = {}
    default_initial_values = {}

    @classmethod
    def has_parameter(cls, name):
        return name in cls.default_parameters
    
    @classmethod
    def get_parameter_names(cls):
        return cls.default_parameters.keys()
    
    @classmethod
    def get_schema(cls):
        return dict((name, type(value))
                    for name, value in cls.default_parameters.items())
    
    @classmethod
    def describe(cls, template='modeltype_default.txt', engine='default'):
        """
        Returns a human-readable description of the cell or synapse type.
        
        The output may be customized by specifying a different template
        togther with an associated template engine (see ``pyNN.descriptions``).
        
        If template is None, then a dictionary containing the template context
        will be returned.
        """
        context = {
            "name": cls.__name__,
            "default_parameters": cls.default_parameters,
            "default_initial_values": cls.default_initial_values,
        }
        return descriptions.render(engine, template, context)


class BaseCellType(BaseModelType):
    """Base class for cell model classes."""
    recordable = []
    synapse_types = []
    conductance_based = True # override for cells with current-based synapses
    injectable = True # override for spike sources


class BaseCurrentSource(BaseModelType):
    """Base class for current source model classes."""


class BaseSynapseDynamics(object):
    pass
