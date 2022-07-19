from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
class problem(models.Model):
    name=models.TextField()
    statement = models.TextField()
    input_format=models.TextField(default=" ")
    difficulty=models.TextField()
    def __str__(self):
        return self.name


class solution(models.Model):
    curr_problem=models.ForeignKey(problem, on_delete=models.CASCADE, null=True)
    verdict=models.TextField(null=True)
    time_of_submit = models.DateTimeField(auto_now=True)
    code=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.curr_problem.name
     

class testcase(models.Model):
    curr_problem=models.ForeignKey(problem, on_delete=models.CASCADE,null=True)
    input=models.TextField()
    output=models.TextField()
    def __str__(self):
        return self.curr_problem.name

    
 
