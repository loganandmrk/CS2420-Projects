class Course:
    ''' Course object '''
    def __init__(self, course_num = 0, course_name = "", credit_hours = 0.0, grade = 0.0):

        if not isinstance(course_num, int):
            raise ValueError("Course number must be an integer")
        elif course_num < 0:
            raise TypeError("Course number must be non-negative")
        else:
            self._course_num = course_num
        
        self._course_name = str(course_name)
        
        if not isinstance(credit_hours, (int, float)):
            raise TypeError("Credit hours must be a number")
        elif credit_hours < 0:
            raise ValueError("Credit hours must be non-negative")
        else:
            self._credit_hours = credit_hours
        
        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be a number")
        elif grade < 0.0 or grade > 4.0:
            raise ValueError("Grade must be between 0.0 and 4.0")
        else:
            self._grade = grade

    def number(self):
        return int(self._course_num)
    
    def name(self):
        return str(self._course_name)
    
    def credit_hr(self):
        return float(self._credit_hours)
    
    def grade(self):
        return float(self._grade)

    def __eq__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() == cnumb
    def __ne__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() != cnumb

    def __lt__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() < cnumb
    
    def __gt__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() > cnumb
    
    def __le__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() <= cnumb
    
    def __ge__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() >= cnumb
    
    def __str__(self):
        return f"cs{self.number()} {self.name()} Grade: {self.grade()} Credit Hours: {self.credit_hr()}"