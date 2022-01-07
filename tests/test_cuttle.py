"""Test that color mapping does not raise."""

from cuttleyak import cuttle


def test_color_map_works():
    some_groups = [[1, 2, 3], [3, 4], [4, 5]]
    angle_colors = cuttle.map_groups_to_colors(some_groups)
    assert len(angle_colors) == len(some_groups)
    for g, a in zip(some_groups, angle_colors):
        assert len(g) == len(a)
