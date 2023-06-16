# Web project example

Пример простого backend на django и frontend из HTML/CSS/JS для выполнения проекта в рамках учебы для системы автоматизированного доступа к инструментам 

## BackEnd на django
Собранный в данном примере django сервер во многом опирается и повторяет [статью](https://webdevblog.ru/sozdanie-django-api-ispolzuya-django-rest-framework-apiview/). 

Надо отметить, что в этой версии включен механизм CORS для запросов от фронтенда. Грубо говоря это механизм защиты от принятия запросов с незнакомого frontend.
Этот механизм требует дополнительной установки модуля для django через pip:
`$ pip install django-cors-headers`

## QR сканер
В данном примере используется библиотека instascan для javascript. Ссылка на нее [тут](https://github.com/schmich/instascan).

## Инструкция по развертке
Нужно распаковать zip в отедльную папку на компьютере. Открыть папку через консоль. с помощью команд cd перейти в директорию backend. Далее с помощью команды python manage.py runserver 
*1) Если хотите запустить просто на своем компьютере, то ничего больше не пишете* 
*2) Если хотите запустить на лане, то нужно добавить 0.0.0.0:8000*. 
Если вы ввели вторую команду, то это значит любое устройство (которое подключено к одной сети с компьютером) сможет теперь зайти на него по адресу, который можно посмотреть в настройках сети ( вам нужен ipv4 адрес, он имеет примерно такой вид 100.65.38.120 ). Только не забудьте указать после адреса через : порт на котором вы запустили сайт, в нашем примере это 8000.


(Также возможно для использования страницы с камерой и ее корректным отображением нужно будет добавить сайт в исключение безопасности в браузере. Самый простой способ сделать это через хром с помощью команды - chrome://flags/#unsafely-treat-insecure-origin-as-secure , но также можно и в других.
