"""Symmetric projection operator."""
import math
from itertools import permutations

import numpy as np
import scipy

from toqito.perms import permutation_operator


def symmetric_projection( dim: int, p_val: int = 2, partial: bool = False ) -> [np.ndarray, scipy.sparse.lil_matrix]:
    r"""Produce the projection onto the symmetric subspace :cite:`Chen_2014_Symmetric`.

    For a complex Euclidean space :math:`\mathcal{X}` and a positive integer :math:`n`, the projection onto the
    symmetric subspace is given by

    .. math::
        \frac{1}{n!} \sum_{\pi \in S_n} W_{\pi}

    where :math:`W_{\pi}` is the swap operator and where :math:`S_n` is the symmetric group on :math:`n` symbols.

    Produces the orthogonal projection onto the symmetric subspace of :code:`p_val` copies of `dim`-dimensional space.
    If `partial = True`, then the symmetric projection (PS) isn't the orthogonal projection itself, but rather a matrix
    whose columns form an orthonormal basis for the symmetric subspace (and hence the PS * PS' is the orthogonal
    projection onto the symmetric subspace).

    This function was adapted from the QETLAB package.

    Examples
    ==========

    The :math:`2`-dimensional symmetric projection with :math:`p=1` is given as :math:`2`-by-:math:`2` identity matrix

    .. math::
        \begin{pmatrix}
            1 & 0 \\
            0 & 1
        \end{pmatrix}.

    Using :code:`toqito`, we can see this gives the proper result.

    >>> from toqito.perms import symmetric_projection
    >>> symmetric_projection(2, 1)
    array([[1., 0.],
           [0., 1.]])

    When :math:`d = 2` and :math:`p = 2` we have that

    .. math::
        \begin{pmatrix}
            1 & 0 & 0 & 0 \\
            0 & 1/2 & 1/2 & 0 \\
            0 & 1/2 & 1/2 & 0 \\
            0 & 0 & 0 & 1
        \end{pmatrix}.

    Using :code:`toqito` we can see this gives the proper result.

    >>> from toqito.perms import symmetric_projection
    >>> symmetric_projection(dim=2)
    array([[1. , 0. , 0. , 0. ],
           [0. , 0.5, 0.5, 0. ],
           [0. , 0.5, 0.5, 0. ],
           [0. , 0. , 0. , 1. ]])

    References
    ==========
    .. bibliography::
        :filter: docname in docnames


    :param dim: The dimension of the local systems.
    :param p_val: Default value of 2.
    :param partial: Default value of 0.
    :return: Projection onto the symmetric subspace.

    """
    dimp = dim ** p_val

    if p_val == 1:
        return np.eye(dim)

    p_list = np.array(list(permutations(np.arange(1, p_val + 1))))
    p_fac = math.factorial(p_val)
    sym_proj = np.zeros((dimp, dimp))

    for j in range(p_fac):
        sym_proj += permutation_operator(dim * np.ones(p_val), p_list[j, :], False, True)
    sym_proj = sym_proj / p_fac

    if partial:
        sym_proj = scipy.linalg.orth(sym_proj)
    return sym_proj
