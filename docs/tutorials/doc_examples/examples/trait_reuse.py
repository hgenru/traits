# trait_reuse.py --- Example of reusing trait definitions

#--[Imports]--------------------------------------------------------------------
from enthought.traits.api import HasTraits, Range, Trait, TraitRange

#--[Code]-----------------------------------------------------------------------
coefficient = Range(-1.0, 1.0, 0.0))

class quadratic(HasTraits):
    c2 = coefficient
    c1 = coefficient
    c0 = coefficient
    x  = Range(-100.0, 100.0, 0.0)
