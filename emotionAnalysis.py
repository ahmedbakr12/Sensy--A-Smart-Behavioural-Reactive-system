# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zk9DjNm-3iHAAp5fnJxwMgBRtsuYDNSG
"""

! pip install transformers -q

from transformers import pipeline

emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')

emotion_labels = emotion("i feel a little bit worried")

emotion_labels

emotion_labels[0]['label']

import pandas as pd

large_text = pd.read_csv('https://github.com/abishekarun/Text-Emotion-Classification/blob/master/text_emotion.csv?raw=true')

large_text.shape

large_text.head()

large_text = large_text[:100]

large_text.shape

large_text['content'][1:10].apply(emotion)

def get_emotion_label(text):
  return(emotion(text)[0]['label'])

get_emotion_label("i think we have solved well in the exam but i feel worried")

large_text['content'][1:10].apply(get_emotion_label)

large_text['emotion'] = large_text['content'].apply(get_emotion_label)

large_text

import seaborn as sns

sns.countplot(data = large_text, y = 'emotion').set_title("Emotion Distribution")