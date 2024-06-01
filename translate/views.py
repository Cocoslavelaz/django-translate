from django.shortcuts import render
from msrest.authentication import CognitiveServicesCredentials
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

# Create your views here.
def index(request):
    T_REGION = 'eastus' # 填入位置/區域
    T_KEY = '8172170dfee1419e96108bfd158af72e' # 填入金鑰
    T_ENDPOINT = 'https://api.cognitive.microsofttranslator.com/' # 填入文字翻譯的 Web API
    if request.method == "POST":
        word = request.POST.get('word',None)
        text_translator = TextTranslationClient(
        endpoint=T_ENDPOINT,
        credential=TranslatorCredential(T_KEY, T_REGION)
    )
        targets = []
        targets.append(InputTextItem(text=word))
        responses = text_translator.translate(content=targets, to=["zh-hant"], from_parameter="en")
        output = responses[0]["translations"][0]["text"]
        print(output)
    args = {"text":output}


    

    return render(request,'./translate/index.html',args)
