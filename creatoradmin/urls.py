from django.urls import path
from creatoradmin import views
from django.contrib.auth import views as auth_views
urlpatterns = [
########################################################################################################################
################################ FOR CREATOR  ##########################################################################
########################################################################################################################
    path('register_creator/', views.register_creator, name='register_creator'),
    path('login_form/', views.login_form, name='login_form'),
    path('creator/', views.creator, name='creator'),
    path('client/', views.client, name='client'),
    path('user_update/', views.user_update, name='user_update'),
    path('logout_form/', views.logout_form, name='logout_form'),
    path('user_password/', views.user_password, name='user_password'),
########################################################################################################################
################################ FOR CLIENT  ###########################################################################
########################################################################################################################
    path('register/', views.register, name='register'),
    path('user_update_client/', views.user_update_client, name='user_update_client'),
    path('user_password_client/', views.user_password_client, name='user_password_client'),
    path('user_orders_product/', views.user_orders_product, name='user_orders_product'),
    path('user_order_product_detail_client/<int:id>/<int:oid>', views.user_order_product_detail_client, name='user_order_product_detail_client'),
    path('order_delate_client/<int:pk>', views.order_delate_client, name='order_delate_client'),
########################################################################################################################
################################ INFORMATIONS ##########################################################################
########################################################################################################################
    path('addinformatsions/', views.addinformatsions, name='addinformatsions'),
    path('informatsion_update/', views.informatsion_update, name='informatsion_update'),
    path('info_edit/<int:id>', views.info_edit, name='info_edit'),
    path('info_delate/<int:id>', views.info_delate, name='info_delate'),
    path('info_delate_all/', views.info_delate_all, name='info_delate_all'),
########################################################################################################################
################################ CATEGORY ##############################################################################
########################################################################################################################
    path('addcategory/', views.addcategory, name='addcategory'),
    path('category_update/', views.category_update, name='category_update'),
    path('category_edit/<int:id>', views.category_edit, name='category_edit'),
    path('category_delate/<int:id>', views.category_delate, name='category_delate'),
    path('category_delate_all/', views.category_delate_all, name='category_delate_all'),
########################################################################################################################
################################ PRODUCTS ##############################################################################
########################################################################################################################
    path('addproduct/', views.addproduct, name='addproduct'),
    path('product_update/', views.product_update, name='product_update'),
    path('product_edit/<int:id>', views.product_edit, name='product_edit'),
    path('product_delate/<int:id>', views.product_delate, name='product_delate'),
    path('product_delate_all/', views.product_delate_all, name='product_delate_all'),
########################################################################################################################
################################ ORDERSSS ##############################################################################
########################################################################################################################
    path('order_all/', views.order_all, name='order_all'),
    path('orders/<int:id>', views.orders, name='orders'),
    path('order_delate/<int:pk>', views.order_delate, name='order_delate'),
    path('order_delate_all/', views.order_delate_all, name='order_delate_all'),
########################################################################################################################
################################ DETAILS-PRODUCT #######################################################################
########################################################################################################################
    path('apanddetail/', views.apanddetail, name='apanddetail'),
    path('details_update/', views.details_update, name='details_update'),
    path('detail_edit/<int:id>', views.detail_edit, name='detail_edit'),
    path('detail_delate/<int:id>', views.detail_delate, name='detail_delate'),
    path('detail_delate_all/', views.detail_delate_all, name='detail_delate_all'),
########################################################################################################################
################################### BLOG ###############################################################################
    path('apandblog/', views.apandblog, name='apandblog'),
    path('blog_update/', views.blog_update, name='blog_update'),
    path('blog_edit/<int:id>', views.blog_edit, name='blog_edit'),
    path('blog_delate/<int:id>', views.blog_delate, name='blog_delate'),
    path('blog_delate_all/', views.blog_delate_all, name='blog_delate_all'),
########################################################################################################################
########################################## ABOUT US ####################################################################
########################################################################################################################
    path('apandabout/', views.apandabout, name='apandabout'),
    path('about_update/', views.about_update, name='about_update'),
    path('about_edit/<int:id>', views.about_edit, name='about_edit'),
    path('about_delate/<int:id>', views.about_delate, name='about_delate'),
    path('about_delate_all/', views.about_delate_all, name='about_delate_all'),
########################################################################################################################
########################################## FAQ  ########################################################################
########################################################################################################################
    path('apandfaqs/', views.apandfaqs, name='apandfaqs'),
    path('faq_update/', views.faq_update, name='faq_update'),
    path('faq_edit/<int:id>', views.faq_edit, name='faq_edit'),
    path('faq_delate/<int:id>', views.faq_delate, name='faq_delate'),
    path('faq_delate_all/', views.faq_delate_all, name='faq_delate_all'),
########################################################################################################################
########################################## NEWSLATTER  #################################################################
########################################################################################################################
    path('newslatter_get/', views.newslatter_get, name='newslatter_get'),
    path('newslatter_delate/<int:id>', views.newslatter_delate, name='newslatter_delate'),
    path('newslatter_delate_all/', views.newslatter_delate_all, name='newslatter_delate_all'),
########################################################################################################################
########################################## CONTACTUS  ##################################################################
########################################################################################################################
    path('contact_get/', views.contact_get, name='contact_get'),
    path('contact_edit/<int:id>', views.contact_edit, name='contact_edit'),
    path('contact_delate/<int:id>', views.contact_delate, name='contact_delate'),
    path('contact_delate_all/', views.contact_delate_all, name='contact_delate_all'),
########################################################################################################################
########################################## BLOG COMMENTS  ##############################################################
########################################################################################################################
    path('comment_blog_get/', views.comment_blog_get, name='comment_blog_get'),
    path('comment_blog_edit/<int:id>', views.comment_blog_edit, name='comment_blog_edit'),
    path('coment_blog_delate/<int:id>', views.coment_blog_delate, name='coment_blog_delate'),
    path('coment_blog_delate_all/', views.coment_blog_delate_all, name='coment_blog_delate_all'),
########################################################################################################################
########################################## PRODUCTS COMMENTS  ##########################################################
########################################################################################################################
    path('comment_product_get/', views.comment_product_get, name='comment_product_get'),
    path('comment_product_edit/<int:id>', views.comment_product_edit, name='comment_product_edit'),
    path('coment_product_delate/<int:id>', views.coment_product_delate, name='coment_product_delate'),
    path('coment_product_delate_all/', views.coment_product_delate_all, name='coment_product_delate_all'),
########################################################################################################################
########################################## USER PERMISSION  ############################################################
########################################################################################################################
    path('users_get/', views.users_get, name='users_get'),
    path('apanduserpermission/<int:id>', views.apanduserpermission, name='apanduserpermission'),
    path('users_delete/<int:id>', views.users_delete, name='users_delete'),
    path('users_delete_delate_all/', views.users_delete_delate_all, name='users_delete_delate_all'),
########################################################################################################################
########################################## PRODUCT GALLERY  ############################################################
########################################################################################################################
    path('product_gallery/', views.product_gallery, name='product_gallery'),
    path('product_gallery_id/<int:id>', views.product_gallery_id, name='product_gallery_id'),
########################################################################################################################
########################################## PRODUCT SEARCHED  ###########################################################
########################################################################################################################
    path('searched/', views.searched, name='searched'),
########################################################################################################################
################################################   SLIDER   ############################################################
########################################################################################################################
    path('apandslider/', views.apandslider, name='apandslider'),
    path('slider_update/', views.slider_update, name='slider_update'),
    path('slider_edit/<int:id>', views.slider_edit, name='slider_edit'),
    path('slider_delate/<int:id>', views.slider_delate, name='slider_delate'),
    path('slider_delate_all/', views.slider_delate_all, name='slider_delate_all'),
########################################################################################################################
################################################   FORGET PASSWORD RESET  ##############################################
########################################################################################################################
    path('password_reset', auth_views.PasswordResetView.as_view(template_name = 'Reset_password/password_reset_form.html'), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name = 'Reset_password/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'Reset_password/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name = 'Reset_password/password_reset_complete.html'),name='password_reset_complete'),
]