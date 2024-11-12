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

from transformers import pipeline

model = pipeline(model="seara/rubert-tiny2-russian-sentiment")

def Em_T():
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