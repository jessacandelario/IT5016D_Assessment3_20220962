
class Problem:

    def __init__(self, problem):
        self.problem = problem

    def password_change(self, user_id, username):
        """Create the new password"""
        first_digit = user_id[0]
        second_digit = user_id[1]
        third_digit = username[0]
        fourth_digit = username[1]
        fifth_digit = username[2]
        new_password = first_digit + second_digit + third_digit + fourth_digit + fifth_digit
        return new_password

    def problem_input(self):
        return self.problem
