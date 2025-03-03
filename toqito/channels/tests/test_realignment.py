"""Test realignment."""
import numpy as np

from toqito.channels import realignment


def test_realignment_two_qubit():
    """Standard realignment map.

    When viewed as a map on block matrices, the realignment map takes each block of the original matrix and makes its
    vectorization the rows of the realignment matrix. This is illustrated by the following small example:
    """
    test_input_mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    expected_res = np.array([[1, 2, 5, 6], [3, 4, 7, 8], [9, 10, 13, 14], [11, 12, 15, 16]])
    np.testing.assert_array_equal(realignment(test_input_mat), expected_res)


def test_realignment_non_square():
    """The realignment map sends |i⟩⟨j|⊗|k⟩⟨ℓ| to |i⟩⟨k|⊗|j⟩⟨ℓ|.

    Thus it changes the dimensions of matrices if the subsystems aren't square and of the same size. The following code
    computes the realignment of an operator X∈M5,2⊗M3,7:
    """
    test_input_mat = np.arange(1, 211).reshape(15, 14)
    expected_res = np.array(
        [
            [1, 2, 3, 4, 5, 6, 7, 15, 16, 17, 18, 19, 20, 21, 29, 30, 31, 32, 33, 34, 35],
            [8, 9, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 27, 28, 36, 37, 38, 39, 40, 41, 42],
            [43, 44, 45, 46, 47, 48, 49, 57, 58, 59, 60, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77],
            [50, 51, 52, 53, 54, 55, 56, 64, 65, 66, 67, 68, 69, 70, 78, 79, 80, 81, 82, 83, 84],
            [85, 86, 87, 88, 89, 90, 91, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119],
            [92, 93, 94, 95, 96, 97, 98, 106, 107, 108, 109, 110, 111, 112, 120, 121, 122, 123, 124, 125, 126],
            [127, 128, 129, 130, 131, 132, 133, 141, 142, 143, 144, 145, 146, 147, 155, 156, 157, 158, 159, 160, 161],
            [134, 135, 136, 137, 138, 139, 140, 148, 149, 150, 151, 152, 153, 154, 162, 163, 164, 165, 166, 167, 168],
            [169, 170, 171, 172, 173, 174, 175, 183, 184, 185, 186, 187, 188, 189, 197, 198, 199, 200, 201, 202, 203],
            [176, 177, 178, 179, 180, 181, 182, 190, 191, 192, 193, 194, 195, 196, 204, 205, 206, 207, 208, 209, 210],
        ]
    )
    res = realignment(test_input_mat, np.array([[5, 3], [2, 7]]))
    np.testing.assert_array_equal(res, expected_res)


def test_realignment_non_square_list_dims():
    """Pass in dimensions are list (not np.array)."""
    test_input_mat = np.arange(1, 211).reshape(15, 14)
    expected_res = np.array(
        [
            [1, 2, 3, 4, 5, 6, 7, 15, 16, 17, 18, 19, 20, 21, 29, 30, 31, 32, 33, 34, 35],
            [8, 9, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 27, 28, 36, 37, 38, 39, 40, 41, 42],
            [43, 44, 45, 46, 47, 48, 49, 57, 58, 59, 60, 61, 62, 63, 71, 72, 73, 74, 75, 76, 77],
            [50, 51, 52, 53, 54, 55, 56, 64, 65, 66, 67, 68, 69, 70, 78, 79, 80, 81, 82, 83, 84],
            [85, 86, 87, 88, 89, 90, 91, 99, 100, 101, 102, 103, 104, 105, 113, 114, 115, 116, 117, 118, 119],
            [92, 93, 94, 95, 96, 97, 98, 106, 107, 108, 109, 110, 111, 112, 120, 121, 122, 123, 124, 125, 126],
            [127, 128, 129, 130, 131, 132, 133, 141, 142, 143, 144, 145, 146, 147, 155, 156, 157, 158, 159, 160, 161],
            [134, 135, 136, 137, 138, 139, 140, 148, 149, 150, 151, 152, 153, 154, 162, 163, 164, 165, 166, 167, 168],
            [169, 170, 171, 172, 173, 174, 175, 183, 184, 185, 186, 187, 188, 189, 197, 198, 199, 200, 201, 202, 203],
            [176, 177, 178, 179, 180, 181, 182, 190, 191, 192, 193, 194, 195, 196, 204, 205, 206, 207, 208, 209, 210],
        ]
    )
    res = realignment(test_input_mat, [[5, 3], [2, 7]])
    np.testing.assert_array_equal(res, expected_res)


def test_realignment_int_dim():
    """Pass in dimension argument as integer."""
    test_input_mat = np.arange(1, 17).reshape(4, 4)

    expected_res = np.array([1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16])

    res = realignment(test_input_mat, 1)
    np.testing.assert_array_equal(res, expected_res)
