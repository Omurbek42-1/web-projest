from  rest_framework import  serializers
from  .models import  Task

class
    TaskSerializers(serializers.ModelSerializers):
    class Meta:
        model = Task
        fields = '__all__'