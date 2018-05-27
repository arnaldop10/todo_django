from django.template.response import TemplateResponse
from django.views.generic import View
from django.http import HttpResponseRedirect

# Create your views here.
from todo.models import Todo

class TodoListView(View):
	def get(self, request, *args, **kwargs):
		context = {
			'todo_list': Todo.objects.all()
		}
		return TemplateResponse(request, 'todo_list.html', context)


class TodoAddView(View):
	def get(self, request, *args, **kwargs):
		return TemplateResponse(request, 'todo_add.html', {})

	def post(self, request, *args, **kwargs):
		description = request.POST['description']
		Todo.objects.create(description=description)
		return HttpResponseRedirect('/')


class TodoDoneView(View):
	def get(self, request, *args, **kwargs):
		todo = Todo.objects.get(id=kwargs['todo_id'])
		todo.is_done = True
		todo.save()
		return HttpResponseRedirect('/')