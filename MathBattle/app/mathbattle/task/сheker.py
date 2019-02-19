from .models import Task

class Checker():
    def __init__(self, task_id):
        self.task_id = task_id
        self.listOfNums = []

    def check(self,answer):
        Tasks = Task.objects.all()
        typytype = Tasks[self.task_id].type
        rans = Tasks[self.task_id].right_answer
        if typytype == 0:
            if (rans == answer):
                return "OK"
            else:
                return "WA"
        elif typytype == 1:
            for i in range(-1000, 1000):
                new_ans = answer
                new_ans = new_ans.replace('x', 'i')
                new_rans = rans
                new_rans = new_rans.replace('x', 'i')
                if (eval(new_ans) == eval(new_rans)):
                    return "OK"
                else:
                    return "WA"
        elif typytype == 2:
            for i in range(-100, 100):
                for j in range(-100, 100):
                    new_ans = answer
                    new_ans = new_ans.replace('x', 'i')
                    new_ans = new_ans.replace('y', 'j')
                    new_rans = rans
                    new_rans = new_rans.replace('x', 'i')
                    new_rans = new_rans.replace('y', 'j')
                    print(new_rans, new_ans)
                    if (eval(new_ans) == eval(new_rans)):
                        return "OK"
                    else:
                        return "WA"
        elif typytype == 3:
            for i in range(-10, 10):
                for j in range(-10, 10):
                    for ii in range(-10, 10):
                        new_ans = answer
                        new_ans = new_ans.replace('x', 'i')
                        new_ans = new_ans.replace('y', 'j')
                        new_ans = new_ans.replace('z', 'ii')
                        new_rans = rans
                        new_rans = new_rans.replace('x', 'i')
                        new_rans = new_rans.replace('y', 'j')
                        new_rans = new_rans.replace('z', 'ii')

                        if (eval(new_ans) == eval(new_rans)):
                            return "OK"
                        else:
                            return "WA"
        else:
            return "CF"
