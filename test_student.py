import unittest
from main import Student


class TestStudent(unittest.TestCase):

    def test_walk_distance(self):
        student = Student('Dima')
        for _ in range(10):
            student.walk()
        self.assertEqual(student.get_distance(), 500, f"Дистанции не равны {student.get_distance()} != 500")

    def test_run_distance(self):
        student = Student('Dima')
        for _ in range(10):
            student.run()
        self.assertEqual(student.get_distance(), 1000, f"Дистанции не равны {student.get_distance()} != 1000")

    def test_race_results(self):
        runner = Student('Dima')
        walker = Student('Dima')
        for _ in range(10):
            runner.run()
            walker.walk()
        self.assertGreater(runner.get_distance(), walker.get_distance(),
                           f"{runner} должен преодолеть дистанцию больше, чем {walker}")


if __name__ == '__main__':
    unittest.main()
