import Student.py
'''
A class that represents a course specified with a course code.
'''
class Course():
    
    def __init__(self, code):
        ''' Initialize a new course specified by the course code.
        code -> str
        '''
        self.code = code
        
        
    
    def __str__(self):
        ''' Returns the course code of a course.
        return -> str
        '''
        return self.code