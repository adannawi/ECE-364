import re


class Course:

    def __init__(self, courseID, fst, snd, final):
        self.courseID = courseID
        self.fst = fst
        self.snd = snd
        self.final = final
        self.total = 0.25 * fst + 0.25 * snd + 0.50 * final
        self.letter = self.getLetterGrade()

    def __str__(self):
        return "{0}: ({1:.2f}, {2:.2f}, {3:.2f}) = ({4:.2f}, {5})".format(self.courseID, self.fst, self.snd,
                                                                          self.final, self.total, self.letter)

    def getLetterGrade(self):
        if self.total >= 90:
            return "A"
        elif 80 <= self.total < 90:
            return "B"
        elif 70 <= self.total < 80:
            return "C"
        elif 60 <= self.total < 70:
            return "D"
        else:
            return "F"


class Student:

    def __init__(self, name):
        self.name = name
        self.courses = {}

    def __str__(self):

        courseList = sorted("({0}: {1})".format(c.courseID, c.letter) for c in self.courses.values())
        return "{0}: {1}".format(self.name, ", ".join(courseList))

    def addCourse(self, course):
        self.courses[course.courseID] = course

    def generateTranscript(self):

        courseList = sorted("{}: ({:.2f}, {:.2f}, {:.2f}) = ({:.2f}, {})".format(c.courseID, c.fst, c.snd,
                                                                                 c.final, c.total, c.letter)
                            for c in self.courses.values())

        return "{}\n{}".format(self.name, "\n".join(courseList))


class School:

    def __init__(self, name):
        self.name = name
        self.students = dict()

    def __str__(self):
        uniString = ""
        studentList = []
        for student in self.students.values():
            studentList.append(student.name)
        studentList.sort()
        uniString += "{0}: {1} students \n".format(self.name, len(studentList))
        for person in studentList:
            uniString += "{}\n".format(person)
        return uniString

    def loadStudentsInfo(self, filename):
        with open(filename) as studentFile:
            lineString = studentFile.read()

        studentList = lineString.split("\n\n")

        for student in studentList:
            lines = student.split("\n")
            newStudent = Student(lines[0])

            for course in lines[2:]:
                courseRe = re.search("(\w*): (\w*), (\w*), (\w*)", course)
                newCourse = Course(courseRe.group(1), float(courseRe.group(2)),
                                   float(courseRe.group(3)), float(courseRe.group(4)))
                newStudent.addCourse(newCourse)
            self.students[newStudent.name] = newStudent

    def saveSchoolInfo(self, filename):
        studentList = sorted(s.generateTranscript() for s in self.students.values())
        output = "\n\n".join(studentList)

        with open(filename, 'w') as saveFile:
            saveFile.write(output)

if __name__ == "__main__":
    course301 = Course("ECE 301", 100, 80.5, 0)
    course302 = Course("ECE 302", 80, 70, 85)
    upCourse301 = Course("ECE 301",80, 90, 100)
    course201 = Course("ECE 201", 50, 100, 100)
    course202 = Course("ECE 202", 80, 90, 100)
    course274 = Course("ECE 274", 99.00, 72.00, 74.00)
    course377 = Course("ECE 377", 64.00, 86.00, 79.00)
    course474 = Course("ECE 474", 96.00, 90.00, 67.00)
    course678 = Course("ECE 678", 89.00, 86.00, 79.00)
    #ECE274: (99.00, 72.00, 74.00) = (79.75, C)
    #ECE377: (64.00, 86.00, 79.00) = (77.00, C)
    #ECE474: (96.00, 90.00, 67.00) = (80.00, B)
    #ECE678: (89.00, 86.00, 79.00) = (83.25, B)
    Merp = Student("Barack Obama")
    Mike = Student("Michael Jackson")
    Bush = Student("George Bush")
    Merp.addCourse(course274)
    Merp.addCourse(course377)
    Merp.addCourse(course474)
    Merp.addCourse(course678)
    Mike.addCourse(course301)
    Bush.addCourse(course302)
    purdueUni = School("Purdue University")
    students = dict()
    students["Barack Obama"] = Merp
    students["Michael Jackson"] = Mike
    students["George Bush"] = Bush
    purdueUni.loadStudentsInfo("school_data_source.txt")
    purdueUni.saveSchoolInfo("save_confirm.txt")
    #print(purdueUni.__str__())
    #print(Merp.generateTranscript())
