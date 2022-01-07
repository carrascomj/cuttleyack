"""Cuttlefish algorithm for color mapping of hierarchical categories.

Adapted from `Waldin et al., 2019`_.

.. _Waldin et al., 2019: https://onlinelibrary.wiley.com/doi/epdf/10.1111/cgf.13611
"""

import logging
from typing import List, Optional

from .color_space import hsv_to_rgb, normalize_hue


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def map_groups_to_colors(
    groups: List, alpha: float = 20.0, beta: Optional[float] = None
) -> List:
    """Compute a color scale from a hierarchical group.

    Items within and between groups are only separated by hue. Similar groups
    are similar by position and will have similar groups.

    Parameters
    ----------
    groups: list
        list of lists.
    alpha: float
        max distance (in degrees [0, 360]) between two items in the same group.

    Returns
    -------
    hues: list
        a list of 3-dim vectors representing RGB values, in the same structure
        than `groups`.
    """
    m = [len(k) for k in groups]
    beta = scale_beta(len(m)) if beta is None else beta
    alpha = 20
    LOGGER.info(f"alpha: {alpha}; beta: {beta}")
    hues = [
        [
            hsv_to_rgb([normalize_hue(compute_hue(i, j, beta, alpha, m_k=m)), 1, 1])
            for i in range(m[j])
        ]
        for j in range(len(m))
    ]
    return hues


def compute_hue(
    i: int, j_group: int, alpha: float, beta: float, m_k: List[float]
) -> float:
    r"""Get the :math:`h_{ij}` of item `i` in group `j`.

    .. math::

        h_{ij} = (i-1) * \beta + (\sum_{k=1}^(i-1) m_k) + (j-1) * \alpha

    Parameters
    ----------
    i: int
        index of item in group
    j_group: int
        index of group
    alpha: float
        angle
    beta: float
        angle
    m_k: list[int]
        number of visible items in group k
    """
    return (i - 1) * beta + sum(m_k[k] for k in range(1, i - 1)) + (j_group - 1) * alpha


def scale_beta(n: int) -> float:
    """Get :math:`beta` parameter.

    Parameters
    ----------
    n: int
        number of visible groups

    Returns
    -------
    beta: float
        angle between two neighbouring groups.
    """
    return 360 / n


def scale_alpha(m: List[int]) -> float:
    r"""Get :math:`alpha` parameter.

    ::math

        s_{alpha} = \frac{360 - n * \beta}{\sum_{i=1}^n (m_i - 1)}

    Parameters
    ----------
    m: list[float]
        number of items per group.

    Returns
    -------
    alpha: float
        between two neighbouring items inside a group

    """
    n = len(m)
    beta = scale_beta(n)
    return (360 - n * beta) / (sum(m) - n)
