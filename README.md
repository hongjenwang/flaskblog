# Flask Blog

```bash
python3 -m venv testenv
source testenv/bin/activate
pip install -r requirements.txt
export FLASK_APP=flaskblog && python3 -m flask run
```

## If Missing Package

```bash
pip3 install <package_name> && pip3 freeze > requirements.txt
```
