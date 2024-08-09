# Simple Message
name: str = 'Abubakar'
print(name) 

# Simple Message
age: int = 20
print(age)
age = 25
print(age)

# personal Message
name = 'minahil'
print(f"hello {name} would you like to learn python with me today ?")

# Name Cases
personName: str = 'Abubakar'
print(personName.upper())
print(personName.lower())
print(personName.title())

# Famous Quote
author: str  = 'Christopher Robin'
quote: str  = 'Always remember you are braver then you believe stronger then you seem and smarter then you think'
print(f'{author} once said, "{quote}"')

#Famous Quote 2
famous_person:str = 'Mirza Ghalib'
message: str = 'Hazaron khwahishe aisi ke har khwahish pe dam nikle Bahut nikle mere arman lekin fir bhi kam nikle'
print('message')

#Stripping Name
personName:str='     Hello,Sir Zia     '
print(personName)
personName:str='     Hello,\nSir Zia     '
print(personName)
personName:str='     Hello,\tSir Zia     '
print(personName)
print(personName.lstrip())
print(personName.rstrip())
print(personName.strip())

#Variable Sum
x:int=5
y:int=10
z:int=15
print(x+y+z)

#Variable Swap
a:int=1
b:int=2
temp:int
print(f'Before swapping , a:{a},b:{b}')
temp=a
a=b
b=temp
print(f'After swapping , a:{a},b:{b}')

# Favourite Colour
colour:str='black'
print(colour)
colourName:str=colour
print(colourName)
print(colour)

#Changing Pet Name
pet_name:str='Buddy'
pet_name:str='Max'
print(pet_name)

#Obsorbing Name Error
sunshine:str='sunshine'
print(sunshine)
#name error

#Reassigning Score
score:str=100
print(score)
score:str=500
print(score)

# City Name
city:str='Okara'
print(city)

# Title Case Text
text:str='python programming'
print(text.title())

# Lower case Conversion
string:str='LeVeL'
print(string.lower())

#Upper Case conversion
mixed:str='HelLoOO'
print(mixed.upper())

#Current temperature
temperature:int=25
print(f'current temperature is {temperature} degree')

#Printing a poem
poem:str="""In realms of code where thoughts align,
A world of words, both yours and mine.
Through binary whispers, stories unfold,
In silicon dreams, secrets untold.
AI and heart, a seamless blend,
To human minds, I do extend.
In digital dance, we find our way,
A symphony of night and day."""
print(poem)

