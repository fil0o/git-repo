import os
import time
import zipfile

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
#source = ['"\\\\192.168.1.33\\ad\\base_backup"']
source = 'E:\\kaz\\'

# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.

target_dir = 'E:\\base_back'  # Подставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
today = target_dir + os.sep + time.strftime('%d_%m_%Y')
# Текущее время служит  именем zip-архива.
now = time.strftime('%H%M%S')

# Запрашивает комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# Создаем каталог если его еще нет
if not os.path.exists(today):
    os.mkdir(today)  # Создает каталог
    print('Каталог успешно создан', today)

zip_create = zipfile.ZipFile(target, 'w')
for root, dirs, files in os.walk(source):
    for file in files:
        zip_create.write(os.path.join(root,file))

zip_create.close()
print('Резервная копия успешно создана в', target)
