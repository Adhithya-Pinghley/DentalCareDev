from WPP_Whatsapp import Create
# import psutil


    
    
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

class openWhatsapp():
    # start client with your session name
    your_session_name = "test"
    creator = Create(session=your_session_name)
    client = creator.start()
    # Now scan Whatsapp Qrcode in browser

    # check state of login
    if creator.state != 'CONNECTED':
        raise Exception(creator.state)

def whatsappApi(patientName, whatsappNumber, time, date):
    # reclient= openWhatsapp.client
    phone_number = f"+91{whatsappNumber}" #phone_number = "+917904427507"  # or "+201016708170"
    message = f"Dear, {patientName} This is Dr.Nanda's Dental Clinic. Your Appointment is fixed at {time} on {date}. Please do not forget your prescription!! Thansk!!"

    # Simple message
    result = openWhatsapp.client.sendText(phone_number, message)

def whatsappApiEdit(patientName, whatsappNumber, time, date):
    # reclient= openWhatsapp.client
    phone_number = f"+91{whatsappNumber}" #phone_number = "+917904427507"  # or "+201016708170"
    message = f"Dear, {patientName} This is Dr.Nanda's Dental Clinic. Your Appointment has been changed to {time} on {date}. Please do not forget your prescription!! Thansk!!"

    # Simple message
    result = openWhatsapp.client.sendText(phone_number, message)

def whatsappMedia(whatsappNumber, pdfPathForWP):
    phone_number = f"+91{whatsappNumber}"
    path = pdfPathForWP
    name = "dummy"
    caption = "Dummy"
    result = openWhatsapp.client.sendFile(phone_number, path, name, caption )
    # message = openWhatsapp.client.sendMessageOptions()