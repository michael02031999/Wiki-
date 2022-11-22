from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

from . import util
import random
import re

def markdownToHTML(entry):
    if entry == None:
        return entry
    list_withLineBreaks = entry.splitlines()

    newList = []

    for element in list_withLineBreaks:
        
        if "#####" in element:
            element = element.replace("#####", "</h5>")
            element += " </h5>"
        
        if "####" in element:
            element = element.replace("####", "</h4>")
            element += " </h4>"
         
        if "###" in element:
            element = element.replace("###", "</h3>")
            element += " </h3>"
      
        if "##" in element:
            element = element.replace("##", "<h2>")
            element += " </h2>"
      
        if "#" in element:
            element = element.replace("# ", "<h1>")
            element += " </h1>"
        
        if "**" in element:
            element = element.replace("**", "<strong>")
            element += "</strong>"
        
        if "*" in element:
            element = element.replace("*", "<li>")
            element += "</li>"
        if "[" in element:
            result = element[element.find('(')+1:element.find(')')]
            aTag = "<a href ='"+result+"'>"
            element = element.replace("[", aTag)
        if "]" in element: 
            element = element.replace("]", "</a>")
        
        element = "<p>" + element
        element = element + "</p>"

        newList.append(element)
        
    newList = "\n".join(newList)    
    
    return newList


def random_page(request):

    entriesList = util.list_entries()

    entryNum = random.randint(0, len(entriesList)-1)

    return render(request, "encyclopedia/entry.html", {
        "entry": markdownToHTML(util.get_entry(entriesList[entryNum]))
    })
     

def edit_markdown(request):
    if request.method == "POST":
        textarea = request.POST.get("textarea")
        title = request.POST.get("title")

        #def save_entry(title, content):
        #print(textarea)
        #print(title)

        util.save_entry(title, textarea)

        return HttpResponseRedirect(title)
        #return entry(request, title)

        #return render(request, "encyclopedia/entry.html", {
                    #"entry": markdownToHTML(util.get_entry(title))
                #})

       
        
       

    #path = request.POST["path"]
    #path = request.POST.get("path", False)
    path = request.GET.get('path')
    
    splitURL = path.split("/")

    title = splitURL[len(splitURL)-1]

    print(title)

    return render(request, "encyclopedia/edit_markdown.html", {
                "entry": util.get_entry(title),
                "title": title
            })


    
def create_new_page(request):
    if request.method == "POST":
        print(request.POST["title"])
        print("hello")
        title = request.POST["title"]
        textarea = request.POST["textarea"]

        print(util.get_entry(title))

        if util.get_entrsy(title) == None:

            #def save_entry(title, content):

            util.save_entry(title, textarea)
            return render(request, "encyclopedia/entry.html", {
                    "entry": markdownToHTML(util.get_entry(title))
                })

        else: 
            print("this is working")
            return render(request, "encyclopedia/create_new_page.html", {
                "Warning": "There is already a file with this name!"
            })


    return render(request, "encyclopedia/create_new_page.html") 



def index(request):
    if request.method == "POST":

        substringEntries = []

        query = request.POST["q"]

        entries = util.list_entries()

        for entry in entries:
            if entry.capitalize() == query.capitalize():
                return render(request, "encyclopedia/entry.html", {
                    "entry": markdownToHTML(util.get_entry(entry))
                })

            elif query.upper() in entry.upper():
                substringEntries.append(entry)

        return render(request, "encyclopedia/search_results.html", {
            "substringEntries": substringEntries
        })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):

    if util.get_entry(entry) == None:
        return render(request, "encyclopedia/error.html")

    return render(request, "encyclopedia/entry.html", {
        "entry": markdownToHTML(util.get_entry(entry))
    })


    #return render(request, "encyclopedia/create_new_page.html")

