#!/bin/bash


if  pyenv versions | grep 2.7.1 
then
	echo "Python 2.7.1 already exists"
else 
pyenv install 2.7.1
fi


if pyenv versions | grep 3.7.1
then
	echo "Python 3.7.1 already exists"
else 
pyenv install 3.7.1
fi


pyenv virtualenv 2.7.1 p271
pyenv activate p271 
python -V
python -c "print('Hello world!') "


pyenv virtualenv 3.7.1 p371
pyenv activate p371 
python -V
python -c "print('Hello world!') "
