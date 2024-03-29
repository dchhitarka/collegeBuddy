from django import forms
from .models import UserAccount, Posts, Notes
from django.core import validators
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

class UserAccountCreation(forms.ModelForm):
    raw_password = forms.CharField(widget=forms.PasswordInput)
    raw_password_cm = forms.CharField(widget=forms.PasswordInput)
    
    class Meta():
        model = UserAccount
        fields = ['first_name', 'last_name', 'email', 'username', 'reg_no']
    
    def clean_password(self):
        p1 = self.cleaned_data.get('raw_password')
        p2 = self.cleaned_data.get('raw_password_cm')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Password Do not match!")
        return p2
    
    def save(self, commit=True):
        user = super(UserAccountCreation, self).save(commit=False)
        user.set_password(self.cleaned_data.get('raw_password'))
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta():
        model = Posts
        fields = []

class NotesForm(forms.ModelForm):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"placeholder": "Title"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 15, "cols": 25, "placeholder": "Write something here..."}))
    class Meta():
        model = Notes
        fields = ['title', 'content']