from tkinter import *
from tkinter import font
import requests

#날씨 찾는 함수

#날씨정보 사이트 (OpenWeather map site)에 접속해 데이터 가져오기(회원가입, API 키를 가져오기 등의 사전 준비 필요)

#url = 접속 링크

#city = 문자열 리스트

def city_weather(city):
    weather_Key = '5287789411ed2a8ad052d7fd6f97510e' #API 키
    url = 'http://api.openweathermap.org/data/2.5/weather' #url 
    parameter = {'APPID': weather_Key, 'q':city, 'units':'Metric'} #q = 도시 및 국가 #'units':'Metric' = 현재 기온을 섭씨온도로 출력
    response = requests.get(url, parameter)
    weather = response.json()
    label['text'] = weather_Result(weather)

    
#도시, 날씨, 온도를 알려주는 함수
   
def weather_Result(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp= weather['main']['temp']

        result =  '도시: %s \n\n날씨: %s \n\n온도:(C)%s' %(name,description,temp)
    except:
        result = 'There was a problem\n retrieving that information'

    return result #result 값 반환

window = Tk()
window.title("오늘의 날씨는 어떤가요?")
window.geometry("700x500")

window.resizable(width = False, height = False) #창 크기 조절 X

#백그라운드 이미지

background_image = PhotoImage(file='날씨 배경사진.png')
background_label = Label(window,image= background_image)

#relwidth = 위젯의 너비 비율, 기본값 : 0, 속성 : 0 ~ 1
#relheight = 위젯의 높이 비율, 기본값 : 0, 속성 : 0 ~ 1

background_label.place(x= 0, y =0, relwidth=1, relheight=1)

#( 검색 창 + 버튼 ) 프레임 색, 두께 설정 및 좌표설정

frame = Frame(window,bg='light green',bd=5)

#relx = x좌표 배치 비율, 기본값 : 0, 속성 : 0 ~ 1

#rely = y좌표 배치 비율, 기본값 : 0, 속성 : 0 ~ 1

#anchor = 위젯의 기준 위치 기본값 : nw 속성 : n, e, w, s, ne, nw, se, sw

frame.place(relx=0.5, rely=0.15, relwidth=0.5, relheight=0.1,anchor='n')
button = Button(frame, text ='날씨 찾기',font=40, command=lambda: city_weather(entry.get())) #lambda = 쓰고 버리는 일시적인 함수. 필요한 곳에서 즉시 사용하고 버릴 수 있음
button.place(relx=0.7, relwidth=0.3, relheight=1)



#relwidth = 위젯의 너비 비율, 기본값 : 0, 속성 : 0 ~ 1
#relheight = 위젯의 높이  비율, 기본값 : 0, 속성 : 0 ~ 1

#검색창 폰트 설정 및 좌표설정

entry = Entry(frame, font=("나눔고딕",25)) #Entry = 글자 입력할 수 있는 창 생성
entry.place(relwidth=0.65, relheight=1) 

#결과 창 프레임 색, 두께 설정 및 좌표설정

frame2 = Frame(window,bg='light blue',bd=10)
frame2.place(relx=0.5, rely=0.35, relwidth=0.5,relheight=0.55, anchor='n')

#결과창 폰트 설정

label = Label(frame2, font=("나눔고딕",18) )
label.place(relwidth=1, relheight=1)

window.mainloop()
