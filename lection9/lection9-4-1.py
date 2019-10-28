"""
Принимаем адрес и ищем вхождения его как подстроки, выводим время отключения
"""
import json
fin=open("test.txt","r",encoding="utf-8")#lection-9-4-out.json
text=fin.read()
lst=json.loads(text)