# Keep in mind that there's no actual api endpoint for users to get guild members.
# So, to get guild members, we have to request for and read the member list.
# This is all handled with the bot.gateway.fetchMembers(...) function :) . This function can either be run while the gateway is connected or before the gateway connects.
# Note, you'll need to connect to the gateway to get the member list.
# An example usage is below. The Guild and Channel ids used are from the fortnite server (652k members, around 150k of those are actually fetchable).
# The number of fetchable members changes from time to time.
# https://github.com/Merubokkusu/Discord-S.C.U.M/blob/master/docs/using.md#fetch-guild-members

import discum
bot = discum.Client(token='your token')

def close_after_fetching(resp, guild_id):
	if bot.gateway.finishedMemberFetching(guild_id):
		lenmembersfetched = len(bot.gateway.session.guild(guild_id).members) #this line is optional
		print(str(lenmembersfetched)+' members fetched') #this line is optional
		bot.gateway.removeCommand(close_after_fetching)
		bot.gateway.close()

def get_members(guild_id, channel_id):
	bot.gateway.fetchMembers(guild_id, channel_id)
	bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
	bot.gateway.run()
	return bot.gateway.session.guild(guild_id).members

members = get_members('322850917248663552', '754536220826009670')
