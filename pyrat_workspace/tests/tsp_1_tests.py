#####################################################################################################################################################
######################################################################## INFO #######################################################################
#####################################################################################################################################################

"""
    This program contains all the unit tests for the functions developed in the program "tsp_1.py".
    Let's consider the following maze for our tests:
    #############################################################
    # (0)       # (1)      # (2)       ⵗ (3)       # (4)        #
    #           #          #           ⵗ           #            #
    #           #          #           ⵗ           #            #
    #⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅############⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅##########################
    # (5)       ⵗ (6)       ⵗ (7)       ⵘ (8)       ⵘ (9)       #
    #           ⵗ           ⵗ           6           9            #
    #           ⵗ           ⵗ           ⵘ           ⵘ           #
    #⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅#ⴾⴾⴾⴾⴾⴾ8ⴾⴾⴾⴾⴾⴾ############⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅#############
    # (10)      ⵗ (11)      # (12)      # (13)      # (14)      #
    #           ⵗ           #           #           #           #
    #           ⵗ           #           #           #           #
    #ⴾⴾⴾⴾⴾⴾ9ⴾⴾⴾⴾⴾⴾ#⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅#############ⴾⴾⴾⴾⴾⴾ6ⴾⴾⴾⴾⴾⴾ#⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅#
    # (15)      ⵘ (16)      ⵗ (17)      ⵘ (18)      ⵗ (19)      #
    #           4           ⵗ           5           ⵗ            #
    #           ⵘ           ⵗ           ⵘ           ⵗ           #
    #⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅#⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅#⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅#⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅#⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅#
    # (20)      # (21)      ⵗ (22)      # (23)      # (24)      #
    #           #           ⵗ           #           #           #
    #           #           ⵗ           #           #           #
    #############################################################
"""

#####################################################################################################################################################
###################################################################### IMPORTS ######################################################################
#####################################################################################################################################################

# Import PyRat
from pyrat import *

# External imports
import unittest
import numpy
import sys
import os

# Previously developed functions
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "programs"))
from tsp_1 import *

#####################################################################################################################################################
############################################################### UNIT TESTS DEFINITION ###############################################################
#####################################################################################################################################################

class TestsTutorial (unittest.TestCase):

    """
        Here we choose to use the unittest module to perform unit tests.
        This module is very simple to use and allows to easily check if the code is working as expected.
    """

    #############################################################################################################################################
    #                                                                CONSTRUCTOR                                                                #
    #############################################################################################################################################

    def __init__ ( self:     Self,
                   *args:    Any,
                   **kwargs: Any,
                 ) ->        Self:

        """
            This function is the constructor of the class.
            In:
                * self:   Reference to the current object.
                * args:   Arguments of the parent constructor.
                * kwargs: Keyword arguments of the parent constructor.
            Out:
                * self: Reference to the current object.
        """

        # Inherit from parent class
        super(TestsTutorial, self).__init__(*args, **kwargs)

        # We need to store the width of the maze
        self.maze_width = 5

        # We define the graph structures that will be used for the tests
        self.graph_dictionary = {0: {5: 1},
                                 2: {3: 1, 7: 1},
                                 3: {2: 1},
                                 5: {0: 1, 6: 1, 10: 1},
                                 6: {5: 1, 7: 1, 11: 8},
                                 7: {2: 1, 3: 1, 6: 1, 8: 6},
                                 8: {7: 6, 9: 9, 13: 1},
                                 9: {8: 9},
                                 10: {5: 1, 11: 1, 15: 9},
                                 11: {6: 8, 10: 1, 16: 1},
                                 13: {8: 1, 18: 6},
                                 14: {19: 1},
                                 15: {10: 9, 16: 4, 20: 1},
                                 16: {11: 1, 15: 4, 17: 1, 21: 1},
                                 17: {16: 1, 18: 5, 22: 1},
                                 18: {13: 6, 17: 5, 19: 1, 23: 1},
                                 19: {14: 1, 18: 1, 24: 1},
                                 20: {15: 1},
                                 21: {16: 1, 22: 1},
                                 22: {17: 1, 21: 1},
                                 23: {18: 1},
                                 24: {19: 1}}
        
        # Here is the same graph represented as an adjacency matrix
        self.graph_matrix = numpy.array([[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 1, 0, 0, 0, 1, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 6, 0, 9, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 4, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 5, 0, 0, 0, 1, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 5, 0, 1, 0, 0, 0, 1, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]])

        self.vertices = [0, 2, 5, 7]
        
    #############################################################################################################################################
    #                                                               PUBLIC METHODS                                                              #
    #############################################################################################################################################

    def test_graph_to_metagraph(self):
        """Test the graph_to_metagraph function."""
        complete_graph, routing_tables = graph_to_metagraph(self.graph_dictionary, self.vertices)
        
        # Here, you need to assert that the `complete_graph` and `routing_tables` are what you expect them to be
        # for the given input.
        expected_complete_graph = numpy.array([
            [0, float('inf'), 1, float('inf')],
            [float('inf'), 0, float('inf'), 1],
            [1, float('inf'), 0, 2],
            [float('inf'), 1, 2, 0]
        ])  # This is a placeholder; you should replace it with the expected result.

        expected_routing_tables = {
            0: {2: None, 5: 5, 7: None},
            2: {0: None, 5: 7, 7: 7},
            5: {0: 0, 2: 7, 7: 6},
            7: {0: None, 2: 2, 5: 6}
        }  # This is a placeholder; replace with the expected routing table for each vertex.
        
        numpy.testing.assert_array_equal(complete_graph, expected_complete_graph)
        self.assertEqual(routing_tables, expected_routing_tables)

    #############################################################################################################################################

    def test_tsp(self):
        """
        Unit test for the tsp function.
        """
        # Define test case inputs
        example_metagraph = {}  # replace with example metagraph
        
        # Call the function with the test inputs
        result_path = tsp(example_metagraph)
        
        # Define expected output
        expected_path = []  # replace with expected path
        
        # Check if the function’s output matches expected output
        self.assertEqual(result_path, expected_path)

    #############################################################################################################################################

    def test_expand_route(self):
        """
        Unit test for the expand_route function.
        """
        # Define test case inputs
        example_route = []  # replace with example route
        example_routing_tables = {}  # replace with example routing tables
        example_cell_names = {}  # replace with example cell names
        
        # Call the function with the test inputs
        result_expanded_route = expand_route(example_route, example_routing_tables, example_cell_names)
        
        # Define expected output
        expected_expanded_route = []  # replace with expected expanded route
        
        # Check if the function’s output matches expected output
        self.assertEqual(result_expanded_route, expected_expanded_route)


#####################################################################################################################################################
######################################################################## GO! ########################################################################
#####################################################################################################################################################

if __name__ == "__main__":

    # Run all unit tests
    unittest.main(verbosity=2)

#####################################################################################################################################################
#####################################################################################################################################################
