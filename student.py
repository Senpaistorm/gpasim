import Course.py
'''
A class that represents a student with first name, last name, and courses
that the student is taking.
'''
class Student():
    
    def __init__(self, first, last):
        ''' Initialize a student with the first name first and last name last.
        As well as an empty course list.
        first, last -> str
        '''
        self.first = first
        self.last = last
        self.courses = []
        
    def getFirst():
        return self.first
    
    def getLast():
        return self.last
    
    def setFirst(first):
        self.first = first
    
    def setLast(last):
        self.last = last
        
    def add_course(self, course):
        ''' Add a course to a student.
        course -> Course
        '''
        self.courses.append(course)
    
    def del_course(self, code):    
        ''' Delete a course specified by the course code.
        code -> str
        '''

            
    
