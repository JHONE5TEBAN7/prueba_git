# Base Django

## Iniciar en Windows

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Abre http://127.0.0.1:8000/ para ver la página de inicio. Los clientes pueden registrarse desde `/cuenta/registro/`; el login está en `/cuenta/entrar/`. El administrador creado con `createsuperuser` puede iniciar sesión y acceder a `/admin/`.

La vista y la plantilla inicial están en `inicio/`. La configuración del proyecto está en `config/`.