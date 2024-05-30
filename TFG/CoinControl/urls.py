"""
URL configuration for CoinControl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CoinControllapp import views
from CoinControllapp import views_gastos, views_ingresos, views_estadisticas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('login/',views.user_login, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout_view, name='logout'),
    
    #Todas las rutas que tengan que ver con gastos
    path('mis_gastos/',views_gastos.misgastos_view, name='mis_gastos'),
    path('mis_gastos/unicos',views_gastos.gastosUnicos_view,name='gastos_unico'),
    path('mis_gastos/recurrente',views_gastos.gastosRecurrente_view,name='gastos_recurrente'),
    
    #Tipos de filtros Gastos
    path('mis_gastos/recurrentes/flitro_rango',views_gastos.filtrar_mis_gastos_rango_fecha_Recurrente, name='filtrar_mis_gastos_rango_fecha_Recurrente'),
    path('mis_gastos/recurrentes/flitro_mes',views_gastos.filtrar_mis_gastos_mes_Recurrente, name='filtrar_mis_gastos_mes_Recurrente'),
    path('mis_gastos/recurrentes/flitro_año',views_gastos.filtrar_mis_gastos_año_Recurrente, name='filtrar_mis_gastos_año_Recurrente'),
 
    path('mis_gastos/unicos/flitro_rango',views_gastos.filtrar_mis_gastos_rango_fecha_Unico, name='filtrar_mis_gastos_rango_fecha_Unico'),
    path('mis_gastos/unicos/flitro_mes',views_gastos.filtrar_mis_gastos_mes_Unico, name='filtrar_mis_gastos_mes_Unico'),
    path('mis_gastos/unicos/flitro_año',views_gastos.filtrar_mis_gastos_año_Unico, name='filtrar_mis_gastos_año_Unico'),
    #Editar Gastos, crear y borrar
    
    path('mis_gastos/unicos/new',views_gastos.new_gasto_unico, name='new_gasto_unico'),
    path('mis_gastos/recurrentes/new',views_gastos.new_gasto_recurrente, name='new_gasto_recurrente'),
    path('mis_gastos/borrarUnico/<int:gasto_id>/', views_gastos.borrar_gasto_unico, name='borrar_gasto_unico'),
    path('mis_gastos/borrarRecurrente/<int:gasto_id>/', views_gastos.borrar_gasto_recurrente, name='borrar_gasto_recurrente'),
    path('mis_gastos/editarUnico/<int:gasto_id>/', views_gastos.editar_gasto_unico, name='editar_gasto_unico'),
    path('mis_gastos/editarUnico/view/<int:gasto_id>/', views_gastos.editar_gasto_unico_view, name='editar_gasto_unico_view'),
    path('mis_gastos/editarRecurrente/view/<int:gasto_id>/', views_gastos.editar_gasto_recurrente_view, name='editar_gasto_recurrente_view'),
    path('mis_gastos/editarRecurrente/<int:gasto_id>/', views_gastos.editar_gasto_recurrente, name='editar_gasto_recurrente'),
  #  path('mis_ingresos/',views.misingresos_view, name='mis_ingresos'),
  
  
    # Todo  lo que tiene que ver con ingresos 
    path('mis_ingresos/',views_ingresos.misIngresos_view, name='mis_ingresos'),
    path('mis_ingresos/unicos',views_ingresos.ingresosUnicos_view,name='ingreso_unico'),
    path('mis_ingresos/recurrente',views_ingresos.ingresosRecurrente_view,name='ingreso_recurrente'),
    # Filtros ingresos
    
    
    #Tipos de filtros Ingresos
    path('mis_ingresos/recurrentes/flitro_rango',views_ingresos.filtrar_mis_ingresos_rango_fecha_Recurrente, name='filtrar_mis_ingresos_rango_fecha_Recurrente'),
    path('mis_ingresos/recurrentes/flitro_mes',views_ingresos.filtrar_mis_ingresos_mes_Recurrente, name='filtrar_mis_ingresos_mes_Recurrente'),
    path('mis_ingresos/recurrentes/flitro_año',views_ingresos.filtrar_mis_ingresos_año_Recurrente, name='filtrar_mis_ingresos_año_Recurrente'),
 
    path('mis_ingresos/unicos/flitro_rango',views_ingresos.filtrar_mis_ingresos_rango_fecha_Unico, name='filtrar_mis_ingresos_rango_fecha_Unico'),
    path('mis_ingresos/unicos/flitro_mes',views_ingresos.filtrar_mis_ingresos_mes_Unico, name='filtrar_mis_ingresos_mes_Unico'),
    path('mis_ingresos/unicos/flitro_año',views_ingresos.filtrar_mis_ingresos_año_Unico, name='filtrar_mis_ingresos_año_Unico'),
    
    #
    
    #Editar Gastos, crear y borrar
    
    path('mis_ingresos/unicos/new',views_ingresos.new_ingreso_unico, name='new_ingreso_unico'),
    path('mis_ingresos/recurrentes/new',views_ingresos.new_ingreso_recurrente, name='new_ingreso_recurrente'),
    path('mis_ingresos/borrarUnico/<int:ingreso_id>/', views_ingresos.borrar_ingreso_unico, name='borrar_ingreso_unico'),
    path('mis_ingresos/borrarRecurrente/<int:ingreso_id>/', views_ingresos.borrar_ingreso_recurrente, name='borrar_ingreso_recurrente'),
    path('mis_ingresos/editarUnico/<int:ingreso_id>/', views_ingresos.editar_ingreso_unico, name='editar_ingreso_unico'),
    path('mis_ingresos/editarUnico/view/<int:ingreso_id>/', views_ingresos.editar_ingreso_unico_view, name='editar_ingreso_unico_view'),
    path('mis_ingresos/editarRecurrente/view/<int:ingreso_id>/', views_ingresos.editar_ingreso_recurrente_view, name='editar_ingreso_recurrente_view'),
    path('mis_ingresos/editarRecurrente/<int:ingreso_id>/', views_ingresos.editar_ingreso_recurrente, name='editar_ingreso_recurrente'),
 
 
 
 
 
 #
    path('mis_stats/', views_estadisticas.mis_estadisticas, name='mis_estadisticas'),
    path('mis_stats/<tipo>/<mes>', views_estadisticas.statsInicio, name='stats_inicio'),
    path('mis_stats/<tipo>/filtrar/', views_estadisticas.filtrar_stats, name='filtrar_stats'),
    path('mis_stats/<tipo>/getStats/<mes>', views_estadisticas.obtener_filtro_mes, name='obtener_filtro_mes'),
 
]
