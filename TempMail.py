import requests
from bs4 import BeautifulSoup
import time

class TempMail():
	def __init__(self, proxies = None):
		self.proxies = proxies
		Data=self.get()

		self.get = Data[0]
		self.headers={'cookie':Data[1]}
		self.Start_Time = time.time()


	def get(self):
		response = requests.get('https://10minutemail.net/', proxies=self.proxies)
		return(BeautifulSoup(response.text, 'html.parser').find(id='fe_text')['value'], 'PHPSESSID='+response.cookies['PHPSESSID'])

	def Time_Order(self):
		Total_Segundos=self.Time_Seconds()
		return((Total_Segundos//60,Total_Segundos%60))

	def Time_Seconds(self):
		return(int(time.time()-self.Start_Time))

	def Response_Brute(self):
		response = requests.get('https://10minutemail.net/mailbox.ajax.php', headers=self.headers)
		return(response.text)

	def Response_Order(self):
		Data_brute = self.Response_Brute()

		soup = BeautifulSoup(Data_brute, 'html.parser')
		Info=[]

		for i in soup.find_all('tr'):
			Info.append([])
			for j in i.find_all('td'):
				Info[-1].append(j.get_text())

		del Info[0]
		del Info[-1]
		return(Info)


	def WaitResponse(self, stop = 1, cooldown = 0):
		Len_Message=0

		while stop>Len_Message:
			self.message=self.Response_Order()
			Len_Message=len(self.message)
			time.sleep(cooldown)

		return(self.message)

	def Reset_Time(self):
		response = requests.get('https://10minutemail.net/more.html', proxies=self.proxies, headers=self.headers)
		self.Start_Time=time.time()
		return('Los minutos se resetearon a 10!')
