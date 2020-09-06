# Instalación
## Python
```
pyenv install 3.7.8
```
## Actualizar pip
```
python -m pip install --upgrade pip
```
## Instalar dependencias
```
pip install -r requirements.txt
```

### Descargar modelos de spaCy
```
python -m spacy download es_core_news_md
python -m spacy link es_core_news_md es
```
## Entrenar modelo
```
rasa train
```

# Correr
## Rasa actions
```
rasa run  actions
```
##  Duckling
```
docker run -p 8000:8000 rasa/duckling
```

## RASA
```
rasa shell --debug
```
