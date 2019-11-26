from django.shortcuts import render
from django.http import HttpResponse 
from study.models import Teacher
from study.models import Student


# def index(request):
# 	teachers=Teacher.objects.exclude()
# 	return render(request,'study/index.html'),{
# 		'teachers' : teachers,

# 	}
def index(request):
	students= Student.objects.all()
	return render(request,'study/index.html',{'students' : students,})
	# return render(request,'study/index.html')

def detail_teacher(request):
		return render(request,'study/detail.html')



