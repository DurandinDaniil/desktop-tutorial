from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Review
from .forms import UserForm

from .apps import ML

 
# получение данных из бд
def index(request):
    userform = UserForm()
    review = Review.objects.all()
    return render(request, "index.html", { "userform": userform, "review": review})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        comment = Review()
        comment.text = request.POST.get("text")
        alg = ML()
        text = alg.text_preprocessing(comment.text)
        text = alg.vectorizer.transform([text])
        comment.length = alg.classificator.predict(text)
        comment.save()
    return HttpResponseRedirect("/")