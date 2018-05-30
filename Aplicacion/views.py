from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from Aplicacion.forms import SignUpForm, Hospital_form, Sector_form, Estado_form
#Prueva view dinamic
from django.views.generic import ListView,DetailView,TemplateView,CreateView,UpdateView
from django.views.generic.edit import FormView
from Aplicacion.models import Hospital,Usuario
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class Perfil_View(TemplateView):
  template_name = 'perfil.html'

  def get_context_data(self, **kwargs):
    context = super(Perfil_View, self).get_context_data(**kwargs)
    user = User.objects.get(username=self.request.user.username)
    context['object_list'] = Usuario.objects.filter(user=user)
    return context

class Perfil_Update(UpdateView):
  model = Usuario
  fields = ['email','image','Direccion','TipodeSangre','Alergias']
  template_name = 'perfil_update.html'
  success_url = reverse_lazy('perfil_view')

def Hospital(request):
    args={}
    args.update(csrf(request))

    args['articles']=Hospital.objects.all()
    return render_to_response('Hospital.html',args)

def Sector(request):
     form=Sector_form(request.POST or None)
     if request.method=='POST':
        if form.is_valid():
            form.save()
            form = Sector_form()
     return render(request,'Sector.html',{'form':form,'titulo':'Sector'})

def Estado(request):
     form=Estado_form(request.POST or None)
     if request.method=='POST':
        if form.is_valid():
            form.save()
            form = Estado_form()
     return render(request,'Estado.html',{'form':form,'titulo':'Estado'})

@login_required
def home(request):
    return render(request, 'home.html')

def Perfil(request):
    return render(request, 'perfil.html')


def buscar(request):
    return render(request, 'buscar.html')




def Foro(request):
    return render(request, 'foro.html')

def Acerca(request):
    return render(request, 'acerca.html')


def contactos(request):
    return render(request, 'contactos.html')
def Nopermisos(request):
  return render(request, 'Nopermisos.html')

class SignUp(CreateView):
  template_name = 'signup.html'
  form_class = SignUpForm
  success_url = reverse_lazy('login')

  def form_valid(self, form):
    user = form.save()
    p = Usuario()
    p.user = user
    p.email = form.cleaned_data['email']
    p.image = form.cleaned_data['image']
    p.Direccion=form.cleaned_data['Direccion']
    #p.is_staff=True
    p.save()
    return super(SignUp, self).form_valid(form)

def prueba(request):
    return render(request, 'prueba.html')

def Ruta(request):
    return render(request, 'ruta.html')
def test(request):
    return render(request, 'test.html')


#Reporte
#1. Importar el modelo ej. 
from Aplicacion.models import Hospital,Ubicacion
#2. Crear lavista del reporte.html
def reporte_uno(request):
  return render(request, 'reporte.html', {'Hospital': Hospital.objects.all()})  

#Prueba dinamic view


class TodasPublicaciones(ListView):
    model=Hospital
    template_name='listapublicaciones.html'
    paginate_by=3
    
    def get_queryset(self):
        return Hospital.autorizados_objects.all().order_by('calificacion').reverse()


def ListaPublicacion(request,slug):
    try:
        pub_id=Hospital.autorizados_objects.filter(slug=slug)
        
    except Hospital.DoesNotExist:
        raise Http404("No existe ese Hospital")
    return render(
        request,
        'listapublicaciones.html',
        context={'object_list':pub_id,}
        )



#Prueba de buscador
#def busqueda(self):
 #  q = request.GET.get('q', '')

  # querys=(Hospital(Nombre_icontains=q)|Hospital(Sector_icontains=q))

   #Hospital = Hospital.objects.filter(querys)
   #return render(request, 'busqueda.html', {'Hospital': Hospital})

#Pruea 3
class BuscarView(TemplateView):

  def post(self,request,*args, **kwargs):
    buscar=request.POST['buscalo']
    Especialidad=Hospital.objects.filter(Especialidad__contains=buscar)    
    Hospitales=Hospital.objects.filter(Nombre__contains=buscar)
    if Hospitales:
      print ("Ha buscado un hospitalpor su nombre")
      return render(request,'busca.html',
        {'Hospitales':Hospitales, 'hospital':True})
    elif Especialidad:
      print ("Ha buscado un hospitalpor su especialidad")
      return render(request,'busca.html',
        {'Hospitales':Especialidad, 'hospital':True})
    else:
      print ("NO existe")
      return render(request, 'Noexiste.html')



#Prueba imagen 1.0
def list_hospital(request):
  queryset_list=Hospital.objects.all()
  return render(request,'list_hospital.html',{'queryset_list':queryset_list,'titulo':'Hospitales'})



class privado(ListView):
    model=Hospital
    template_name='Privados.html'
    paginate_by=3
    
    def get_queryset(self):
        return Hospital.objects.all().filter(Sector=3).order_by('calificacion').reverse()


class publicos(ListView):
    model=Hospital
    template_name='publicos.html'
    paginate_by=3
    
    def get_queryset(self):
        return Hospital.objects.all().filter(Sector=1).order_by('calificacion').reverse()


class datos_hosp(ListView):
    model=Hospital
    template_name='hosp.html'
    queryset = Hospital.autorizados_objects.all()


def DetallePublicacion(request,pk):
    try:
        pub_id=Hospital.objects.get(pk=pk)
    except Hospital.DoesNotExist:
        raise Http404("No existe ese Hospital")
    if request.method == 'POST':
        pub_id=Hospital.autorizados_objects.get(pk=pk)
        pub_id.like()

    return render(
        request,
        'detallepublicacion.html',
        context={'Hospital':pub_id,}
    )




