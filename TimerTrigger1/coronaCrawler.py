import time
import requests
from bs4 import BeautifulSoup

def corona():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90&oquery=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90+%EC%A7%80%EC%97%AD%EB%B3%84&tqi=hKfw%2BdprvhGssFNiur8ssssst4Z-170822'

    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    seoulTotal = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    seoulNew = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    ulsanTotal = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    ulsanNew = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    daeguTotal  = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    daeguNew = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    gwangjuTotal  = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    gwangjuNew  = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    busanTotal  = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    busanNew  = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    daejeonTotal  = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    daejeonNew = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    incheonTotal = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()
    incheonNew = soup.select_one('##_cs_production_type > div > div:nth-child(7) > div.patients_info > div:nth-child(3) > div:nth-child(1) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').get_text()


    
    return list[seoulTotal, seoulNew, ulsanTotal, ulsanNew, daeguTotal, daeguNew,
     gwangjuTotal, gwangjuNew, busanTotal, busanNew, daejeonTotal, daejeonNew, incheonTotal, incheonNew]