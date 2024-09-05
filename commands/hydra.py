import subprocess
from discord.ext import commands

class Hydra(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hydra")
    async def hydra(ctx, protocol: str, target: str, user: str, wordlist: str):
        """
        Commande pour lancer Hydra depuis Discord.
    
        Arguments:
        - protocol: Le protocole à tester (par exemple, ssh, ftp, http).
        - target: L'adresse IP ou le domaine de la cible.
        - user: Nom d'utilisateur à tester.
        - wordlist: Chemin du fichier de la liste de mots de passe.
        """
        try:
            cmd = ['hydra', '-l', user, '-P', wordlist, '-t', '4', protocol + '://' + target]

            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            output = result.stdout if result.returncode == 0 else result.stderr

            if len(output) > 2000:
                output = output[:1990] + '... [Résultat tronqué]'

            await ctx.send(f'```{output}```')
        except Exception as e:
            await ctx.send(f"Erreur lors de l'exécution de Hydra : {str(e)}")

def setup(bot):
    bot.add_cog(Hydra(bot))