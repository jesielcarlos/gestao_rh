from django.db.models.query import QuerySet
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Funcionario
from django.contrib.auth.models import User



class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome','departamentos']

    def form_valid(self, form):
        
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username=funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.user = User.objects.create(username=username)   
        funcionario.save()

        return super(FuncionarioNovo, self).form_valid(form)    
