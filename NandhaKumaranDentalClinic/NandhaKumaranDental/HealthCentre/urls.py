from django.urls import path

from . import views
# from django.urls import path
# from .views import get_whatsapp_number

urlpatterns = [
    path('', views.login, name = "index"),
    path('register', views.register, name = "register"),
    path('doctors', views.doctors, name = "doctors"),
    path('login', views.login, name = "login"),
    path('emergency', views.emergency, name = "emergency"),
    path('logout', views.logout, name = "logout"),
    path('contactus', views.contactus, name = "contactus"),
    path('onlineprescription', views.onlineprescription, name = "onlineprescription"),
    path('doctorprofile', views.doctorprofile, name = "doctorprofile"),
    #path('doctorprofile/<str:selectedMedicineValue>', views.doctorprofile, name = "doctorprofile"),
    path('doctorappointments', views.doctorappointments, name = "doctorappointments"),
    path('searchAppointments', views.searchAppointments, name = "searchAppointments"),
    path('searchPrescriptions', views.searchPrescriptions, name = "searchPrescriptions"),
    path('doctorappointmentsfalse', views.doctorappointmentsfalse, name = "doctorappointmentsfalse"),
    path('editAppointments/<pk>', views.editAppointments, name = 'editAppointments'),
    path('deleteappointment/<pk>', views.deleteappointment, name = 'deleteappointment'),
    path('deleteprescription/<pk>', views.deleteprescription, name = 'deleteprescription'),
    path('addingMedicineData/<str:selectedMedicineValue>', views.addingMedicineData, name = 'addingMedicineData'),
    path('generatePDF', views.generatePDF, name = "generatePDF"), 
    path('sendPdfinWhatsapp', views.sendPdfinWhatsapp, name = "sendPdfinWhatsapp"),
    path('dummy', views.dummy, name = "dummy")
    # path('editAppointments', views.editAppointments, name = 'editAppointments')
]

# from django.urls import path
# from your_app.views import get_whatsapp_number

# urlpatterns = [
#     # Other URL patterns...
#     path('whatsapp-number/<int:number_id>/', get_whatsapp_number, name='whatsapp_number'),
# ]
