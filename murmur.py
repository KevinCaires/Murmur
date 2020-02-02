import discord
from discord.ext import commands
from settings import API_URL
from utils import get_gql_client
from queries import *
from mutations import set_player

# Ultima edição feita por @Grievon

client = commands.Bot(command_prefix='m/')

@client.event
async def on_ready():
    print("Ei de sussurrar em vossos ouvidos!")


@client.command()
async def ponto(bot):
    """
    Mostra sua localização atual no mapa!
    """
    player = '<@!' + str(bot.author.id) + '>'
    payload = get_location(player)
    api_client = get_gql_client(API_URL)
    response = api_client.execute(payload)
    print(response)

    if response.get('actualPosition') == None:
        return await bot.send(f'{player} você não se encontra em nenhuma partida atualmente!')

    return await bot.send(f'{player} sua localização é `{response.get("actualPosition")}`')


@client.command()
async def mortos(bot):
    payload = is_dead()
    api_client = get_gql_client(API_URL)
    response = api_client.execute(payload)
    aux = list()

    for i in response:
        aux.append(response.get('discordId'))

    for i in response:
        await bot.send(response.get('discordId'))

    await bot.send('--------------------------')

    return await bot.send(aux)


@client.command()
async def carga(bot):
    player = '<@!' + str(bot.author.id) + '>'
    payload = is_dead()
    api_client = get_gql_client(API_URL)
    response = api_client.execute(payload)

    if response.get('bag') == None:
        return await bot.send(f'{player} não há itens no seu inventário!')

    return await bot.send(f"{player} você está carregando:```{response.get('bag')} ```")


@client.command()
async def ajuda(bot):
    player = '<@!' + str(bot.author.id) + '>'
    return await bot.send(f'''Olá {player}, sou Murmur o assistente que te ajudará a retornar para casa!


```Para verificar onde é sua atual localização no mapa basta comandar: m/ponto
Para verificar as informações de seu inventário apenas comande: m/carga
Para verificar os jogadores que estão mortos comande: m/mortos``` 


Espero ter ajudado com sua dúvidas!
''')
