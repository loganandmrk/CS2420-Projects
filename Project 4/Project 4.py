from slist import SList
from course import Course

def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.grade() * course.credit_hr()
        credits += course.credit_hr()
    if credits == 0:
        return 0
    return round(sumGrades / credits, 2)

def is_sorted(lyst):
    for i in range(0, lyst.size()  - 1):
        if lyst[i] > lyst[i + 1]:
            return False
    return True

def main():
    course_list = SList()
    try:
        course_list.insert(Course(1010, "Intro to Programming", 3, 3.5))
        course_list.insert(Course(2050, "Data Structures", 4, 3.7))
        course_list.insert(Course(1500, "Computer Science I", 3, 3.2))
        course_list.insert(Course(3000, "Algorithms", 3, 3.8))
        course_list.insert(Course(2500, "Computer Architecture", 4, 3.0))
    except (ValueError, TypeError) as error:
        print(f"Error inserting course: {error}")
        return

    print(course_list[0])
    print(course_list)
    print(calculate_gpa(course_list))
    print(is_sorted(course_list))
    print(course_list.size())
  
if __name__ == "__main__":
    main()
