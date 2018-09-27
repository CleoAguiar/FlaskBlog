# FlaskBlog
Microblog with Flask
```
FlaskBlog\
  venv\
  app\
    __init__.py
    errors.py
    forms.py
    models.py
    routes.py
    templates\
    	_post.html
    	404.html
    	500.html
    	base.html
    	edit_profile.html
    	index.html
    	login.html
    	register.html
    	user.html
  bin\
  docs\
  logs\
  	flaskblg.log
  tests\
  	tests.py
  setup.py
  flaskblog.py
```

## Test
Suite of automated tests 
```
nosetests -v tests\tests.py
```