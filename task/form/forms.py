from django import forms

CONTINENTS = (
    ('Africa','Africa'),
    ('Asia','Asia'),
    ('Australia','Australia'),
    ('Europe','Europe'),
    ('North America','North America'),
    ('South America','South America'),
)


class ExampleForm(forms.Form):
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=64)
    date_of_birth = forms.DateTimeField()
    email = forms.EmailField()
    favourite_number = forms.IntegerField()
    your_continent = forms.ChoiceField(choices=CONTINENTS)