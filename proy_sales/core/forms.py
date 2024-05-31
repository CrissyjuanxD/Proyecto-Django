from django import forms
from core.models import Product , Category , Supplier , Brand
class ProductForm(forms.ModelForm):
        
    class Meta:
        model=Product
        fields=['description','price','stock','expiration_date','brand','supplier','categories','line','image']

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['description']
        
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'ruc', 'address', 'phone']
        
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['description']