class Grades(object):
    def __init__(self):
        """
        空の成績ブックを生成する
        """
        self.students = []
        self.grades = {}
        self.inSorted = True

    def addSutudent(self, student):
        """
        studentをStudent型とする
        studentを成績ブックへ追加する
        """
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(Student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self,student,grade):
        """
        gradeをfloat型とする
        gradeをstudentの成績リストへ追加する
        """
        try:
            self.grades[student.getNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getStudent(self):
        """
        成績ブックに収められた学生の、ソートされたリストを返す
        """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] # 学生リストのコピーを返す

def getStudents(self):
    """
    成績ブックに収められた学生のリストを
    アルファベット順に一度に1要素づつ返す
    """
    if not self.isSorted:
        self.students.sort()
        self.isSorted = True
    for s in self.students:
        yield s
