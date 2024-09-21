from django.db import models
Class Task(models.Models):
title = models.CharField(max_length=100)
description = models.TextField()
comleted = models.BoolenField(default=False)
created = model.DataTimeField(auto_now_add=True)
 def __str__(self):
     return self.title