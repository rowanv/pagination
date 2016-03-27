import unittest
from pagination_link_finder import pagination_link_finder as pl

class PaginationLinkFinderTest(unittest.TestCase):

    def test_similarity_matrix_yields_result(self):
        similarity_matrix = [[ 0, 14, 15, 15],
                            [14,  0, 24, 24],
                            [15, 24, 0,  1],
                            [15, 24,  1,  0]]
        label_prop_model = pl.SimilarityMatrixLabelSpreading(
            similarity_matrix=similarity_matrix)
        laplacian = label_prop_model._build_graph()
        self.assertEqual(laplacian, '')

class LevenshteinDistanceTest(unittest.TestCase):

    def test_levenshtein_produces_expected_result(self):

        dist = pl._levenshtein_distance('kitten', 'sitting')
        self.assertEqual(dist, 3)

        dist = pl._levenshtein_distance('book', 'back')
        self.assertEqual(dist, 2)

        dist = pl._levenshtein_distance(
            'https://news.ycombinator.com/from?site=martinfowler.com',
            'https://news.ycombinator.com/from?site=eff.org')
        self.assertEqual(dist, 14)

        dist = pl._levenshtein_distance('https://news.ycombinator.com/news?p=2',
            'https://news.ycombinator.com/news?p=3')
        self.assertEqual(dist, 1)


if __name__ == '__main__':
    unittest.main()