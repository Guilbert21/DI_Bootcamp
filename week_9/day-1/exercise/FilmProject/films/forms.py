from django import forms
from .models import Film, Director, Category, Country, models, Comment


# class FilmForm(forms.ModelForm):
#     class Meta:
#         model = Film
#         fields = '__all__'

# class DirectorForm(forms.ModelForm):
#     class Meta:
#         model = Director
#         fields = ['first_name', 'last_name']
    

# AddFilmForm
# class AddFilmForm(forms.form):
#     title = forms.CharField(label='Title', max_length=100)
#     release_date = forms.DateField(label='Release Date')
#     created_in_country = forms.ModelChoiceField(queryset=Country.objects.all())
#     category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'


# AddDirectorForm
# class AddDirectorForm(forms.form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     film = forms.ModelMultipleChoiceField(queryset=Film.objects.all()) 
class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__' 

# CommentForm
class CommentForm(forms.Modelform):
    class Meta:
        model = Comment
        fields = ['text']

    

