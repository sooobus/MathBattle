from .models import Task

class Checker():
    def __init__(self, task_id):
        self.task_id = task_id
        self.task_id = task_id
        self.listOfNums = []

    def check(self, answer):
        try:
            Tasks = Task.objects.all()
            typytype = Tasks[self.task_id].type
            rans = Tasks[self.task_id].right_answer
            from sympy import simplify, cos, sin, expand, symbols, init_printing
            x, y, z = symbols('x y z')
            init_printing(use_unicode=True)
            eval_str = 'simplify(({})-({}))'.format(rans, answer)
            if (eval(eval_str) == 0):
                return "OK"
            else:
                return "WA"
        except Exception as e:
            print(e)
            return "CF"