# Обрезка ссылок с помощью Битли

Программа может сокращать ссылки используя сервис Bitly, и выводить информацию о количестве переходов по этим ссылкам.

### Как установить

Для корректрой работы программы необходимо использовать токен Bitly. Получить токен можно в [личном кабинете по ссылке](https://app.bitly.com/settings/api/).
Его необходимо сохранить в переменную среды BITLY_TOKEN, в файле .env. Конечная запись должна иметь вид BITLY_TOKEN=sa0m0p000000let0ok0000e00n000a0mp0le000.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).