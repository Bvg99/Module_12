import unittest
from main import Student

class TestStudent(unittest.TestCase):
    def test_walk_10_times(self):
        student = Student("Коля")
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 50, f"Дистанции не равны {student.distance} != 50")

    def test_run_10_times(self):
        student = Student("Вася")
        for _ in range(10):
            student.run()
        self.assertEqual(student.distance, 100, f"Дистанции не равны {student.distance} != 100")

    def test_running_vs_walking(self):
        runner = Student("Катя")
        walker = Student("Лена")

        for _ in range(10):
            runner.run()
            walker.walk()

        self.assertGreater(runner.distance, walker.distance, f"{runner.name} должен преодолеть дистанцию больше, чем {walker.name}")

if __name__ == "__main__":
    unittest.main()