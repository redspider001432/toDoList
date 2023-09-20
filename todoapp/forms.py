from django import forms
from .models import Task,Tag
from django.utils import timezone

class TaskForm(forms.ModelForm):
    tags = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'tags', 'status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        if self.instance and self.instance.pk:  # Set initial value for tags field based on existing tags in the instance
            self.fields['tags'].initial = ', '.join(tag.name for tag in self.instance.tags.all())
        else:
            self.fields['tags'].initial = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        self.initial['tags'] = self.fields['tags'].initial


    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if tags:
            tags = [tag.strip() for tag in tags.split(',')]  # Split tags by comma and remove leading/trailing spaces
        return tags if tags else []
    
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and self.instance and self.instance.timestamp:
            if due_date < self.instance.timestamp:
                raise forms.ValidationError("Due Date cannot be before the Timestamp created.")
        return due_date

    
    def save(self, commit=True):
        instance = super().save(commit=False)
        tags = self.cleaned_data.get('tags')
        if tags:
            instance.save()
            instance.tags.clear()
            for tag in tags:
                tag_obj, _ = Tag.objects.get_or_create(name=tag)
                instance.tags.add(tag_obj)
        else:
            instance.tags.clear()
        if commit:
            instance.save()
        return instance

