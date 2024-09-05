import subprocess
from discord.ext import commands

class Nikto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nikto")
    async def nikto(ctx, url: str):
        """
        Commande pour lancer Nikto depuis Discord.
    
        Arguments:
        - url: URL cible pour le scan de sécurité.
        """
        try:
            # Construire la commande Nikto
            cmd = ['nikto', '-h', url]

            # Exécuter la commande Nikto
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Récupérer et formater le résultat de la commande
            output = result.stdout if result.returncode == 0 else result.stderr

            # Limiter le nombre de caractères à envoyer sur Discord
            if len(output) > 2000:
                output = output[:1990] + '... [Résultat tronqué]'

            await ctx.send(f'```{output}```')
        except Exception as e:
            await ctx.send(f"Erreur lors de l'exécution de Nikto : {str(e)}")

def setup(bot):
    bot.add_cog(Nikto(bot))