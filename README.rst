Cuttleyack
==========

(Naive) Hierarchical color scale implementation.

Adapted from `Waldin et al., 2019`_.

The weight on the index vs. the group is controlled by the angles :math:`alpha`
and :math:`beta`:

alpha: 120; beta: 50 (positional index has more weight)

.. image:: ./examples/some_colors_a120_b50.png
    :alt: About to make the tackle, Yale Alumni Game 2017

alpha: 5; beta: 120 (group has more weight)

.. image:: ./examples/some_colors_a5_b120.png
    :alt: About to make the tackle, Yale Alumni Game 2017

Not implemented
---------------

Rotational shift not implemented (zoom).

.. _Waldin et al., 2019: https://onlinelibrary.wiley.com/doi/epdf/10.1111/cgf.13611
