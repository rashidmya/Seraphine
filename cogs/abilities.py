import discord
from discord.ext import commands
import json
import traceback
import re
import os
from dotenv import load_dotenv

load_dotenv()
version = str(os.getenv('VERSION'))

ops = '<:outage:835522354963677184>'

class Abilities(commands.Cog):
    def __init__(self, client):
        self.client = client   
   
    @commands.command()
    async def ability(self, ctx, value, ability):
        if len(value) > 2:
            if ability == None:
                pass
            elif ability.lower() == 'p' or ability.lower() == 'passive': 
                await self.ability_passive(ctx, value)
            elif ability.lower() == 'q':
                await self.ability_q(ctx, value)
            elif ability.lower() == 'w':
                await self.ability_w(ctx, value)
            elif ability.lower() == 'e':
                await self.ability_e(ctx, value)
            elif ability.lower() == 'r':
                await self.ability_r(ctx, value)
            else:
                await ctx.send("That's not a valid ability.")
        else:
            await ctx.send("Oops, Couldn't find champion.")
            
        
    
    async def ability_passive(self, ctx, value):
        try:
            with open(f'dragontail/{version}/data/en_GB/championFull.json', encoding='utf-8') as f:
                champions = json.load(f)
            
            champions_data = champions['data']
            champion = value.lower()
            name = None
            title = None
            passive_name = None
            passive_description = None
            passive_image = None
            passive_images_path = f'dragontail/{version}/img/passive/'
            cid = None
            pic = None

            for k,v in champions_data.items():
                if champion in k.lower():
                    name = v['name']
                    title = v['title']
                    cid = v['key']
                    pic = v['id']
                    passive_name = v['passive']['name']
                    clean = re.compile('<.*?>')
                    passive_description = re.sub(clean, "", v['passive']['description']) 
                    passive_image = v['passive']['image']['full']
            passive_image_full_path = passive_images_path + passive_image
            f.close()
            
            file = discord.File(f"{passive_image_full_path}", filename=f"{passive_image}")
            embed = discord.Embed(description='<:sep:838164218514505759> \u200B <:sep:838164218514505759>', color=0xfda5b0)
            embed.set_author(name=f'{name} - {title.title()}', icon_url=f'https://seraphine-bot.s3.eu-central-1.amazonaws.com/champion/{pic}.png')
            embed.set_thumbnail(url=f'attachment://{passive_image}')
            embed.set_image(url=f'https://seraphine-bot.s3.eu-central-1.amazonaws.com/abilities_gifs/ability_{cid}_p.gif')
            embed.add_field(name=f'(Passive) {passive_name}', value=f"{passive_description}", inline=False)
            await ctx.send(file=file, embed=embed)
        except IndexError:
            await ctx.send("Oops, Couldn't find champion.") 
        except Exception:
            traceback.print_exc()
        
    async def ability_q(self, ctx, value):
        try:
            with open(f'dragontail/{version}/data/en_GB/championFull.json', encoding='utf-8') as f:
                champions = json.load(f)
            
            champions_data = champions['data']
            champion = value.lower()
            name = None
            title = None
            spells_names = []
            spells_description = []
            spells_cd = []
            spells_cost = []
            spells_image = []
            spell_images_path = f'dragontail/{version}/img/spell/'
            pic = None

            for k,v in champions_data.items():
                if champion in k.lower():
                    name = v['name']
                    title = v['title']
                    cid = v['key']
                    pic = v['id']
                    for spell in v['spells']:
                        spells_names.append(spell['name'])  
                        clean = re.compile('<.*?>')
                        description = re.sub(clean, "", spell['description'])  
                        spells_description.append(description)
                        spells_cd.append(spell['cooldownBurn'])
                        spells_cost.append(spell['costBurn'])
                        spells_image.append(spell['image']['full'])
            spell_image_full_path = spell_images_path + spells_image[0]
            f.close()
            
            file = discord.File(f"{spell_image_full_path}", filename=f"{spells_image[0]}")
            embed = discord.Embed(description='<:sep:838164218514505759> \u200B <:sep:838164218514505759>', color=0xfda5b0)
            embed.set_author(name=f'{name} - {title.title()}', icon_url=f'https://seraphine-bot.s3.eu-central-1.amazonaws.com/champion/{pic}.png')
            embed.set_thumbnail(url=f'attachment://{spells_image[0]}')
            embed.set_image(url=f'https://seraphine-bot.s3.eu-central-1.amazonaws.com/abilities_gifs/ability_{cid}_q.gif')
            embed.add_field(name=f'(Q) {spells_names[0]}', value=f"{spells_description[0]}", inline=False)
            embed.add_field(name='Cooldown', value=f"{spells_cd[0]}")
            embed.add_field(name='Cost', value=f"{spells_cost[0]}")
            await ctx.send(file=file, embed=embed)
        except IndexError:
            await ctx.send("Oops, Couldn't find champion.") 
        except Exception:
            traceback.print_exc()
    
    async def ability_w(self, ctx, value):
        try:
            with open(f'dragontail/{version}/data/en_GB/championFull.json', encoding='utf-8') as f:
                champions = json.load(f)
            
            champions_data = champions['data']
            champion = value.lower()
            name = None
            title = None
            spells_names = []
            spells_description = []
            spells_cd = []
            spells_cost = []
            spells_image = []
            spell_images_path = f'dragontail/{version}/img/spell/'
            pic = None

            for k,v in champions_data.items():
                if champion in k.lower():
                    name = v['name']
                    title = v['title']
                    cid = v['key']
                    pic = v['id']
                    for spell in v['spells']:
                        spells_names.append(spell['name'])  
                        clean = re.compile('<.*?>')
                        description = re.sub(clean, "", spell['description'])  
                        spells_description.append(description)
                        spells_cd.append(spell['cooldownBurn'])
                        spells_cost.append(spell['costBurn'])
                        spells_image.append(spell['image']['full'])
            spell_image_full_path = spell_images_path + spells_image[1]
            f.close()
            
            file = discord.File(f"{spell_image_full_path}", filename=f"{spells_image[1]}")
            embed = discord.Embed(description='<:sep:838164218514505759> \u200B <:sep:838164218514505759>', color=0xfda5b0)
            embed.set_author(name=f'{name} - {title.title()}', icon_url=f'https://seraphine-bot.s3.eu-central-1.amazonaws.com/champion/{pic}.png')
            embed.set_thumbnail(url=f'attachment://{spells_image[1]}')
            embed.set_image(url=f'https://seraphine-bot.s3.eu-central-1.amazonaws.com/abilities_gifs/ability_{cid}_w.gif')
            embed.add_field(name=f'(W) {spells_names[1]}', value=f"{spells_description[1]}", inline=False)
            embed.add_field(name='Cooldown', value=f"{spells_cd[1]}")
            embed.add_field(name='Cost', value=f"{spells_cost[1]}")
            await ctx.send(file=file, embed=embed)
        except IndexError:
            await ctx.send("Oops, Couldn't find champion.") 
        except Exception:
            traceback.print_exc()
    
    async def ability_e(self, ctx, value):
        try:
            with open(f'dragontail/{version}/data/en_GB/championFull.json', encoding='utf-8') as f:
                champions = json.load(f)
            
            champions_data = champions['data']
            champion = value.lower()
            name = None
            title = None
            spells_names = []
            spells_description = []
            spells_cd = []
            spells_cost = []
            spells_image = []
            spell_images_path = f'dragontail/{version}/img/spell/'
            pic = None

            for k,v in champions_data.items():
                if champion in k.lower():
                    name = v['name']
                    title = v['title']
                    cid = v['key']
                    pic = v['id']
                    for spell in v['spells']:
                        spells_names.append(spell['name'])  
                        clean = re.compile('<.*?>')
                        description = re.sub(clean, "", spell['description'])  
                        spells_description.append(description)
                        spells_cd.append(spell['cooldownBurn'])
                        spells_cost.append(spell['costBurn'])
                        spells_image.append(spell['image']['full'])
            spell_image_full_path = spell_images_path + spells_image[2]
            f.close()
            
            file = discord.File(f"{spell_image_full_path}", filename=f"{spells_image[2]}")
            embed = discord.Embed(description='<:sep:838164218514505759> \u200B <:sep:838164218514505759>', color=0xfda5b0)
            embed.set_author(name=f'{name} - {title.title()}', icon_url=f'https://seraphine-bot.s3.eu-central-1.amazonaws.com/champion/{pic}.png')
            embed.set_thumbnail(url=f'attachment://{spells_image[2]}')
            embed.set_image(url=f'https://seraphine-bot.s3.eu-central-1.amazonaws.com/abilities_gifs/ability_{cid}_e.gif')
            embed.add_field(name=f'(E) {spells_names[2]}', value=f"{spells_description[2]}", inline=False)
            embed.add_field(name='Cooldown', value=f"{spells_cd[2]}")
            embed.add_field(name='Cost', value=f"{spells_cost[2]}")
            await ctx.send(file=file, embed=embed)
        except IndexError:
            await ctx.send("Oops, Couldn't find champion.") 
        except Exception:
            traceback.print_exc()
    
    async def ability_r(self, ctx, value):
        try:
            with open(f'dragontail/{version}/data/en_GB/championFull.json', encoding='utf-8') as f:
                champions = json.load(f)
            
            champions_data = champions['data']
            champion = value.lower()
            name = None
            title = None
            spells_names = []
            spells_description = []
            spells_cd = []
            spells_cost = []
            spells_image = []
            spell_images_path = f'dragontail/{version}/img/spell/'
            pic = None

            for k,v in champions_data.items():
                if champion in k.lower():
                    name = v['name']
                    title = v['title']
                    cid = v['key']
                    pic = v['id']
                    for spell in v['spells']:
                        spells_names.append(spell['name'])  
                        clean = re.compile('<.*?>')
                        description = re.sub(clean, "", spell['description'])  
                        spells_description.append(description)
                        spells_cd.append(spell['cooldownBurn'])
                        spells_cost.append(spell['costBurn'])
                        spells_image.append(spell['image']['full'])
            spell_image_full_path = spell_images_path + spells_image[3]
            f.close()
            
            file = discord.File(f"{spell_image_full_path}", filename=f"{spells_image[3]}")
            embed = discord.Embed(description='<:sep:838164218514505759> \u200B <:sep:838164218514505759>', color=0xfda5b0)
            embed.set_author(name=f'{name} - {title.title()}', icon_url=f'https://seraphine-bot.s3.eu-central-1.amazonaws.com/champion/{pic}.png')
            embed.set_thumbnail(url=f'attachment://{spells_image[3]}')
            embed.set_image(url=f'https://seraphine-bot.s3.eu-central-1.amazonaws.com/abilities_gifs/ability_{cid}_r.gif')
            embed.add_field(name=f'(R) {spells_names[3]}', value=f"{spells_description[3]}", inline=False)
            embed.add_field(name='Cooldown', value=f"{spells_cd[3]}")
            embed.add_field(name='Cost', value=f"{spells_cost[3]}")
            await ctx.send(file=file, embed=embed)
        except IndexError:
            await ctx.send("Oops, Couldn't find champion.") 
        except Exception:
            traceback.print_exc()
            
    @ability.error
    async def ability_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title=f'{ops} Seraphine: Ability', description="You need to give me a champion and a skill!", color=0xfda5b0)
            embed.add_field(name='Usage', value='`!ability [champion] [p/q/w/e/r]`')
            await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(Abilities(client))