class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0  # Counts consecutive students who couldn't eat

        while students and count < len(students):

            student = students.pop(0)
            sandwich = sandwiches[0]  # Top of the stack

            if student == sandwich:
                sandwiches.pop(0)
                count = 0  # Reset because a student ate
            else:
                students.append(student)
                count += 1

        return len(students)
        