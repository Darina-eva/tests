import unittest
from votes import vote
from square_root import discriminant, solution
from assistant import get_name, get_directory, add


class TestVote(unittest.TestCase):
    def test_vote_cases(self):
        cases = [
            (['A', 'A', 'B'], 'A'),
            (['B', 'B', 'A'], 'B'),
            (['C', 'C', 'C'], 'C'),
            ([1, 2, 2, 3], 2),
        ]
        for votes, expected in cases:
            with self.subTest(votes=votes):
                self.assertEqual(vote(votes), expected)


class TestQuadratic(unittest.TestCase):
    def test_discriminant_cases(self):
        cases = [
            ((1, -3, 2), 1),
            ((1, 2, 1), 0),
            ((1, 0, 1), -4),
        ]
        for args, expected in cases:
            with self.subTest(args=args):
                self.assertEqual(discriminant(*args), expected)

    def test_solution_cases(self):
        cases = [
            ((1, -3, 2), (2.0, 1.0)),
            ((1, 2, 1), -1.0),
            ((1, 0, 1), None),
        ]
        for args, expected in cases:
            with self.subTest(args=args):
                result = solution(*args)
                if isinstance(expected, tuple):
                    self.assertAlmostEqual(result[0], expected[0])
                    self.assertAlmostEqual(result[1], expected[1])
                else:
                    self.assertEqual(result, expected)


class TestDocuments(unittest.TestCase):
    def test_get_name_cases(self):
        cases = [
            ('2207 876234', 'Василий Гупкин'),
            ('11-2', 'Геннадий Покемонов'),
            ('9999', 'Документ не найден'),
        ]
        for doc_number, expected in cases:
            with self.subTest(doc_number=doc_number):
                self.assertEqual(get_name(doc_number), expected)

    def test_get_directory_cases(self):
        cases = [
            ('11-2', '1'),
            ('10006', '2'),
            ('9999', 'Полки с таким документом не найдено'),
        ]
        for doc_number, expected in cases:
            with self.subTest(doc_number=doc_number):
                self.assertEqual(get_directory(doc_number), expected)

    def test_add_document(self):
        add('passport', '7777', 'Test User', 3)
        self.assertEqual(get_name('7777'), 'Test User')
        self.assertEqual(get_directory('7777'), '3')


if __name__ == '__main__':
    unittest.main()
