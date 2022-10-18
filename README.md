# WhoWantsToBecomeAMillioner

# commit - по сути точка сохранения при разработки проекта

# ветка - способ разделить разрабокту на несколько путей, для работы в команде (не забываем слить ветки в конце)

# репозиторий github - по сути аналог гугл диска, но для программиста. Удаленая папка на сервере. 



<h1>Команды git:</h1>

<h3>Список команд для создание комита:</h3>

git add .  # иницилизирует точку создания комита (локальную)
git commit -m 'Our comments'  # добавляем название комита
git push  # отправляет локальные изменения на удаленный сервер github


git pull  # обновляет локальную версию до новой версии с сервера /дз: git log, git status, dir, cd, git clone, rm/

git status # команда покажет какие файлы были изменены 

git log # команда показывает свойства коммита - автора, дату, хэш функцию, на какой ветке находится коммит



<h3>Список команд для работы с ветками:</h3>

git branch newbranchname - создание новой ветке в проекте (с того комита на котором сейчас стоит HEAD)

git checkout master - переход на ветку master

git branch -a   - вывести все ветки в репозитории (через * обозначается ветка в которой мы сейчас находимся)

Чтобы слить две ветки, сначала нужно перейсти в более приоритетную (в которую будем сливать), затем вызвать команду:

git merge namebeanch2  - указываем имя ветки которую хотим сливать с основной



<h1>Команды консоли:</h1>

dir # показывает файлы в папке

cd # команда, помогающая попасть в папу

cd .. # способ спуститься по директории назад (выйти из папки) 

del # удаление файла из папки (директории) 
