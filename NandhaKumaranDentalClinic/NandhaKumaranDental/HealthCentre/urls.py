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
    path('addingSessionData/<str:SelectedSessionValue>', views.addingSessionData, name = 'addingSessionData'),
    path('generatePDF', views.generatePDF, name = "generatePDF"), 
    path('sendPdfinWhatsapp', views.sendPdfinWhatsapp, name = "sendPdfinWhatsapp"),
    path('dummy', views.dummy, name = "dummy"),
    path('createNewMedicine', views.createNewMedicine, name = 'createNewMedicine'),
    path('createTimeline', views.createTimeline, name='createTimeline'),
    path('catchqrcode', views.catchqrcode, name='catchqrcode'),
    # path('whatsappStatus', views.whatsappStatus, name='whatsappStatus'),
    path('whatsappBrowser', views.whatsappBrowser, name = 'whatsappBrowser'),
    path('patMed', views.patMed, name = 'patMed'),
    path('editPatientMed/<pk>', views.editPatientMed, name = 'editPatientMed'),
    path('medicineEdit/<pk>', views.medicineEdit, name = 'medicineEdit'),
    path('deletepatientDetails/<pk>', views.deletepatientDetails, name = 'deletepatientDetails'),
    path('deletemedicineDetails/<pk>', views.deletemedicineDetails, name = 'deletemedicineDetails'),
    path('searchPatients', views.searchPatients, name = 'searchPatients'),
    path('searchMedicine', views.searchMedicine, name = 'searchMedicine'),
    path('updateExcel', views.updateExcel, name = 'updateExcel'),
    path('uploadExcel', views.uploadExcel, name = 'uploadExcel'),
    path('countPrescriptionRows', views.countPrescriptionRows, name = 'countPrescriptionRows'),
    path('uploadImage', views.uploadImage, name = 'uploadImage'),
]

# from django.urls import path
# from your_app.views import get_whatsapp_number

# urlpatterns = [
#     # Other URL patterns...
#     path('whatsapp-number/<int:number_id>/', get_whatsapp_number, name='whatsapp_number'),
# ]
