class Course:
    def __init__(self, t, m):
        self.__CourseTitle = t
        self.__MaxStudents = m
        self.__NumberOfLessons = 00
        self.__CourseLesson = ""
        self.__CAssessment = ""

    def GetCourseTitle(self):
        return self.__CourseTitle
    
    def GetMaxStudents(self):
        return self.__MaxStudents
    
    def GetNumberOfLessons(self):
        return self.__NumberOfLessons
    
    def GetCourseLesson(self):
        return self.__CourseLesson
    
    def GetCAssessment(self):
        return self.__CAssessment
    

    
    def AddLesson(self, lesson):
        if self.__NumberOfLessons < 50:
            self.__NumberOfLessons = self.__NumberOfLessons + 1
            self.__CourseLesson[self.__NumberOfLessons] = lesson
        else:
            print("Can not add more than 50 lessons")

    def AddAssessment(self):
        self.AddAssessment = input("Please enter your assessment marks")
    
    def OutputCourseDetails(self):
        print("Course:" + self.__CourseTitle)
        print("Max Students:" + self.__MaxStudents)
        print("Number of lessons:" + self.__NumberOfLessons)
        print("Progress:" + self.__CourseLesson)
        print("Assessment:" + self.__CAssessment)
        
class Lesson(Course):
    def __init__(self, lessontitle, durationminutes, requireslab):
        self.__LessonTitle = lessontitle
        self.__DurationMinutes = durationminutes
        self.__RequiresLab = requireslab
    def GetLessonTitle(self):
        return self.__LessonTitle
    
    def GetDurationMinutes(self):
        return self.__DurationMinutes
    
    def GetRequiresLab(self):
        return self.__RequiresLab

    def OutputLessonDetails(self):
        Course.OutputCourseDetails()
        print("Lesson title:" + self.__LessonTitle)
        print("Duration of lesson:" + str(self.__DurationMinutes))
        print("Lab required?:" + str('Yes' if self.__RequiresLab else 'No'))

class Assessment(Course):
    def __init__(self, t, m):
        self.AssessmentTitle = t
        self.MaxMarks = m
    def OutputAssessmentDetails(self):
        Courses.OutputCourseDetails()
        print("Assessment Title:" + self.AssessmentTitle)
        print("Max marks:" + str(self.MaxMarks))

course1 = Course("Object Oriented Programming", 35)
lesson1 = Lesson("Introduction to OOP", 60, False)
lesson2 = Lesson("Inheritance and Polymorphism", 90, True)
final_assessment = Assessment("final Exam", 100)

course1.AddLesson(lesson1)
course1.AddLesson(lesson2)
course1.AddAssessment(final_assessment)

course1.OutputCourseDetails()

print(f"Course Title: {course1.GetCourseTitle()}")
print(f"Max Students: {course1.GetMaxStudents}")
print(f"Number of Lessons: {course1.GetNumberOfLessons}")

for lesson_num, lesson in course1.GetCourseLesson().items():
    print(f"\nLesson {lesson_num} --> Title: {lesson.GetLessonTitle()}")

    
