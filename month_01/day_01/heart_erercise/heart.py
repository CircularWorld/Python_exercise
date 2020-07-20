from pyecharts.charts import WordCloud
from greetings import words

fr = open()
wc = WordCloud()
wc.add('', words, word_size_range=[12, 12], mask_image=('heart.jpg'))
wc.render('render.html')
