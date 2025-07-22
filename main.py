from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix=">", intents=discord.Intents.default())

class BoardRepresentationButton(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="Read about the first part - Board Representation", style=discord.ButtonStyle.success)
    async def go_to_boardrepresentation(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a fake context from interaction
        ctx = await self.bot.get_context(interaction.message)
        ctx.interaction = interaction  # optional

        command = self.bot.get_command("boardrepresentation")
        await command.invoke(ctx)

class EvaluationButton(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="Done reading? You may want to know about evaluating too", style=discord.ButtonStyle.success)
    async def go_to_evaluation(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a fake context from interaction
        ctx = await self.bot.get_context(interaction.message)
        ctx.interaction = interaction  # optional

        command = self.bot.get_command("evaluation")
        await command.invoke(ctx)

class MinimaxButton(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="You might want to read about Minimax too", style=discord.ButtonStyle.success)
    async def go_to_minimax(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a fake context from interaction
        ctx = await self.bot.get_context(interaction.message)
        ctx.interaction = interaction  # optional

        command = self.bot.get_command("minimax")
        await command.invoke(ctx)

class AlphaBetaButton(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="You might also want to optimize Minimax", style=discord.ButtonStyle.success)
    async def go_to_alphabeta(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a fake context from interaction
        ctx = await self.bot.get_context(interaction.message)
        ctx.interaction = interaction  # optional

        command = self.bot.get_command("alphabeta")
        await command.invoke(ctx)

class MoveOrderingButton(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="Optimize Alpha-Beta pruning", style=discord.ButtonStyle.success)
    async def go_to_moveordering(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Create a fake context from interaction
        ctx = await self.bot.get_context(interaction.message)
        ctx.interaction = interaction  # optional

        command = self.bot.get_command("moveordering")
        await command.invoke(ctx)

@bot.event
async def on_message(message):
    if "<@1397151250340122634>" in message.content:
        await message.channel.send("""
This is a wiki to help you get started with writing your own chess engine. Topics will be divided into commands. I also recommended what to read next after each article.
There will be code examples for each part, so don't worry if you don't understand how to implement it in your engine. (but i know what are you gonna do heheheheh)

Note that this is written in Python, but the concept is kinda the same. Install the newest Python version at https://www.python.org/downloads/release/python-3135/
Use `>gettingstarted` to get started.""")
        
@bot.command(name="gettingstarted", help="Getting started with writing a chess engine")
async def gettingstarted(ctx):
    await ctx.send("""
Writing a chess engine is a lot of work, but it can be a fun and rewarding project.
If you are new, you can start with a library. I will use the `python-chess` package here. https://python-chess.readthedocs.io for more info.

There are 3 main parts of a chess engine:
1. The board representation
2. The board evaluation
3. The search algorithm
""", view=BoardRepresentationButton(ctx.bot))

@bot.command(name="boardrepresentation", help="A brief documentation about board representation")
async def boardrepresentation(ctx):
    await ctx.send("""
With `python-chess` it's quite easy to represent a chessboard. There is a built-in `Board` class with all the rules of chess and a `unicode()` method for displaying an Unicode board.
Here is an example about how to use it:
```py
import chess

board = chess.Board()
print(board.unicode(
# These are the optional parameters you can use for your board
invert_color=True, # Invert the color of the black pieces
borders=False, # Shows borders around the board
empty_square=".", # The character for empty squares
orientation=chess.WHITE # The orientation of the board
))
```

Once you are done, continue with the second part - evaluation.       
""", view=EvaluationButton(ctx.bot))
    
@bot.command(name="evaluation", help="A brief documentation about board evaluation")
async def evaluation(ctx):
    await ctx.send("You can read about a simple evaluation function here: https://docs.google.com/document/d/1ZSZdRZMz72WQPmbPRlrE3xMOSmRajyhjcLlWwhb_Mdc/edit?usp=sharing", view=MinimaxButton(ctx.bot))

@bot.command(name="minimax", help="A brief documentation about the minimax algorithm")
async def minimax(ctx):
    await ctx.send("You can read about the explanation of minimax here: https://docs.google.com/document/d/1f6Xrm-6T2NAjBnnoDXRhdUJLl3NmTY_nEJXXtDP1Q4c/edit?usp=sharing", view=AlphaBetaButton(ctx.bot))

@bot.command(name="alphabeta")
async def alphabeta(ctx):
    await ctx.send("You can read about the explanation of alpha-beta pruning here: https://docs.google.com/document/d/1ePVT1ep_WX5m-qG2-5rRW_PvSVsZXlqix-fE7Z3frRE/edit?usp=sharing", view=MoveOrderingButton(ctx.bot))

@bot.command(name="moveordering")
async def moveordering(ctx):
    await ctx.send("Have a headache here: https://docs.google.com/document/d/1e-Q-mv8ctG9rGn-806Jfb4u9p3K8iAJiCbGEL7vjHkk/edit?usp=sharing")

token = os.getenv("BOT_TOKEN")
bot.run(token)