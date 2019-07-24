# SchoolLibrary
This project is a simple interface for the small school's library. A user of this program can:  
* get information about all books in the library;
* add new book (schoolbook and fiction book) in the database;
* search need books using some nformation about title, author for example.

This program is a project written by for education next technologies:
* python 3.7
* pyqt5
* pytest
* etc

# Install environments

You need activate virtual environment.

If you use `virtualenvwrapper` run next command in a terminal:

```bash
mkvirtualenv your_environment
workon your_environment
pip install -r requirements.txt
```

If you use `virtualenv` run next command in the directory with the current project.

On Linux:
```bash
virtualenv your_environment
source your_environment/bin/activate
pip install -r requirements.txt
```

On Windows:
```bash
virtualenv your_environment
your_environment/Scripts/activate
pip install -r requirements.txt
```

# Run the project

```bash
workon your_environment
python main.py
```

# Run all tests

You will open the directory with the project and will run:

```bash
workon your_environment
PYTHONPATH=. pytest tests/
```
