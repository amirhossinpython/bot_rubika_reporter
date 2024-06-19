import os

try:
    from rubpy import Client, filters, utils,enums,exceptions,Rubino
    from rubpy.types import Updates
    from rubpy.enums import ReportType
except ImportError :
    os.system("pip install rubpy ")
import time
import random

# نشستی که ربات روی حساب شما داره
bot = Client(name='Reporter', display_welcome=False)

    
@bot.on_message_updates()
async def updates(update: Updates):
    
    list_report =[
        "SPAM",
        "obscene",
        "violence",
        "Fraud and fraud",
        "child abuse",
        "Copyright infringement",
        
        
        
    ]
    # گزارشات به طور راندم
    res=random.choice(list_report)
    object_guid ="""
        گوید حساب را وارد کنید 
    """
    # محل گذاشتن گوید کاربر
    
    print(f"target : {object_guid}")
    
    report_type =res
    # متغییر توضحیات برای سایر گزارشات
    description ="""
    Hello, this user has insulted the sanctities and religion of Islam, spreads rumors against the system of the Islamic Republic of Iran, and promotes prostitution and corruption in cyberspace.
    """
    
    # نوع شناسه گزارشی که میخواید بدید
    report_type_object="User"
    count = 0
    
    
    #در حلقه تکرار شروع به گزارش زدن میکند وگزارشات را میشمارد 
   
        
        
    
    while True :
        
        try:
            try:
                
                
                result =bot.report_object(object_guid=object_guid,report_type=report_type,report_type_object=report_type_object,description=description)
                count += 1
                # 5ثانیه تاخییر در گزارش
                time.sleep(5)
                print(f"Report {count}: {res}")
            except exceptions.InvalidInpu as inv:
                
                print(inv)
        except Exception as er:
            print(er)
                    


bot.run()




