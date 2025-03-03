"""Tests for XORGame class."""
import unittest

import numpy as np

from toqito.nonlocal_games.xor_game import XORGame


class TestXORGame(unittest.TestCase):
    """Unit test for XORGame."""

    def test_chsh_game_quantum_value(self):
        """Quantum value for the CHSH game."""
        prob_mat = np.array([[1 / 4, 1 / 4], [1 / 4, 1 / 4]])
        pred_mat = np.array([[0, 0], [0, 1]])

        chsh = XORGame(prob_mat, pred_mat)
        res = chsh.quantum_value()
        expected_res = np.cos(np.pi / 8) ** 2
        self.assertEqual(np.isclose(res, expected_res), True)

    def test_chsh_game_quantum_value_error_tol(self):
        """Quantum value for the CHSH game with error tolerance."""
        prob_mat = np.array([[1 / 4, 1 / 4], [1 / 4, 1 / 4]])
        pred_mat = np.array([[0, 0], [0, 1]])
        reps = 1
        tol = 1e-4

        chsh = XORGame(prob_mat, pred_mat, reps, tol)
        res = chsh.quantum_value()
        expected_res = np.cos(np.pi / 8) ** 2
        self.assertEqual(np.isclose(res, expected_res), True)

    def test_chsh_game_quantum_value_two_reps(self):
        """Quantum value for two repetitions of the CHSH game."""
        prob_mat = np.array([[1 / 4, 1 / 4], [1 / 4, 1 / 4]])
        pred_mat = np.array([[0, 0], [0, 1]])
        reps = 2

        chsh = XORGame(prob_mat, pred_mat, reps)
        res = chsh.quantum_value()
        expected_res = np.cos(np.pi / 8) ** 4
        self.assertEqual(np.isclose(res, expected_res), True)

    def test_chsh_game_classical_value(self):
        """Classical value for the CHSH game."""
        prob_mat = np.array([[1 / 4, 1 / 4], [1 / 4, 1 / 4]])
        pred_mat = np.array([[0, 0], [0, 1]])

        chsh = XORGame(prob_mat, pred_mat)
        res = chsh.classical_value()
        expected_res = 3 / 4
        self.assertEqual(np.isclose(res, expected_res), True)

    def test_chsh_game_classical_value_tol_optimal(self):
        """Classical value for the CHSH game with optimal tolerance."""
        prob_mat = np.array([[1 / 4, 1 / 4], [1 / 4, 1 / 4]])
        pred_mat = np.array([[0, 0], [0, 1]])

        chsh = XORGame(prob_mat, pred_mat, 1)
        res = chsh.classical_value()
        expected_res = 3 / 4
        self.assertEqual(np.isclose(res, expected_res), True)

    def test_chsh_game_classical_value_early_exit(self):
        """Classical value for the CHSH game where early exit condition occurs."""
        prob_mat = np.array([[1 / 4, 1 / 4], [1 / 4, 1 / 4]])
        pred_mat = np.array([[1, 1], [1, 1]])

        chsh = XORGame(prob_mat, pred_mat, 1, 1e-10)
        res = chsh.classical_value()
        expected_res = 1
        self.assertEqual(np.isclose(res, expected_res), True)

    def test_odd_cycle_game_quantum_value(self):
        """Quantum value for the odd-cycle game."""
        prob_mat = np.array(
            [
                [0.1, 0.1, 0, 0, 0],
                [0, 0.1, 0.1, 0, 0],
                [0, 0, 0.1, 0.1, 0],
                [0, 0, 0, 0.1, 0.1],
                [0.1, 0, 0, 0, 0.1],
            ]
        )

        pred_mat = np.array(
            [
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0],
            ]
        )
        odd_cycle = XORGame(prob_mat, pred_mat)
        res = odd_cycle.quantum_value()
        expected_res = 0.975528
        self.assertEqual(np.isclose(res, expected_res), True)

    def test_odd_cycle_game_classical_value(self):
        """Classical value for the odd-cycle game."""
        prob_mat = np.array(
            [
                [0.1, 0.1, 0, 0, 0],
                [0, 0.1, 0.1, 0, 0],
                [0, 0, 0.1, 0.1, 0],
                [0, 0, 0, 0.1, 0.1],
                [0.1, 0, 0, 0, 0.1],
            ]
        )

        pred_mat = np.array(
            [
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0],
            ]
        )
        odd_cycle = XORGame(prob_mat, pred_mat)
        res = odd_cycle.classical_value()
        expected_res = 0.9
        self.assertEqual(np.isclose(res, expected_res), True)

    def test_classical_parallel_rep(self):
        """Tests for classical value parallel reps."""
        prob_mat = np.array([[1 / 4, 1 / 4], [1 / 4, 1 / 4]])
        pred_mat = np.array([[0, 0], [0, 1]])

        game = XORGame(prob_mat, pred_mat, 2)
        res = game.classical_value()
        self.assertEqual(res, 0.625)

    def test_negative_prob_mat(self):
        """Tests for invalid negative probability matrix."""
        with self.assertRaises(ValueError):
            prob_mat = np.array([[1 / 4, -1 / 4], [1 / 4, 1 / 4]])
            pred_mat = np.array([[0, 0], [0, 1]])

            game = XORGame(prob_mat, pred_mat)
            game.quantum_value()

    def test_invalid_prob_mat(self):
        """Tests for invalid probability matrix."""
        with self.assertRaises(ValueError):
            prob_mat = np.array([[1 / 4, 1], [1 / 4, 1 / 4]])
            pred_mat = np.array([[0, 0], [0, 1]])

            game = XORGame(prob_mat, pred_mat)
            game.quantum_value()

    def test_non_square_prob_mat(self):
        """Tests for invalid non-square probability matrix."""
        with self.assertRaises(ValueError):
            prob_mat = np.array([[1 / 4, 1 / 4, 1 / 4], [1 / 4, 1 / 4, 1 / 4]])
            pred_mat = np.array([[0, 0], [0, 1]])

            game = XORGame(prob_mat, pred_mat)
            game.quantum_value()

    def test_zero_prob_mat(self):
        """Tests for zero probability matrix."""
        with self.assertRaises(ValueError):
            prob_mat = np.array([[1 / 4, 0], [1 / 4, 0]])
            pred_mat = np.array([[0, 0], [0, 1]])

            game = XORGame(prob_mat, pred_mat)
            game.quantum_value()

    def test_chsh_game_nonsignaling_value(self):
        """Non-signaling value for the CHSH game."""
        prob_mat = 1 / 4 * np.ones((2, 2))
        pred_mat = np.array([[0, 0], [0, 1]])

        chsh = XORGame(prob_mat, pred_mat)
        self.assertEqual(np.isclose(chsh.nonsignaling_value(), 1), True)

    def test_chsh_game_nonsignaling_value_rep_2(self):
        """Non-signaling value for the CHSH game for 2 reps."""
        prob_mat = 1 / 4 * np.ones((2, 2))
        pred_mat = np.array([[0, 0], [0, 1]])

        chsh_2_rep = XORGame(prob_mat, pred_mat, reps=2)
        self.assertEqual(np.isclose(chsh_2_rep.nonsignaling_value(), 1), True)

    def test_to_nonlocal_game(self):
        """XOR game to nonlocal game conversion."""
        prob = 1 / 4 * np.ones((2, 2))
        pred = np.array([[0, 0], [0, 1]])

        xor_chsh = XORGame(pred, prob, reps=1)
        nlg_chsh = xor_chsh.to_nonlocal_game()

        self.assertEqual(xor_chsh.classical_value(), nlg_chsh.classical_value())
