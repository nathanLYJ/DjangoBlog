from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import ChatForm
from openai import OpenAI
from django.conf import settings
from django.views.generic import TemplateView
import fitz  # PyMuPDF
from youtube_transcript_api import YouTubeTranscriptApi
from .models import SearchHistory

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def get_completion(prompt, model="gpt-3.5-turbo"):
    try:
        chat_completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.5,
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"


def extract_text_from_pdf(pdf_file):
    # PDF파일에서 텍스트를 추출 함수
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text


def extract_text_from_youtube(url):
    # Youtube URL에서 자막(스크립트를)을 추출하는 함수
    # http://www.youtube.com/watch?v=
    video_id = url.split("v=")[-1]  # Youtube URL에서  video_id 추출
    # get_transcript 해당하는 비디오 ID를 기반으로 동영상 자막을 가져오게 됨
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    # 자막 텍스트를 하나의 문자열로 결합하는 과정 -> 리스트컴프리핸션! 공백으로 연결해서 하나의 텍스트로 만들어줌
    transcript_text = " ".join([item["text"] for item in transcript])
    return transcript_text


def translate_to_korean(text, model="gpt-3.5-turbo"):
    try:
        translation_prompt = f"국어로 번역해줘: {text}"
        translatation = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": translation_prompt}],
            max_tokens=100,
            temperature=0.5,
        )
        return translatation.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"


def generate_prompt(text_input=None, file_input=None, youtube_url=None):
    if text_input:
        return f"다음 내용을 10줄 이내로 요약해줘: {text_input}"
    elif file_input:
        file_content = extract_text_from_pdf(file_input)
        return f"다음 PDF파일 내용을 10줄 이내로 요약해줘: {file_content}"
    elif youtube_url:
        youtube_content = extract_text_from_youtube(youtube_url)
        return f"다음 Youtube 동영상 내용을 10줄 이내로 요약해줘: {youtube_content}"
    else:
        return "요약할 내용이 없습니다."


class ChatView(LoginRequiredMixin, FormView):
    template_name = "chatgpt/chatgpt.html"
    form_class = ChatForm
    success_url = "/"  # 폼 제출 후 다시 메인 페이지로 리디렉션

    def form_valid(self, form):
        text_input = form.cleaned_data["text_input"]
        file_input = form.cleaned_data["file_input"]
        youtube_url = form.cleaned_data["youtube_url"]
        prompt = generate_prompt(text_input, file_input, youtube_url)
        summary_result = get_completion(prompt)

        translation_result = translate_to_korean(summary_result)
        # 검색기록이 저장!
        SearchHistory.objects.create(
            user=self.request.user,
            url=youtube_url,
            text_input=text_input,
            file_name=file_input.name if file_input else None,
            summary_result=summary_result,
            translation_result=translation_result,
        )

        return self.render_to_response(
            self.get_context_data(
                summary_result=summary_result, translation_result=translation_result
            )
        )
