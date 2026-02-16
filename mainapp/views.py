
from django.http import HttpResponse
from django.shortcuts import render

def index (request):
   return render (request, 'mainapp/index.html')
def ex2(request):
    
    s = '''<h2>Navigation Bar<br></h2>
            <a href="https://www.youtube.com/watch?v=5BDgKJFZM18
    &list=PLu@W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br>

                    <a href="https://www.facebook.com/">Facebook</a><br>
                    <a href="https://www.flipkart.com/">Flipkart</a><br>
                    <a href="https://www.hindustantimes.com">News</a><br>
                    <a href="https://www.google.com/">Google</a>'''

    return HttpResponse(s)

def analyze(request):
    djtext = request.POST.get('text', 'default')
    
    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # check which checkbox is on
    if removepunc =="on":
        punctuations= '''!()-[]{};",:'\/,?@#$~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed+char
        
        params = {
            'purpose': 'removed punctuations',
            'analyzed_text': analyzed
        }
        djtext=analyzed
    # change to uppercase_________________
    
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+ char.upper()
        
        params = {
            'purpose': 'change to uppercase',
            'analyzed_text': analyzed
        }

        return render(request, 'mainapp/analyze.html', params)
        djtext=analyzed
    
    
    # this code extra remover______________
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
    # this code is newlineremover________________
      
    if(newlineremover=="on"):
          analyzed=""
          for char in djtext:
              if char!="\n" and char!="\r":
                  
               analyzed=analyzed+ char
             
        
          params = {
            'purpose': ' newlineremover',
            'analyzed_text': analyzed
        }
    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
    
        return HttpResponse("plz select the operation")
     
     
    return render(request, 'mainapp/analyze.html', params)