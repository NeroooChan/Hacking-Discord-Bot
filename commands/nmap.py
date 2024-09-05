import subprocess
from discord.ext import commands

class Nmap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nmap")
    async def nmap(ctx, *, target: str):
        try:
            result = subprocess.run(['nmap', target], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
            output = result.stdout if result.returncode == 0 else result.stderr

            if len(output) > 2000:
                output = output[:1990] + '... [Résultat tronqué]'

            await ctx.send(f'```{output}```')
        except Exception as e:
            await ctx.send(f"Erreur lors de l'exécution de nmap : {str(e)}")

def setup(bot):
    bot.add_cog(Nmap(bot))