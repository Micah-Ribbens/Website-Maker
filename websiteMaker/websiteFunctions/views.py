from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from websiteFunctions.forms import FunctionForm
from datetime import datetime
from websiteFunctions.models import Function

class create_view(TemplateView):
    template_name = 'create.html'
    def get(self, request):
        form = FunctionForm()
        all_functions = Function.objects.all()
        for function in all_functions:
            Function.delete(function)
        
        args = {'form': form, "hi": "hello coma esta"}
        return render(request, self.template_name, args)
    
    def post(self, request):
        form = FunctionForm(request.POST)
        args = {}
        if form.is_valid():
            command = form.cleaned_data['command']
            args = {'form': form, 'command': command}

            form.save()

     
        return redirect('/code', args)
        return render(request, 'code.html', args)
            
class code_response(TemplateView):
    template_name = "code.html"
    def get(self, request, *args):
        all_functions = Function.objects.all()
        last_command = all_functions[len(all_functions) - 1].command

        args = {
            "command": last_command,
        }
        print(args)
        return render(request, self.template_name, args)
        
def makeErrorReadable(error):
    legibleError = ""
    unimportantCh = ["[", "]","''"]
    for ch in error:
        if not ch == unimportantCh.__contains__(ch):
            legibleError += ch
    return legibleError


def hasDuplicate(note):
    allNotes = notes.objects.all()
    for a in allNotes:
        if a.description == note:
            return True

    return False
