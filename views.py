from django.shortcuts import render
def my_view (request):
  return render(request,"app/display1.html")    ---# this will render to the display.html file in template
