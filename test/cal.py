import pyjokes

joke1 = pyjokes.get_joke(language='en', category= 'all')

joke2 = pyjokes.get_joke(language='en', category= 'neutral')


print(joke2)
print(joke1)
