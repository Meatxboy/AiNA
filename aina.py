# -*- coding: utf-8 -*-
"""AiNA.ipynb

Исходный файл расположен по ссылке:
    https://colab.research.google.com/drive/1ESgyugW5-CnT9EbxCb3Q_cV4gelIQVfK

Модель определяет позитивную, нейтральную или негативную эмоцию содержит в себе текст.

Группа: Груздев Илья, Касимов Тимерхан.
"""

#Установка библиотек производится командами:
#pip install transformers sentencepiece
#pip install -q streamlit

import streamlit as st
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

model = pipeline(model="seara/rubert-tiny2-russian-sentiment")

def Em_T_accuracy(inp):
  res = model(inp)
  acc = round(res[0]['score'] * 100, 2)
  return acc

def Em_T_label(inp):
  res = model(inp)
  lbl = res[0]['label']
  return lbl

def Em_T(to_api=False):
  st.header('Определить настроение по тексту')

  inp = st.text_input('Введите фразу, а я определю ваше настроение: ')

  if st.button('Старт'):
    result = model(inp)
    acc = round(result[0]['score'] * 100, 2)

    if result[0]['label'] == 'negative':
      st.error(f'Я уверена на {acc}%, что у вас ПЛОХОЕ настроение')
    elif result[0]['label'] == 'positive':
      st.success(f'Я уверена на {acc}%, что у вас ХОРОШЕЕ настроение')
    else:
      st.warning(f'Я уверена на {acc}%, что у вас НЕЙТРАЛЬНОЕ настроение')

if __name__ == "__main__":
  Em_T()

#Работа с API

class Item(BaseModel):
  text: str


app = FastAPI()


@app.get('/')
def root():
  return {'massage': 'Я умею читать настроение по тексту'}


@app.get('/how/')
def how():
  
  res = model('Hello World!')
  acc = round(res[0]['score'] * 100, 2)

  if res[0]['label'] == 'negative':
    res = 'Негативное на' + str(acc) + '%'
  elif res[0]['label'] == 'positive':
    res = 'Позитивное на' + str(acc) + '%'
  else:
    res = 'Нейтральное на' + str(acc) + '%'

  return 'Например, я считаю, что "Hello world!" ' + res


@app.post('/predict/')
def predict(item: Item):
  res = model(item.text )[0]
  acc = round(res[0]['score'] * 100, 2)

  if res[0]['label'] == 'negative':
    res = 'Негативный на' + str(acc) + '%'
  elif res[0]['label'] == 'positive':
    res = 'Позитивный на' + str(acc) + '%'
  else:
    res = 'Нейтральный на' + str(acc) + '%'

  return 'Ваш текст ' + res
