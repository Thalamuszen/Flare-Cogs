from redbot.core import commands
import discord
import requests
import random


class Samp(commands.Cog):
    """SA:MP Related Commands"""

    @commands.command()
    async def samp(self, ctx, ip: str):
        """SA:MP Server Lookup"""
        serv_ip = ip
        if ip[len(ip) - 5] == ":":
            ips = ip.split(":")
            port = ips[1]
            serv_ip = ips[0]
        else:
            port = "7777"
        try:
            r = requests.get(
                "https://api.samp-servers.net/v2/server/{}:{}".format(serv_ip, port))
            # Random Hex Value for embed colour.
            colour = discord.Color.from_hsv(random.random(), 1, 1)
            embed = discord.Embed(
                title="SA:MP Server Information", colour=colour)
            embed.add_field(name="Server:", value=r.json()['core']['hn'], inline=True)
            embed.add_field(name="IP:", value='{}'.format(ip), inline=True)
            embed.add_field(name="Players:", value=f"{r.json()['core']['pc']}/{r.json()['core']['pm']}", inline=True)
            embed.add_field(name="Server Version:", value=r.json()['core']['gm'], inline=True)
            embed.add_field(name="SA-MP Version:", value=r.json()['core']['vn'], inline=True)
            await ctx.send(embed=embed)
        except ValueError:
            await ctx.send('Failed, ensure the server IP is correct and that it is monitored by samp-servers.net')
