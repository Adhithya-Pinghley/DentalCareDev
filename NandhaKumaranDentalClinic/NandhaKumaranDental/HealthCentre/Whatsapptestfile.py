from WPP_Whatsapp import Create, PlaywrightSafeThread, Whatsapp
from django.conf import Settings
# if __name__ == '__main__':
    # from .views import catchgenqr
# import psutil

# genqr = ""

    # openWhatsapp()


def catchqr(qrCode: str , asciiQR: str , attempt: int, urlCode: str):
            """
            qrCode:"data:image/png;base64,",
            asciiQR:"",
            attempt:1,
            urlCode:"2@242",
            """
            
            getqr = asciiQR
            print(getqr)
            
            # global genqr
            genqr =qrCode
            # test = testqr()
            # print(test)
            # print(asciiQR)
            # print(attempt)
            # print(urlCode)

creator = ""
client = ""

class openWhatsapp():
        # start client with your session name
     
    def wp(DocName):
        from .views import catchgenqr
        your_session_name = DocName #"test"
        global creator
        creator = Create(session=your_session_name, catchQR= catchgenqr , logQR= True) #catchgenqr
        Settings.globalVar = creator
        global client
        client = creator.start()
        
        
    # Now scan Whatsapp Qrcode in browser
    # check state of login
        if creator.state != 'CONNECTED':
        
            raise Exception(creator.state)
        
        # return client
        client.close()

def whatsappApi(patientName, doctorName, whatsappNumber, time, date):
    # reclient= openWhatsapp.client
    from .views import catchgenqr
    phone_number = f"+91{whatsappNumber}" #phone_number = "+917904427507"  # or "+201016708170"
    message = f"Dear {patientName}, This is Dr.{doctorName}, from XYZ Clinic. Your Appointment is fixed at {time} on {date}. Please do not forget your prescription!! Thanks!!"
    # global client
    # result = client.sendText(phone_number, message)
    Sesscreator = Create(session=doctorName, catchQR= catchgenqr, logQR= True)
    sess = Sesscreator.session
    global client
    sessStart = Sesscreator.start()
    dumSess = sessStart.session
    result = sessStart.sendText(phone_number, message)
    sessStart.close()
    
def whatsappApiDoc(doctorName, whatsappNumber, time, date):
    from .views import catchgenqr
    phone_number = f"+91{whatsappNumber}" #phone_number = "+917904427507"  # or "+201016708170"
    message = f"Dear {doctorName}, You have an appointment fixed at {time} on {date}. Thanks!!"
    # global client
    # # Simple message
    # result = client.sendText(phone_number, message)
    Sesscreator = Create(session=doctorName, catchQR= catchgenqr, logQR= True)
    sess = Sesscreator.session
    global client
    sessStart = Sesscreator.start()
    dumSess = sessStart.session
    result = sessStart.sendText(phone_number, message)
    sessStart.close()

def whatsappApiEdit(patientName, doctorName, whatsappNumber, time, date):
    # reclient= openWhatsapp.client
    from .views import catchgenqr
    phone_number = f"+91{whatsappNumber}" #phone_number = "+917904427507"  # or "+201016708170"
    message = f"Dear {patientName}, This is Dr.{doctorName}, from xyz Clinic. Your Appointment has been changed to {time} on {date}. Please do not forget your prescription!! Thanks!!"
    global creator
    
    Sesscreator = Create(session=doctorName, catchQR= catchgenqr, logQR= True)
    sess = Sesscreator.session
    global client
    sessStart = Sesscreator.start()
    dumSess = sessStart.session
    result = sessStart.sendText(phone_number, message)
    sessStart.close()
    
def whatsappMedia(whatsappNumber, pdfPathForWP):
    from .views import catchgenqr
    phone_number = f"+91{whatsappNumber}"
    path = pdfPathForWP
    name = "dummy"
    caption = "Dummy"
    global client
    result = client.sendFile(phone_number, path, name, caption )
    # message = openWhatsapp.client.sendMessageOptions()


    # # for pc in psutil.process_iter():
    # #     try:
    # #         print(pc.cmdline())
    # #     except psutil.AccessDenied:
    # #         continue
        
    # # start client with your session name
    # your_session_name = "test"
    # # check_open_directory = False
    # creator = Create(session=your_session_name, check_open_directory = False )
    # # client = creator.start()
    # client = creator.start()
    # # Now scan Whatsapp Qrcode in browser

    # # check state of login
    # if creator.state != 'CONNECTED':
    #     raise Exception(creator.state)

    # phone_number = whatsappNumber # or "+201016708170"
    # message = '''Hello From WPP WhatsApp Test Code !
    # A reminder from Dr Nandha kumar Dental clinic. Your Appointment has been fixed on 12 July 23 at 6pm and Don't forget your prescription!! '''

    # # Simple message
    # result = client.sendText(phone_number, message)
    # chrome_process = psutil.Process(1300)
    # info = chrome_process.info()
    # print(info)