print('program started')
import talkey
print('import complete')
tts = talkey.Talkey(
	preffered_languages = ['en'],
	espeak = {
		'languages': {
			'en': {
				'voice': 'english-mb-en1',
				'words_per_minute': 130
			}
		}
		
	})
print('settings in place')
tts.say('Hello, Rhodes!')
tts.say('This is my best intimidating voice. Let us go kick some robot butt.')
tts.say('Do you want to play a game!')
