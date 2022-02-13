from modeltranslation.translator import register, TranslationOptions
from home.models import Informations, Blog, Aboutus, FAQ, Slider


@register(Informations)
class InformationsTranslationOptions(TranslationOptions):
    fields = ('title', 'address', 'description',)


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Aboutus)
class AboutusTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)