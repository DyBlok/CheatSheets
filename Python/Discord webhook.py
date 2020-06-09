#imports of python modules
from discord_webhook import DiscordWebhook, DiscordEmbed
#Setting the webhook URL
#WebhookUrl = ['https://discordapp.com/api/webhooks/636360687668690985/ap5AMc15BLz4M4SM84uiW2Wx93KiUbnx7BkVyRjAfD2fXn7c7qjf0HlWtbZO16i1CkJ-', 'https://discordapp.com/api/webhooks/712738328985862187/ndNF5Wospo9wqIaWD4TiFWhfQQ4_78cX9McI5hd0ooFsTUSCvRVnFYFf9ntijfiv2dA2']
#use [] to use multiple webhooks
WebhookUrl = 'https://discordapp.com/api/webhooks/636360687668690985/ap5AMc15BLz4M4SM84uiW2Wx93KiUbnx7BkVyRjAfD2fXn7c7qjf0HlWtbZO16i1CkJ-'
def post_discord(Field2):
#Selecting the url for the webhook
    webhook = DiscordWebhook(url=WebhookUrl, username='Username', avatar_url='https://avatars3.githubusercontent.com/u/62259640?s=460&u=6124b4b9ed87018e1dfe84a2138393011154cd50&v=4')
#Starting the embed. Color is hex color but replace # with 0x. Use https://www.spycolor.com/. 
    embed = DiscordEmbed(title='A Title', description='A description \n with 2 lines', color=0x00FF00, url='https://google.com')
#Adding more info
    embed.add_embed_field(name='Field 1', value='Field 1 text')
    embed.add_embed_field(name='Field 2', value=Field2)
#Use inline false to get the field underneath the others
    embed.add_embed_field(name='Field 3', value='[Field 3 text](http://example.com)',inline=False)
    embed.set_thumbnail(url='https://avatars3.githubusercontent.com/u/62259640?s=460&u=6124b4b9ed87018e1dfe84a2138393011154cd50&v=4')
    embed.set_footer(text='My Footer', icon_url='https://avatars3.githubusercontent.com/u/62259640?s=460&u=6124b4b9ed87018e1dfe84a2138393011154cd50&v=4')
    embed.set_timestamp()
#Adding embeds and executing the webhook
    webhook.add_embed(embed)
    webhook.execute()
    
Field2 = 'Field 2 text'
post_discord(Field2)
#Full documentation
#https://pypi.org/project/discord-webhook/
