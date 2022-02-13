from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from creatoradmin.models import Client, Creator
from home.models import Informations, Blog, Aboutus, FAQ, ContactMessage, Comment_blog, Slider
from order.models import OrderProduct
from product.models import Category, Product, Images, Comment


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=255, label='Username')
    email = forms.CharField(max_length=255, label='Email')
    first_name = forms.CharField(max_length=255, label='Firstname')
    last_name = forms.CharField(max_length=255, label='Lastname')

    class Meta:
        model= User
        fields = ('username', 'email', 'first_name', 'last_name')



class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Creator
        fields=['phone', 'address', 'city', 'country', 'image',]


class UserClientUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')



class ProfileClinetUpdateForms(forms.ModelForm):
    class Meta:
        model = Client
        fields=['phone', 'address', 'city', 'country', 'image', 'description',]

########################################################################################################################
################################ INFORMATIONS ##########################################################################
########################################################################################################################

class AddInformationsForm(forms.ModelForm):
    class Meta:
        model = Informations
        fields = [ 'title_uz', 'title_en', 'title_ru','country', 'city', 'address_en','address_ru','address_uz','phone','email', 'image', 'telegram','instagram','facebook','twitter','status', 'location', 'description_uz', 'description_en', 'description_ru',]


class EditInformationsForm(forms.ModelForm):
    class Meta:
        model = Informations
        fields = [ 'title_uz', 'title_en', 'title_ru','country', 'city', 'address_en','address_ru','address_uz','phone','email', 'image', 'telegram','instagram','facebook','twitter','status','location', 'description_uz', 'description_en', 'description_ru',]


########################################################################################################################
################################### CATEGORY ###########################################################################
########################################################################################################################

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [ 'title_uz', 'title_en', 'title_ru', 'description_uz', 'description_en', 'description_ru', 'image',  'slug', 'status']


class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [ 'title_uz', 'title_en', 'title_ru', 'description_uz', 'description_en', 'description_ru', 'image',  'slug', 'status']

########################################################################################################################
################################### PRODUCTS ###########################################################################
########################################################################################################################
class AddProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'category', 'title_uz', 'title_en', 'title_ru', 'old_price', 'sell_price', 'image',  'slug', 'status', 'description_uz', 'description_en', 'description_ru',]


class EditProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'category', 'title_uz', 'title_en', 'title_ru', 'old_price', 'sell_price', 'image',  'slug', 'status', 'description_uz', 'description_en', 'description_ru',]

########################################################################################################################
################################### ORDERSSS ###########################################################################
########################################################################################################################

class EditOrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = [ 'status']

########################################################################################################################
################################### APPAND-DETAILS #####################################################################
########################################################################################################################
class AppandDetailsForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = [ 'product', 'image', 'collor', 'size',]


class EditDetailsForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = [ 'product', 'image', 'collor', 'size',]


########################################################################################################################
################################### BLOG ###############################################################################
########################################################################################################################
class AppandBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [ 'title_uz','title_en','title_ru', 'image', 'status', 'description_uz','description_en','description_ru',]

class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [ 'title_uz','title_en','title_ru', 'image', 'status', 'description_uz','description_en','description_ru',]

########################################################################################################################
########################################## ABOUT US ####################################################################
########################################################################################################################
class AppandAboutForm(forms.ModelForm):
    class Meta:
        model = Aboutus
        fields = [ 'title_uz','title_en','title_ru', 'image', 'status', 'description_uz','description_en','description_ru',]

class EditAboutForm(forms.ModelForm):
    class Meta:
        model = Aboutus
        fields = [ 'title_uz','title_en','title_ru', 'image', 'status', 'description_uz','description_en','description_ru',]

########################################################################################################################
########################################## FAQ  ########################################################################
########################################################################################################################

class AppandFAQSForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['ordernumber', 'question_en','question_ru','question_uz', 'answer_en','answer_ru','answer_uz', 'status']


class EditFAQSForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['ordernumber', 'question_en','question_ru','question_uz', 'answer_en','answer_ru','answer_uz', 'status']


########################################################################################################################
########################################## CONTACTUS  ##################################################################
########################################################################################################################

class EditContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['status']


########################################################################################################################
########################################## BLOG COMMENTS  ##############################################################
########################################################################################################################
class EditComentsBlogForm(forms.ModelForm):
    class Meta:
        model = Comment_blog
        fields = ['status']
########################################################################################################################
########################################## PRODUCTS COMMENTS  ##########################################################
########################################################################################################################
class EditCommentProductForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['status']
########################################################################################################################
########################################## USER PERMISSION  ############################################################
########################################################################################################################
class UserPermissonForm(forms.ModelForm):
    class Meta:
        model = Creator
        fields = ['user','image']

########################################################################################################################
################################################   SLIDER   ############################################################
########################################################################################################################
class AppandSliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = [ 'title_uz','title_en','title_ru', 'image', 'status', 'description_uz','description_en','description_ru',]

class EditSliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = [ 'title_uz','title_en','title_ru', 'image', 'status', 'description_uz','description_en','description_ru',]