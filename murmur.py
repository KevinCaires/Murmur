import discord
from discord.ext import commands
from settings import API_URL
from utils import get_gql_client
from queries import *
from mutations import *
from images import imagens

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
    """
    Mostra os jogadores que foram mortos durante o jogo
    """
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
    """
    Mostra os itens do inventário do jogador
    """
    player = '<@!' + str(bot.author.id) + '>'
    payload = bag_itens(player)
    api_client = get_gql_client(API_URL)
    response = api_client.execute(payload)
    bag = response.get('bag')
    print(response)
    print(bag)
    if bag == None:
        return await bot.send(f'{player} não há itens no seu inventário!')
    else:
        return await bot.send(f"{player} você está carregando:```{bag} ```")


@client.command()
async def pegar(bot):
    """
    Pega os itens no mapa atual
    """
    player = '<@!' + str(bot.author.id) + '>'

    return await bot.send(f'{player} pegou a sua mãe, aquela gostosa!')

@client.command()
async def mapear(bot):
    """
    Varre as proximidades do mapa atrás de itens
    """
    player = '<@!' + str(bot.author.id) + '>'
    return await bot.send(f'{player} não há itens próximos!')


@client.command()
async def item(bot, *usr):
    """
    Mostra as informações dos itens
    """
    player = '<@!' + str(bot.author.id) + '>'
    payload = especific_item(' '.join(usr))
    api_client = get_gql_client(API_URL)
    response = api_client.execute(payload)
    img = imagens(' '.join(usr))
    if not usr:
        return await bot.send(f'{player} por favor informe o nome do item que deseja as informações!')
    else:
        edges = response['items']['edges']
        node = edges[0].get('node') if edges else None
        nome = node.get('name') if node else None
        descricao = node.get('description') if node else None
        peso = node.get('weight') if node else None

        embed = discord.Embed(color=0x1E1E1E, type='rich')
        embed.set_thumbnail(url=f'{img}')
        embed.add_field(name=f'{nome}', value=f'{descricao}', inline=False)
        embed.add_field(name='Peso', value=f'{peso}', inline=False)

        desciption = f'{player} as informações sobre item são:'
        return await bot.send(desciption, embed=embed)


@client.command()
async def ajuda(bot):
    """Fornece uma prévia das ações tomadas pelo Bot"""
    player = '<@!' + str(bot.author.id) + '>'
    return await bot.send(f'''Olá {player}, sou Murmur o assistente que te ajudará a retornar para casa!


```Para verificar onde é sua atual localização no mapa basta comandar: m/ponto
Para verificar as informações de seu inventário apenas comande: m/carga
Para vereficar um item específico faça: m/item NomeDoItem privado
Para verificar os jogadores que estão mortos comande: m/mortos
Para pergar os itens do mapa basta comandar: m/pegar NomeDoItem
Para verificar se tem um item próximo use o comando: m/mapear```


''')


@client.command()
async def teste(bot):
    chat = bot.channel.id
    player = '<@!' + str(bot.author.id) + '>'

    if chat == 634589827907584009:
        return await bot.send(f"{player}, chama no pv que o pai tá on!")
    return await bot.send("I'm a suggar dady!")
    