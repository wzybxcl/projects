class Courses:
    def __init__(self, t, m, n, l, a):
        self.CourseTitle = t
        self.MaxStudents = m
        self.NumberOfLessons = n
        self.CourseLesson = l
        self.CAssessment = a
    
    def AddLesson(self):
        self.CourseLesson = self.CourseLesson + 1

    def AddAssessment(self):
        self.AddAssessment = input("Please enter your assessment marks")
    
    def OutputCourseDetails(self):
        print("Course:" + self.CourseTitle)
        print("Max Students:" + self.MaxStudents)
        print("Number of lessons:" + self.NumberOfLessons)
        print("Progress:" + self.CourseLesson)
        print("Assessment:" + self.CAssessment)

class Lesson(Courses):
    def __init__(self, t, m, n, l, a):
        Courses.__init__(self, t, m, n, l, a)
        self.LessonTitle = ""
        self.DurationMinutes = 60
        self.RequiresLab = False

    def OutputLessonDetails(self):
        Courses.OutputCourseDetails()
        print("Lesson title:" + self.LessonTitle)
        print("Duration of lesson:" + str(self.DurationMinutes))
        print("Lab required?:" + str(self.RequiresLab))

class Assessment(Courses):
    def __init__(self, t, m, n, l, a):
        Courses.__init__(self, t, m, n, l, a)
        self.AssessmentTitle = ""
        self.MaxMarks = 00
    def OutputAssessmentDetails(self):
        Courses.OutputCourseDetails()
        print("Assessment Title:" + self.AssessmentTitle)
        print("Max marks:" + self.MaxMarks)

