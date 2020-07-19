from django.shortcuts import render
from .models import feddback_model
from .forms import feedback_form
import datetime as dt

date1=dt.datetime.now()

# Create your views here.
def FeedBack_Page(request):
    if request.method=="POST":
        f_form=feedback_form(request.POST)
        if f_form.is_valid():
            name=request.POST.get("name")
            rateing=request.POST.get("rateing")
            feedback=request.POST.get("feedback")

            data=feddback_model(
                name=name,
                date=date1,
                rateing=rateing,
                feedback=feedback,
            )
            data.save()
            f_form=feedback_form()
            feedbacks = feddback_model.objects.all()
            context={"f_form":f_form,"feedbacks":feedbacks}
            return render(request,"feedback.html",context)

    else:
        f_form=feedback_form()
        feedbacks=feddback_model.objects.all()
        contect={"f_form":f_form,"feedbacks":feedbacks}
        return render(request,"feedback.html",contect)