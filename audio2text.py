#Transcribing an Audio File
import assemblyai as aai

aai.settings.api_key = "ASSEMBLY_AI_API_KEY"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)
