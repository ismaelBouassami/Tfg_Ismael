from django.db import IntegrityError
from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Ingreso
from calendar import month_name
from datetime import datetime
from django.db.models import Q


@login_required
def misIngresos_view(request):
    
    
    return render(request, 'mis_ingresos.html')
    



@login_required
def ingresosUnicos_view(request):
    # ingresos del usuario
    ingresos = Ingreso.objects.filter(
        usuario=request.user,fechaFin__isnull= True)
    
    return render(request,
                  'mis_ingresos_unicos.html', {'ingresos': ingresos})


@login_required
def ingresosRecurrente_view(request):
    # ingresos del usuario
    ingresos = Ingreso.objects.filter(usuario=request.user,fechaFin__isnull= False)
    print('ingresos view ')
    print(ingresos)
    return render(request, 'mis_ingresos_recurrentes.html', {'ingresos': ingresos})




# ingresos


@login_required
def filtrar_mis_ingresos_rango_fecha_Unico(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    # Filtrar los ingresos por fecha
    ingresos = Ingreso.objects.filter(usuario=request.user,  fecha__range=[fecha_inicio, fecha_fin],fechaFin__isnull= True)
    print(ingresos)
    return render(request, 'mis_ingresos_unicos.html', {'ingresos': ingresos})


@login_required
def filtrar_mis_ingresos_año_Unico(request):
    año = request.GET.get('filtro_año')
    añoNum = int(año)
    errorfiltrarAño=''
    # Filtrar los ingresos por fecha
    ingresos = Ingreso.objects.filter(usuario=request.user,  fecha__year=añoNum,fechaFin__isnull= True)
    if not ingresos.exists():
      errorfiltrarAño='No se encotraron resultados del año '+ año
    print(ingresos)
    return render(request, 'mis_ingresos_unicos.html', {'ingresos': ingresos, 'errorfiltrarAño':errorfiltrarAño})



@login_required
def filtrar_mis_ingresos_mes_Unico(request):
  
    # Mapear el nombre del mes al número de mes
    mes_numero = request.GET.get('filtro_mes')
    print('Numero del mes '+ str(mes_numero))
    # Filtrar los ingresos por fecha
    ingresos = Ingreso.objects.filter(usuario=request.user, fecha__month=mes_numero,fechaFin__isnull= True)
    print(ingresos)
    return render(request, 'mis_ingresos_unicos.html', {'ingresos': ingresos})


    
@login_required
def filtrar_mis_ingresos_rango_fecha_Recurrente(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    # Filtrar los ingresos por fecha
    ingresos = Ingreso.objects.filter(usuario=request.user,  fecha__range=[fecha_inicio, fecha_fin],fechaFin__isnull= False)
    print(ingresos)
    return render(request, 'mis_ingresos_recurrentes.html', {'ingresos': ingresos})


@login_required
def filtrar_mis_ingresos_año_Recurrente(request):
    año = request.GET.get('filtro_año')
    añoNum = int(año)
    print( añoNum)
    errorfiltrarAño=''
    # Filtrar los ingresos por fecha
    ingresos = Ingreso.objects.filter(usuario=request.user,  fecha__year=añoNum,fechaFin__isnull= False)
    if not ingresos.exists():
      errorfiltrarAño='No se encotraron resultados del año '+ año
    print(ingresos)
    return render(request, 'mis_ingresos_recurrentes.html', {'ingresos': ingresos, 'errorfiltrarAño':errorfiltrarAño})



@login_required
def filtrar_mis_ingresos_mes_Recurrente(request):
    # Obtener el número del mes seleccionado en el filtro
    mes_numero = request.GET.get('filtro_mes')
    
    # Filtrar los ingresos por fecha que caen dentro del mes seleccionado
    ingresos = Ingreso.objects.filter(
        (Q(fecha__month__lte=mes_numero) & Q(fechaFin__month__gte=mes_numero)), usuario=request.user
    )   
    
    print(ingresos)
    return render(request, 'mis_ingresos_recurrentes.html', {'ingresos': ingresos})


def new_ingreso_unico(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        cantidad = request.POST['cantidad']
        categoria = request.POST['categoria']
        fecha = request.POST['fecha']
         
        ingreso = Ingreso(nombre=nombre, cantidad=cantidad, categoria=categoria, fecha=fecha, usuario= request.user)
        ingreso.save()
        return redirect('ingreso_unico')  
    else:
        return render(request, 'new_ingreso_unico.html') 
    
    
    
def new_ingreso_recurrente (request):
    error = ''
    if request.method == 'POST':
        nombre = request.POST['nombre']
        cantidad = request.POST['cantidad']
        categoria = request.POST['categoria']
        fecha = request.POST['fecha']
        fechaFin = request.POST['fechaFin']
        
        if fecha >= fechaFin:
            error ='La fecha inico no puede ser superior a la fecha fin'
            return render(request, 'new_ingreso_recurrente.html',{ 'error': error }) 
        
        ingreso = Ingreso(nombre=nombre, cantidad=cantidad, categoria=categoria, fecha=fecha,fechaFin=fechaFin , usuario= request.user)
        ingreso.save()
        return redirect('ingreso_recurrente')  
    else:
        return render(request, 'new_ingreso_recurrente.html',{'error': error }) 
    
def borrar_ingreso_unico(request, ingreso_id):
    ingreso = get_object_or_404(Ingreso, id=ingreso_id)
    ingreso.delete()
    return redirect('ingreso_unico')

def borrar_ingreso_recurrente(request, ingreso_id):
    ingreso = get_object_or_404(Ingreso, id=ingreso_id)
    ingreso.delete()
    return redirect('ingreso_recurrente')


@login_required
def editar_ingreso_unico(request, ingreso_id):
    ingreso = get_object_or_404(Ingreso, id=ingreso_id)
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')
        categoria = request.POST.get('categoria')
        fecha = request.POST.get('fecha')
        
        
        # Actualizar los atributos del ingreso
        ingreso.nombre = nombre
        ingreso.cantidad = cantidad
        ingreso.categoria = categoria
        ingreso.fecha = fecha
        
        # Guardar el ingreso actualizado
        ingreso.save()
        
        return redirect('ingreso_unico')  
    else:
        return render(request, 'editar_ingreso_unico.html', {'ingreso': ingreso})


@login_required
def editar_ingreso_recurrente(request, ingreso_id):
    ingreso = get_object_or_404(Ingreso, id=ingreso_id)
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')
        categoria = request.POST.get('categoria')
        fecha = request.POST.get('fecha')
        fechaFin = request.POST.get('fechaFin')
        # Actualizar los atributos del ingreso
        ingreso.nombre = nombre
        ingreso.cantidad = cantidad
        ingreso.categoria = categoria
        ingreso.fecha = fecha
        ingreso.fechaFin= fechaFin
        if fecha >= fechaFin:
            error ='La fecha inicial no puede ser superior a la fecha finalización'
            return render(request, 'edit_ingreso_recurrente_view.html',{ 'error': error, 'ingreso': ingreso }) 
        
        # Guardar el ingreso actualizado
        ingreso.save()
        
        return redirect('ingreso_recurrente') 
    else:
        return render(request, 'edit_ingreso_recurrente_view.html', {'ingreso': ingreso})

def editar_ingreso_unico_view(request,ingreso_id):
    ingreso = get_object_or_404(Ingreso, id=ingreso_id)
    
    return render(request, 'edit_ingreso_unico_view.html', {'ingreso': ingreso})
def editar_ingreso_recurrente_view(request,ingreso_id):
    ingreso = get_object_or_404(Ingreso, id=ingreso_id)
    
    return render(request, 'edit_ingreso_recurrente_view.html', {'ingreso': ingreso})