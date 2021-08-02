from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

key='cpsigaKFRv5pHjt8A4mlDuazW50Pf0d92rtQdpRCtfFs'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/0b1ebf80-3db5-42c4-b823-54c43421c09b'

authenticatorVar = IAMAuthenticator(key)
tts = TextToSpeechV1(authenticator=authenticatorVar)
tts.set_service_url(url)


with open('./watson-streaming-stt/text.txt', 'r') as f:
    text = f.readlines()
text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)




with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_MichaelV3Voice').get_result()
    audio_file.write(res.content)



