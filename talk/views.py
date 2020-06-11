from django.shortcuts import render
from . import forms
from django.template.context_processors import csrf
#from .tf20 import vgg16_imagenet as cl
from . import talk
from . import repeat
import speech_recognition as sr


# 応答用の辞書を組み立てて返す
def __makedic(k, txt):
    return {'k': k, 'txt': txt}


def talk_do(request):
    t = talk.Talk()
    if request.method == 'POST':
        # テキストボックスに入力されたメッセージ
        q = request.POST["texttwo"]
        # Talk-APIからの応答メッセージ取得
        a = t.get(q)
        # 描画用リストに最新のメッセージを格納する
        talktxts = []
        talktxts.append(__makedic('ai', a))
        talktxts.append(__makedic('b', q))
        # 過去の応答履歴をセッションから取り出してリストに追記する
        saveh = []
        if 'hist' in request.session:
            hists = request.session['hist']
            saveh = hists
            for h in reversed(hists):
                x = h.split(':')
                talktxts.append(__makedic(x[0], x[1]))
        # 最新のメッセージを履歴に加えてセッションに保存する
        saveh.append('b:' + q)
        saveh.append('ai:' + a)
        request.session['hist'] = saveh
        # 描画準備
        form = forms.UserForm(label_suffix='：')
        c = {
            'form': form,
            'texttwo': '',
            'talktxts': talktxts
        }
    else:
        # 初期表示の時にセッションもクリアする
        request.session.clear()
        # フォームの初期化
        form = forms.UserForm(label_suffix='：')
        c = {'form': form}
        c.update(csrf(request))
    return render(request, 'talk/talk.html', c)


def repeat_do(request):
    # マイクからの音声入力
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("話しかけてみましょう！")
        audio = r.listen(source)

    try:
        # 日本語でGoogle音声認識
        text = r.recognize_google(audio, language="ja-JP")

    except sr.UnknownValueError:
        print("Google音声認識は音声を理解できませんでした。")
    except sr.RequestError as e:
        print("Google音声認識サービスからの結果を要求できませんでした;"
              " {0}".format(e))
    else:
        # print(text)
        jtalk = repeat.jtalk_run(text)

    return render(request, 'talk/repeat.html', {'youtalk':text, 'jtalk':jtalk, })


def repeat_js(request):
    return render(request, 'talk/repeat.html', {})
