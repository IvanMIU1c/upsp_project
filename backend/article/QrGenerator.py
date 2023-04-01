import qrcode
import uuid as uuid

qr_file = 'qrcode.png'
# Информация, которыя будет закодирована в QR-код
data = uuid.uuid4();
# Создание QR-кода
img = qrcode.make(data)
# Сохранение QR-кода в файл
img.save(qr_file)