from django.shortcuts import render
import random

def home(request):
    return render(request, 'mateapp/home.html')

def result(request):
    
    list = {'황서경', '강연우', '강윤서', '김서영', '김소은', '김유진', '노은성', '문다연',
    '박경나', '박도윤', '박혜준', '송주연', '안현주', '오예림', '유수화', '윤정인', '이민정',
    '이연수', '장한빛', '전수현', '김정운', '조원아', '최진영'}
    names = random.sample(list, 1)
    return render(request, 'mateapp/result.html', {'names':names})

# Create your views here.
