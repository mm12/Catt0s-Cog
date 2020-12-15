from redbot.core import commands

class catt0s(commands.Cog):
    """Catt0s Cog"""

    @commands.command()
    async def catt0s(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
    @commands.command()
    async def weedfox(self, ctx):
        """sends weedfox"""
        # Your code will go here
        await ctx.send("<:WeedFox:785258579472941086>")
    @commands.command()
    @commands.command()
async def fuck(ctx: commands.Context, *users: discord.Member):
    """sex someone"""
    # by Catt0s for use with instacmd or to add to a cog
    fBot = " please no sexing the bot."
    fSelf = " fucked themselves."
    fOther = " sexed "
    fCat = " https://cdn.discordapp.com/attachments/702330905385238620/778863554467463178/Please_do_not_the_cat.gif "
    if len(users) == 2:
        if users[0].id == bot.user.id:
            await ctx.send(users[1].mention + fBot)
            await ctx.send(fCat)
        elif users[1].id == bot.user.id:
            await ctx.send(users[0].mention + fBot)
            await ctx.send(fCat)
        elif users[0].id == users[1].id:
            await ctx.send(ctx.author.mention + fSelf)
        else:
            await ctx.send(users[0].mention + fOther + users[1].mention)
    elif len(users) == 1:
        if users[0].id == bot.user.id:
            await ctx.send(ctx.author.mention + fBot)
            await ctx.send(fCat)
        elif users[0].id == ctx.author.id:
            await ctx.send(ctx.author.mention + fSelf)
        else:
            await ctx.send(ctx.author.mention + fOther + users[0].mention)
    else:
        await ctx.send("Mention someone to sex. Do [p]help fuck for more info.")
return fuck

