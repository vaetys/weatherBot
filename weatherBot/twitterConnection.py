import twitter
api = twitter.Api(consumer_key='xAF16VY8LBjyV8H4DF7qJ1kBJ',
                  consumer_secret='uF36sUi9oXV6cPT92zLj32OLBBGZtitd6w8JhEIVkQzZBut7UE',
                  access_token_key='937778801395855360-cZYLinqhemGzT28DdIHg5aNX1T48Xez',
                  access_token_secret='bqOfqnFKn1oBSYBQVYqsfaJxtxJoR8AGGPMiAw1cpzp8d')

status = api.PostUpdate('sup dawg!')
print(status.text)

#connects properly
#$source activate
#$deactivate