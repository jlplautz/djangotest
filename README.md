# djangotest
Django aplication with pytest procedure, oriented by The Dumbfounds .



## 1- Created a virtual environment
   - djangotest $ pyenv version
   - djangotest $ pyenv local 3.8.1
   - djangotest $ pipenv install django
   - djangotest $ pipenv install flake8 --dev
   - djangotest $ source .venv/bin/activate
   - (djangotest) djangotest $ pip freeze > requirements.txt
   - create a file .flake8
   ```
    [flake8]
    max-line-length = 120
    exclude = .venv
   ```
   - create a file .pyup.yml
   ```
    requirements:
      - Pipfile
      - Pipfile.lock
   ```

