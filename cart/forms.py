from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label="")
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class Cart_one_prod(forms.Form):
    """
    func onli 1 item
    for tenplate:
                for{biz|gos}
    """
    quantity = forms.IntegerField(initial=1,widget=forms.HiddenInput)
    update = forms.CharField(required=False, initial=False, widget=forms.HiddenInput)
