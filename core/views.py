from django.shortcuts import render
# Create your views here.


# from google.cloud import aiplatform
import vertexai
from vertexai.preview.generative_models import GenerativeModel

vertexai.init(project="steady-course-401913", location="us-west4")
model_gemini = GenerativeModel("gemini-pro")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.8,
    "top_p": 0.9,
    "top_k": 15
}


def index(request):
    result_text = None
    query_language = 'Türkçe'
    context = {
        'result_text': None
    }
    if request.method == 'GET' and request.GET.get('search-box') is not None:
        keyword = request.GET.get('search-box')
        response = model_gemini.generate_content(
            f"""{query_language}'deki {keyword} kelimesinin Türkçedeki en sık kullanılan anlamının kökünü bul. Aşağıda vereceğim soruları etkileyici ve yaratıcı bir şekilde cevapla ve hepsini tek paragraf haline getir:
- Kelimenin kökü dile ilk geçtiği zamanlarda ve şimdi ne anlama gelmektedir? Bilgilendir ve kıyasla.
- Kelimenin kökünün önceki hali nasıldı?
- Kelimenin kökü dile geçtikten sonra kullanıldığı ilk yazılı kaynak nedir?
- Kelimeyi etimolojik olarak detaylı bir şekilde incele.
- Kelimeyi filolojik olarak detaylı bir şekilde incele.
- Kelimenin bugüne kadarki geçirdiği değişimleri adım adım incele.
Cevabını göndermeden önce kontrol et, aynı anlama gelecek cümleleri birleştir."""
        )
        result_text = response.text.replace('```html', '').replace(
            '```', '').replace('*', '')
        context['result_text'] = result_text

    return render(request, 'index.html', context)


def index_english(request):
    result_text = None
    query_language = 'English'
    context = {
        'result_text': None
    }
    if request.method == 'GET' and request.GET.get('search-box') is not None:
        keyword = request.GET.get('search-box')
        response = model_gemini.generate_content(
            f"""Find the root of the most commonly used {query_language} meaning of the word {keyword} in {query_language}. Answer the questions below in an impressive and creative way and compile them all into one paragraph:
- What did the root of the word mean when it first came into the language and now? Inform and compare.
- What was the previous version of the root of the word?
- What is the first written source in which the word was used after its root passed into the language?
- Examine the word etymologically in detail.
- Examine the word philologically in detail.
- Examine the changes the word has undergone step by step.
Check your answer before sending it and combine sentences that have the same meaning."""
        )
        result_text = response.text.replace(
            '```html', '').replace('```', '').replace('*', '')
        context['result_text'] = result_text

    return render(request, 'index-en.html', context)


def sitemap(request):
    return render(request, 'sitemap.xml')


def robots(request):
    return render(request, 'robots.txt')
