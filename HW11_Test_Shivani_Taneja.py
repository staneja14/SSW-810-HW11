import unittest
from HW11_Shivani_Taneja import Instructors
from HW11_Shivani_Taneja import Students
from HW11_Shivanni_Taneja import Major

class StudentTest(unittest.TestCase):
    def test__init__(self):
        Student_1 = Student('123', 'Jose', 'SFEN')
        self.assertEqual(Student('123', 'Jose', 'SFEN').name, Student_1.name, True)


class InstructorTest(unittest.TestCase):
    def test_init__(self):
        inst = Instructor('3321', 'James Rowland', 'SFEN')
        self.assertNotEqual(Student('123', 'Jose', 'SFEN').name, inst.name, True)


class MajorTest(unittest.TestCase):
    def test_init__(self):
        major = Major('SSW 540', 'R', 'SFEN')
        self.assertNotEqual(Major('SSW 540', 'E', 'SFEN').name, inst.name, True)


class DBTest(unittest.TestCase):
    def instructor_table_DB(self):
        stevens = Repository('Stevens')

    students_info = {
        '10103': ['10103', 'Baldwin, C', 'SFEN', {'SSW 567': 'A', 'SSW 564': 'A-', 'SSW 687': 'B', 'CS 501': 'B'}],
        '10115': ['10115', 'Wyatt, X', 'SFEN', {'SSW 567': 'A', 'SSW 564': 'B+', 'SSW 687': 'A', 'CS 545': 'A'}],
        '10172': ['10172', 'Forbes, I', 'SFEN', {'SSW 555': 'A', 'SSW 567': 'A-'}],
        '10175': ['10175', 'Erickson, D', 'SFEN', {'SSW 567': 'A', 'SSW 564': 'A', 'SSW 687': 'B-'}],
        '10183': ['10183', 'Chapman, O', 'SFEN', {'SSW 689': 'A'}],
        '11399': ['11399', 'Cordova, I', 'SYEN', {'SSW 540': 'B'}],
        '11461': ['11461', 'Wright, U', 'SYEN', {'SYS 800': 'A', 'SYS 750': 'A-', 'SYS 611': 'A'}],
        '11658': ['11658', 'Kelly, P', 'SYEN', {'SSW 540': 'F'}],
        '11714': ['11714', 'Morton, A', 'SYEN', {'SYS 611': 'A', 'SYS 645': 'C'}],
        '11788': ['11788', 'Fuller, E', 'SYEN', {'SSW 540': 'A'}]}

    instructors_info = {'98765': ['98765', 'Einstein, A', 'SFEN', {'SSW 567': 4, 'SSW 540': 3}],
                        '98764': ['98764', 'Feynman, R', 'SFEN',
                                  {'SSW 564': 3, 'SSW 687': 3, 'CS 501': 1, 'CS 545': 1}],
                        '98763': ['98763', 'Newton, I', 'SFEN', {'SSW 555': 1, 'SSW 689': 1}],
                        '98762': ['98762', 'Hawking, S', 'SYEN', {}],
                        '98761': ['98761', 'Edison, A', 'SYEN', {}],
                        '98760': ['98760', 'Darwin, C', 'SYEN',
                                  {'SYS 800': 1, 'SYS 750': 1, 'SYS 611': 2, 'SYS 645': 1}]}

    majors_info = {'SFEN': ['SFEN', ('SSW 555', 'SSW 564', 'SSW 567', 'SSW 540'), ('CS 513', 'CS 545', 'CS 501')],
                   'SYEN': ['SYEN', ('SYS 800', 'SYS 612', 'SYS 671'), ('SSW 565', 'SSW 810', 'SSW 540')]}

    students_dic = dict()
    for CWID, person in stevens.students.items():
        students_dic[CWID] = person.get_whole_info()

    instructors_dic = dict()
    for CWID, person in stevens.instructors.items():
        instructors_dic[CWID] = person.get_whole_info()

    majors_dic = dict()
    for major, major_info in stevens.majors.items():
        majors_dic[major] = major_info.get_whole_info()

    self.assertEqual(students_dic, students_info)
    self.assertEqual(instructors_dic, instructors_info)

    for item, major in majors_dic.items():
        self.assertEqual(major[0], majors_info[item][0])
        self.assertTrue(major[1], majors_info[item][1])
        self.assertTrue(major[2], majors_info[item][2])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
