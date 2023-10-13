# FastAPI Template

```
This template has connect to sql and mongo database(s)
```

## Structure of this project:
{template} \
├── app\
│   ├── config\
│   │   ├── _init__.py\
│   │   └── config.py\
│   ├── db\
│   │   └── __init__.py\
│   ├── models\
│   │   └── __init__.py\
│   ├── routes\
│   │   ├── __init__.py\
│   │   ├── include\
│   │   │   ├── __init__.py\
│   │   │   └── healthcheck.py\
│   │   └── routes.py\
│   ├── services\
│   │   └── __init__.py\
│   ├── test\
│   │   ├── __init__.py\
│   │   └── test.py\
│   └── utils\
|   |   |── __init__.py
│   │   └── util.py\
│   ├── main.py\
├── Docker-compose.yml\
├── Dockerfile\
├── README.md\
├── requirements.txt\
└── run.py

## Flow of this project:
This flow will run:
```
run.py -> main.py -> (middleware) -> routes -> services <-> models  
```
                                              
## How to use this project:
First, you need have virtualenv for running this project ( smooth):

Unix/ Linux
```
pip install virtualenv
```

Create virtualenv:
```
virtualenv env
```

Activate virtualenv:

Windows:
```
.\env\Scripts\activate
```

Unix/ Linux:

```
source env/bin/activate
```

Install packages:
```
pip install -r requirements.txt
``` 

Run this project:
```
python run.py
```

