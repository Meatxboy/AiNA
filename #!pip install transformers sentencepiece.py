#!pip install transformers sentencepiece

import streamlit as st
from transformers import pipeline

model = pipeline(model="seara/rubert-tiny2-russian-sentiment")

def Em_T(x):
  model = pipeline(model="seara/rubert-tiny2-russian-sentiment")
  return model(x)

st.title('Определить настроение по тексту')

st.warning('Чтобы остановить программу напишите "стоп"')

inp = st.text_input('Введите фразу, а я определю ваше настроение: ')

x = Em_T(inp)[0]
acc = round(x['score'] * 100, 3)

st.text(f'Я уверена на {acc}%')

if x['label'] == 'negative':
  st.error('У вас плохое настроение')
elif x['label'] == 'positive':
  st.success('У вас хорошее настроение')
else:
  st.warning('У вас нейтральное настроение')