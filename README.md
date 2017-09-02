
Flask Project Template
===================

Hey! This is a custom flask project template with reconfigured flask plugins.

----------


Plugins
-------------
- flask restless
- flask httpauth
- flask login
- flask sqlalchemy

Project Structure
---
```
project
│   .gitignore
│   config.py
│   requirements.txt
│   run.py
│
├───app
│   │   __init__.py 
│   │
│   ├───main_module
│   │       admin.py
│   │       api.py
│   │       auth.py
│   │       auth_routes.py
│   │       models.py
│   │       populate_db.py
│   │       routes.py
│   │       __init__.py
│   │    
│   ├───static
│   ├───templates
│   │   │   index_.html
│   │   │
│   │   ├───admin
│   │   │       your template.html
│   │   │
│   │   ├───authentication
│   │   │       login.html
│   │   │
│   │   └───base
│   │           master.html
│   │
```

