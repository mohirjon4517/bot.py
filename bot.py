
import telebot
from telebot import types
import pyowm
from pyowm.exceptions import api_response_error 
from pyowm.exceptions.api_call_error import APICallTimeoutError
import covid19_data
from google_currency import convert 
import requests 
owm = pyowm.OWM('4086f9b16065b2a2a98b558b17aad533', language='ru' )
TOKEN = "1185243077:AAHyQEh7saCgR0TWRuicqVlmXHrBeTzmVQs"
bot = telebot.TeleBot(TOKEN)	#create a new Telegram Bot object

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "<b>🇺🇸Choose language\n🇷🇺Выбери язык\n🇺🇿Tilni tanlang</b>", parse_mode="html" )
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	bt1 = types.KeyboardButton('eng🇺🇸')
	bt2 = types.KeyboardButton('рус🇷🇺')
	bt3 = types.KeyboardButton('uzb🇺🇿')
	markup.add(bt1,bt2,bt3)
	mes = "chatbot = @HACKER_MS"
	bot.send_message(message.chat.id,mes, reply_markup=markup)




@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()
	get_message = message.text.strip().lower()
	if get_message_bot == "uzb🇺🇿":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('valyuta💵')
		btn3 = types.KeyboardButton('ob-havo🌤')
		btn4 = types.KeyboardButton('covid19🦠')
		btn5 = types.KeyboardButton('youtube🎬')
		markup.add(btn1,  btn3, btn4, btn5  )
		o='<b>Salom ' + message.from_user.first_name +'</b>\n\nmen siz uchun👤 judaham ajoyib <i>botman</i>🧑‍💻\n siz mendan#️⃣\n <ins> 👉Valyuta💵🔄💶\n 👉ob-havo🌤\n 👉covid19🦠\n 👉youtube🎬\n</ins> sifatida foydalanishingiz mumkin \n\n  👆Qachonki mendan 5️⃣0️⃣0️⃣kishi foydalansa har-hil pul o\'tkazmalari ham bo\'ladi, 🔍google qidiruv tizimini ham menda telegramda foydalanishingiz mumkin '
		
	
		o+="\n\n\n☄️🧑‍💻Nima <i>yordam</i> kerak bo'lsa, pastda hammasi bor👇👇👇 "


	elif get_message_bot=="рус🇷🇺":
		o="Пожалуйста ждите\n\nпока не готов🔧\n"
		o+= "<b>🇺🇸Choose language\n🇷🇺Выбери язык\n🇺🇿Tilni tanlang</b>"
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		bt1 = types.KeyboardButton('eng🇺🇸')
		bt2 = types.KeyboardButton('рус🇷🇺')
		bt3 = types.KeyboardButton('uzb🇺🇿')
		markup.add(bt1,bt2,bt3)
		o+= "chatbot = @HACKER_MS"

	elif get_message_bot=="eng🇺🇸":
		o="Please wait🔧\n\nfor the time being don't ready\n\n"
		o+="<b>🇺🇸Choose language\n🇷🇺Выбери язык\n🇺🇿Tilni tanlang</b>"
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		bt1 = types.KeyboardButton('eng🇺🇸')
		bt2 = types.KeyboardButton('рус🇷🇺')
		bt3 = types.KeyboardButton('uzb🇺🇿')
		markup.add(bt1,bt2,bt3)
		o+= "chatbot = @HACKER_MS"

	elif get_message_bot == 'valyuta💵':
		o = "<b>💴VALYUTA💴 </b>\n<ins>(ingliz tilida🇺🇸)</ins>\n"
		o+="\n➿➿➿➿➿➿➿\n\n"
		o+= "<b>DOLLAR = SUM</b>\n👉" + (convert('usd', "UZS", 1) ) +"\n"
		o+="\n➿➿➿➿➿➿➿\n\n"
		o+= "<b>RUBL = SUM</b>\n👉" + (convert('RUB', "UZS", 1) ) +"\n"
		o+="\n➿➿➿➿➿➿➿\n\n"
		o+= "<b>EURO = SUM</b>\n👉" + (convert('EUR', "UZS", 1) ) +"\n"
		o+="\n➿➿➿➿➿➿➿\n\n"
		
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		btn1 = types.KeyboardButton("ko'proq💰")
		btn15 = types.KeyboardButton('🔙ortga')
		markup.add( btn1 , btn15 )
	elif get_message_bot == "ko'proq💰":
		o = "Ko'proq valyuta kurslarini bilmoqchimisiz, unda bu botga ulaning\n👉'iltimos kuting hali bot tayyor bo'lmadi'"
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		btn15 = types.KeyboardButton('🔙ortga')
		markup.add(btn15 )

	#ob havo
	elif get_message_bot == "ob-havo🌤":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('🔙ortga')
		markup.add( btn1 )
		#ob-havo
		try:
			observation = owm.weather_at_place('Tashkent')
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o= '<b>Toshkent' +"da" + " hozir:👇👇👇 </b>" +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			#
			observation = owm.weather_at_place('Andijon')
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o+= '<b>Andijon' +"da" + " hozir:👇👇👇 </b>" +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			observation = owm.weather_at_place('Bukhara')
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o+= '<b>Buhoro' +"da" + " hozir:👇👇👇</b> " +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			observation = owm.weather_at_place('Jizzax')
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o+= '<b>Jizzax' +"da" + " hozir:👇👇👇</b> " +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			
			observation = owm.weather_at_place("Farg'ona")
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o+= '<b>Farg\'ona' +"da" + " hozir:👇👇👇 </b>" +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			
			observation = owm.weather_at_place('Nukus')
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o+= '<b>Nukus' +"da" + " hozir:👇👇👇 </b>" +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			
			observation = owm.weather_at_place('Navoiy')
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o+= '<b>Navoiy' +"da" + " hozir:👇👇👇</b> " +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			
			observation = owm.weather_at_place('Khiva')
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o+= '<b>Xorazm' +"da" + " hozir:👇👇👇 </b>" +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			
			observation = owm.weather_at_place('Samarkand')
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o+= '<b>Samarqand' +"da" + " hozir:👇👇👇</b> " +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			
			observation = owm.weather_at_place('Namangan')
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o+= '<b>Namangan' +"da" + " hozir:👇👇👇 </b>" +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			
			observation = owm.weather_at_place('Qashqadaryo')
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o+= '<b>Qashqadaryo' +"da" + " hozir:👇👇👇</b> " +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			
			observation = owm.weather_at_place('Sirdaryo')
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o+= '<b>Sirdaryo' +"da" + " hozir:👇👇👇</b> " +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			
			observation = owm.weather_at_place("Казахстан")
			w = observation.get_weather() 
			t=w.get_temperature('celsius')["temp"]
			x=w.get_wind()['speed']
			b=w.get_humidity() 		
			o+= '<b>Qo\'shni Qozog\'iston' +"da" + " hozir:👇👇👇</b> " +"\n\n"
			o+='👉Havo harorati  '+ str(  t  )+ ' gradus  🌡' + " \n"
							
			o+='👉Shamol  '+str( x )+ "   Km/s  💨🌬 " + " tezligi bilan esmoqda "' \n'

			o+='👉Namlik:    ' +str(   b  )+"💧"' \n \n '


			if  t>25:
			   	o+='👉Hozir havo harorati issiq ☀'+ "\n\n\n"
			elif (t<=24) and (t>=11):
				o+='👉Hozir havo harorati meyyorida 🌤'+ "\n\n\n"
			elif  (t<=10) and (t>=0) :
			  	o+='👉Hozir havo harorati sovuq 🌫'+ "\n\n\n"
			elif t<=-1:
			  	o+='👉Hozir havo harorati judayam sovuq ❄️'+ "\n\n\n"
			

		except api_response_error.NotFoundError:
			o='👉Hato yozdingiz📌'
		except APICallTimeoutError:
			o="Internet bilan muammo"



	elif get_message_bot == "covid19🦠":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		btn1 = types.KeyboardButton('🔙ortga')
		markup.add( btn1 )
		total = covid19_data.dataByName("Total")    
		china = covid19_data.dataByName("China")
		US = covid19_data.dataByName("US")
		u = covid19_data.dataByName("Uzbekistan")
		kazak = covid19_data.dataByName("Kazakhstan")
		ru = covid19_data.dataByName("  Russia")
		af = covid19_data.dataByName("Afghanistan")
		tr = covid19_data.dataByName("Turkey")
		kr = covid19_data.dataByName("Kyrgyzstan")
		cd = covid19_data.dataByName(" Saudi Arabia")
		o = "<b>🌍Dunyo bo'yicha:</b>\n\n" + "<b><i>Kasallar: </i>"  + str(total.confirmed) + "\n" + "<i>Vafot etganlar:</i> " + str(total.deaths) + "\n" + "<i>Sog'ayib ketganlar:</i>" + str(total.recovered) + "</b> \n\n\n"
		o+="➿➿➿➿➿➿\n\n\n"
		o+="<b>🇺🇿O'zbekiston:</b>\n\n" + "<b><i>Kasallar: </i>"  + str(u.confirmed) + "\n" + "<i>Vafot etganlar:</i> " + str(u.deaths) + "\n" + "<i>Sog'ayib ketganlar:</i>" + str(u.recovered) + "</b> \n\n\n"
		o+="➿➿➿➿➿➿\n\n\n"
		o+="<b>🇺🇸Amerika:</b>\n\n" + "<b><i>Kasallar: </i>"  + str(US.confirmed) + "\n" + "<i>Vafot etganlar:</i> " + str(US.deaths) + "\n" + "<i>Sog'ayib ketganlar:</i>" + str(US.recovered) + "</b> \n\n\n"
		o+="➿➿➿➿➿➿\n\n\n"
		o+="<b>🇷🇺Rossiya:</b>\n\n" + "<b><i>Kasallar: </i>"  + str(ru.confirmed) + "\n" + "<i>Vafot etganlar:</i> " + str(ru.deaths) + "\n" + "<i>Sog'ayib ketganlar:</i>" + str(ru.recovered) + "</b> \n\n\n"
		o+="➿➿➿➿➿➿\n\n\n"
		o+="<b>🇨🇳Xitoy:</b>\n\n" + "<b><i>Kasallar: </i>"  + str(china.confirmed) + "\n" + "<i>Vafot etganlar:</i> " + str(china.deaths) + "\n" + "<i>Sog'ayib ketganlar:</i>" + str(china.recovered) + "</b> \n\n\n"
		o+="➿➿➿➿➿➿\n\n\n"
		o+="<b>🇸🇦Saudiya Arabistoni:</b>\n\n" + "<b><i>Kasallar: </i>"  + str(cd.confirmed) + "\n" + "<i>Vafot etganlar:</i> " + str(cd.deaths) + "\n" + "<i>Sog'ayib ketganlar:</i>" + str(cd.recovered) + "</b> \n\n\n"
		o+="➿➿➿➿➿➿\n\n\n"
		o+="<b>🇰🇿Qozog'iston:</b>\n\n" + "<b><i>Kasallar: </i>"  + str(kazak.confirmed) + "\n" + "<i>Vafot etganlar:</i> " + str(kazak.deaths) + "\n" + "<i>Sog'ayib ketganlar:</i>" + str(kazak.recovered) + "</b> \n\n\n"
		o+="➿➿➿➿➿➿\n\n\n"
		o+="<b>🇦🇫Afg'oniston:</b>\n\n" + "<b><i>Kasallar: </i>"  + str(af.confirmed) + "\n" + "<i>Vafot etganlar:</i> " + str(af.deaths) + "\n" + "<i>Sog'ayib ketganlar:</i>" + str(af.recovered) + "</b> \n\n\n"
		o+="➿➿➿➿➿➿\n\n\n"
		o+="<b>🇹🇷Turkiya:</b>\n\n" + "<b><i>Kasallar: </i>"  + str(tr.confirmed) + "\n" + "<i>Vafot etganlar:</i> " + str(tr.deaths) + "\n" + "<i>Sog'ayib ketganlar:</i>" + str(tr.recovered) + "</b> \n\n\n"
		o+="➿➿➿➿➿➿\n\n\n"
		o+="<b>🇰🇬Qirg'iziston:</b>\n\n" + "<b><i>Kasallar: </i>"  + str(kr.confirmed) + "\n" + "<i>Vafot etganlar:</i> " + str(kr.deaths) + "\n" + "<i>Sog'ayib ketganlar:</i>" + str(kr.recovered) + "</b> \n\n\n"
		o+="➿➿➿➿➿➿"

	
	elif get_message == "youtube🎬":
		o = "<b>Youtubedan nimani qidirmoqchisiz?\n</b>"
		o+=	"<ins>Mendan haligacha 500ta odam foydalangani yo'q🔄</ins>"
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		btn1 = types.KeyboardButton('🔙ortga')
		markup.add(btn1 )			
	



	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('valyuta💵')
		btn3 = types.KeyboardButton('ob-havo🌤')
		btn4 = types.KeyboardButton('covid19🦠')
		btn5 = types.KeyboardButton('youtube🎬')
		markup.add(btn1,  btn3, btn4, btn5  ) 	
		o = "<b>Hush kelibsiz</b>"
	bot.send_message(message.chat.id, o, parse_mode="html", reply_markup=markup)
	


@bot.message_handler(func=lambda message: True, content_types=['sticker'])
def echo_all(message):
	bot.reply_to(message, message.from_user.first_name  + " men  to'tiqushman")

bot.polling(none_stop = True)
