Sky-Reg

Установка необходимых утилит (Windows)
------------

### Установка make (необходимо: https://chocolatey.org/install)
~~~
choco install make
~~~
### Установка nvm
~~~
https://github.com/coreybutler/nvm-windows
~~~
~~~
nvm install 19.0.0
nvm use 19.0.0
~~~
### Установка pyenv
~~~
https://github.com/pyenv-win/pyenv-win
~~~
~~~
pyenv install 3.10.0
pyenv global 3.10.0
~~~

### Установка poetry (PowerShell)
~~~
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
~~~
В случае ошибки
~~~
Set-ExecutionPolicy RemoteSigned
~~~
### Установка yarn
~~~
https://classic.yarnpkg.com/lang/en/docs/install/#windows-stable****
~~~
### Установка GTK3
~~~
https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer
~~~
------------

Запуск проекта
------------
Запуск установки
~~~
poetry update
make install
~~~
После
~~~
make run
~~~
------------
