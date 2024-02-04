from discord.ext import commands

@commands.group()
async def command(ctx):
    message_content = "# AC3 Commands\n" \
                      "Here is a list of available AC3 commands.\n\n"

    commands_dict = {
        "/say": "Send a message in the chat.",
        "/commands": "Display a list of available commands.",
        "/report": "Report an issue or user to the moderators.",
        "/support": "Get assistance from the support team.",
        "/socials": "View the social media links for AC3.",
        "/friend": "Manage your friend list.",
        "/profile": "View or edit your user profile.",
        "/follow": "Follow another user.",
        "/item": "View or use an in-game item.",
        "/game": "Access game-related commands.",
        "/group": "Manage or join a group.",
        "/shop": "Browse and purchase items from the shop.",
        "/create": "Create various in-game content.",
        "/start_conversation": "Initiate a conversation with another user.",
        "/random_word": "Get a random word.",
        "/random_number": "Get a random number.",
        "/currency": "Check your in-game currency balance.",
        "/message": "Send a private message to another user.",
        "/language": "Set your preferred language.",
        "/correct": "Correct a previous message.",
        "/translate": "Translate a message.",
        "/register": "Register for an AC3 account."
    }

    for command, description in commands_dict.items():
        message_content += f"{command}: {description}\n"


    message_content += "\nMore commands soon!"

    # Sending the message
    await ctx.author.send(message_content)

command.name = 'commands'

async def setup(bot):
    bot.add_command(command)
