from django import forms

from .models import Item

INPUT_CLASSES='w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','name','description','price','image')
        widgets={
            'category':forms.Select(attrs={
            'class':INPUT_CLASSES
            }),
            
            'name':forms.TextInput(attrs={
            'class':INPUT_CLASSES
            }),
            
            'description':forms.Textarea(attrs={
            'class':INPUT_CLASSES
            }),
            
            'price':forms.TextInput(attrs={
            'class':INPUT_CLASSES
            })
        }


INPUT_CLASSES='w-full py-4 px-6 rounded-xl border'
class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','description','price','image','is_booked')
        widgets={
            
            'name':forms.TextInput(attrs={
            'class':INPUT_CLASSES
            }),
            
            'description':forms.Textarea(attrs={
            'class':INPUT_CLASSES
            }),
            
            'price':forms.TextInput(attrs={
            'class':INPUT_CLASSES
            })
        }