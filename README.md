Добрый день!

то что я не смог сделать:

1 Поиск, выдаёт ошибку которую я не смог решить

2 Docker

Инструкция

Установить 
клонировать проект из след. ссылки на гитхаб
git@github.com:UralSultan/geofarmm.git
я не стал помещать .env  в .gitignore, чтоб было легче для запуска.

python 3.10 или выше
postgresql 14 или выше

Запустить команды ниже:

apt-get install -y binutils libproj-dev gdal-bin python3-gdal
apt-get install --yes libgdal-dev

создать базу данных с раширениями 
![Снимок экрана 2023-01-26 в 16.08.27.png](..%2F..%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-01-26%20%D0%B2%2016.08.27.png)
postgis
postgis_topology

создать миграции


http://127.0.0.1:8000/fields/ = api для показа полей, для просмотра данной панели необходимо пройти
авторизацию в админ панели
создание полей производится только через админ панель, так как необходимо видеть карту.

http://127.0.0.1:8000/register/ = api для регистрации пользователей, необходимо выдать права superuser в админ панели
так как просматривать и создавать или редактировать может авторизованный пользователь, пользователь будет видеть только
свои записи, если создать и сменить пользователя то он не увидит записи первого.

http://127.0.0.1:8000/register/<id>/ = api для редактирования записей пользлвателя.