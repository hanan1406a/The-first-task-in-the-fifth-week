import json
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator('FRzGcl1deop2G9Gxg3RkpHHI8KHADgDxfjRSrfMJ8sm3')

tts =TextToSpeechV1(
    authenticator=authenticator
)

tts.set_service_url('https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/c48e94a4-9dbd-491c-ab6c-3cc1403ffb32')


with open('./speech.mp3', 'wb') as audio_file:
     res = tts.synthesize('Testing text to speech service', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
     audio_file.write(res.content) 