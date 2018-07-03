#Q1
import re
emails=("zuck26@facebook.com"
    "page33@google.com"
    "jeff42@amazon.com")
pattern = '(\w+)@([A-Z0-9]+)\.([A-Z]{2,3})'
d=re.findall(pattern, emails, flags=re.IGNORECASE)
print(d)

#Q2
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
match=re.findall("B\w+",text)
print(match)
matcher = re.findall('b\w+' , text)
print(matcher)


#Q3
import re
sentence = "A, very very; irregular_sentence"
s=re.sub('[\W _]',' ',sentence)
print(s)

#Q4
import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
tweet = re.sub('http\S+\s*', '', tweet)
tweet = re.sub('RT|cc', '', tweet)
tweet = re.sub('#\S+', '', tweet)
tweet = re.sub('@\S+', '', tweet)
tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)
tweet = re.sub('\s+', ' ', tweet)
print(tweet)