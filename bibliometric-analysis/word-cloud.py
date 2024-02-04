import os
import sys
import bibtexparser

from os import path
from wordcloud import WordCloud

if len(sys.argv) < 2:
    print('Invalid arg')
    sys.exit(1)


library = bibtexparser.parse_file(sys.argv[1])

if len(library.failed_blocks) > 0:
    print("Some blocks failed to parse. Check the entries of `library.failed_blocks`.")
    print(library.failed_blocks)
    exit(1)
else:
    print("All blocks parsed successfully...")

abstracts = []
for entry in library.entries:
    try:
        abstracts.append(entry.fields_dict['abstract'].value)
    except:
        continue
text = " ".join(abstracts)



# Generate a word cloud image
wc = WordCloud()
sw_add = {'approach', 'various', 'due', 'present', 'ensure', 'high', 'within', 'require', 'provide', 'achieve', 'paper', 'based', 'propose', 'proposed'}
wordcloud = WordCloud(max_font_size=200, width=1920, height=1080,
                      background_color='#0f131a', colormap='GnBu', stopwords=wc.stopwords.update(sw_add)).generate(text)

print(dir(wordcloud))
# print(wordcloud.to_array())

wordcloud.to_file('biscoito.png')

# sys.exit(0)
# Display the generated image:
# the matplotlib way:
# import matplotlib.pyplot as plt
# plt.imshow(wordcloud, interpolation='bilinear')
# # plt.axis("off")
# # plt.show()

# # lower max_font_size
# # wordcloud = WordCloud(max_font_size=30).generate(text)
# # plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()