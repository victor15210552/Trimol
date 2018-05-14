from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from Aplicacion.forms import SignUpForm, Hospital_form, Especialidad_form, Sector_form, Estado_form
#Prueva view dinamic
from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import FormView

def Hospital(request):
    args={}
    args.update(csrf(request))

    args['articles']=Hospital.objects.all()
    return render_to_response('Hospital.html',args)





#def Hospital(request):
 #    form=Hospital_form(request.POST or None)
  #   if request.method=='POST':
   #     if form.is_valid():
    #        form.save()
     #       form = Hospital_form()
     #return render(request,'Hospital.html',{'form':form,'titulo':'Hospital'})

def Especialidad(request):
     form=Especialidad_form(request.POST or None)
     if request.method=='POST':
        if form.is_valid():
            form.save()
            form = Especialidad_form()
     return render(request,'Especialidad.html',{'form':form,'titulo':'Especialidad'})

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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def prueba(request):
    return render(request, 'prueba.html')

#Reporte
#1. Importar el modelo ej. 
from Aplicacion.models import Hospital,Ubicacion
#2. Crear lavista del reporte.html
def reporte_uno(request):
  return render(request, 'reporte.html', {'Hospital': Hospital.objects.all()})  

#Prueba dinamic view
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
    Hospitales=Hospital.objects.filter(Nombre__contains=buscar)
    if Hospitales:
      print ("Ha buscado un hospitalpor su nombre")
      return render(request,'busca.html',
        {'Hospitales':Hospitales, 'hospital':True})
    else:
      print ("NO existe")
      return render(request, 'Noexiste.html')

class BuscarEspecialidad(TemplateView):

  def post(self,request,*args, **kwargs):
    especialidad=request.POST['especial']
    Especialidades=Especialidad.objects.filter(Nombre__contains=especialidad)
    if Especialidades:
      print ("Ha buscado una especialidad su nombre")
     # return render(request,'buscaE.html',
      # {'Especialidades':Especialidades, 'especial':True})

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