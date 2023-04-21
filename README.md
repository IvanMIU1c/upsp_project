# Web project example

Пример простого backend на django и frontend из HTML/CSS/JS для выполнения проекта в рамках учебы для системы автоматизированного доступа к инструментам 

## BackEnd на django
Собранный в данном примере django сервер во многом опирается и повторяет [статью](https://webdevblog.ru/sozdanie-django-api-ispolzuya-django-rest-framework-apiview/). 

Надо отметить, что в этой версии включен механизм CORS для запросов от фронтенда. Грубо говоря это механизм защиты от принятия запросов с незнакомого frontend.
Этот механизм требует дополнительной установки модуля для django через pip:
`$ pip install django-cors-headers`

## QR сканер
В данном примере используется библиотека instascan для javascript. Ссылка на нее [тут](https://github.com/schmich/instascan).

