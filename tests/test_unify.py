import numpy as np

# Needed to set up unify dispatch functions
import symbolic_pymc.unify

from unification import unify, var


def test_numpy():
    """Make sure we can unify against NumPy arrays without errors."""

    np_array = np.r_[1, 2]

    s = unify(np_array, np.r_[1, 2])
    assert s == {}

    s = unify(np_array, [1, 2])
    assert s == {}

    s = unify([1, 2], np_array)
    assert s == {}

    s = unify(np_array, var('a'))

    assert np.array_equal(s[var('a')], np.r_[1, 2])
    assert s[var('a')] is np_array

    s = unify(var('a'), np_array)
    assert np.array_equal(s[var('a')], np.r_[1, 2])
    assert s[var('a')] is np_array

    s = unify(np_array, [1, var('a')])

    assert s is False

    s = unify([1, var('a')], np_array)

    assert s is False

    s = unify(var('a'), 2, {var('a'): np_array})

    assert s is False

    s = unify(var('a'), var('b'), {var('a'): np_array})

    assert s[var('a')] is np_array
    assert s[var('b')] is np_array

    s = unify(np_array, np_array)
    assert s == {}
