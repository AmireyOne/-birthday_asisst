from django import forms



class Form_Comments(forms.Form):

    def __init__(self , *args , **kwargs):
        super(Form_Comments , self).__init__(*args , **kwargs)
        for item in Form_Comments.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"

    Title=forms.CharField(max_length=200 , required=True ,widget=forms.TextInput(attrs={'placeholder': 'عنوان نظر خود را بنویسید'}  ) , label="عنوان نظر")
    Comment=forms.CharField(  required=True ,widget=forms.Textarea(attrs={'placeholder': 'نظر خود راجب این محصول را بنویسید'}  ) , label="متن نظر")


class Form_Questions(forms.Form):

    def __init__(self , *args , **kwargs):
        super(Form_Questions , self).__init__(*args , **kwargs)
        for item in Form_Questions.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"

   
    question=forms.CharField(  required=True ,widget=forms.Textarea(attrs={'placeholder': 'سوال خود راجب این محصول را بپرسید'}  ) , label="متن سوال")