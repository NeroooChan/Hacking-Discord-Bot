import subprocess
from discord.ext import commands

sqlmap_path = './sqlmap/sqlmap.py' 

class SQLMap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sqlmap")
    async def sqlmap(ctx, url: str, options: str = ''):
        """
        Commande pour lancer SQLMap depuis Discord.
    
        Arguments:
        - url: URL cible pour le scan de vulnérabilités SQL Injection.
        - options: Options supplémentaires pour SQLMap (facultatif).
        """
        try:
            # Construire la commande SQLMap
            cmd = ['python3.7', sqlmap_path, '-u', url] + options.split()

            # Exécuter la commande SQLMap
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Récupérer et formater le résultat de la commande
            output = result.stdout if result.returncode == 0 else result.stderr

            # Limiter le nombre de caractères à envoyer sur Discord
            if len(output) > 2000:
                output = output[:1990] + '... [Résultat tronqué]'

            await ctx.send(f'```{output}```')
        except Exception as e:
            await ctx.send(f"Erreur lors de l'exécution de SQLMap : {str(e)}")

def setup(bot):
    bot.add_cog(SQLMap(bot))
