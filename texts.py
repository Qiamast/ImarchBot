START_MSG = (
    "Hey [{first_name}](tg://user?id={chat_id})!\n\n"
    "I'm *Imarch* 🤖, a bot for searching any kind images on Google 🌐.\n\n"
    "Send /help to get started and see the instructions 📖."
)
HELP_MSG = (
    "📖 *Imarch Bot Usage*\n\n"
    "To search for images, just type my username and the query you want to search 🔎\n"
    "\n*Examples* 🧪 \n\n"
    "🔸 `@ImarchBot cat` - search for images of cats\n"
    "🔸 `@ImarchBot cat page:2` - search for images of cats on page 2\n"
    "\n❗ Beside the query, you can add commands to change the search results behavior.\n\n"
    "*Supported commands*:\n\n"
    "🔸 `page:<number>`: Change the page of the search results (default: 1)\n"
    "\n💡 *Note:*\n\n"
    "The search results are paginated. You can change the page "
    "of the search results by adding a command to the query.\n"

)
NOT_FOUND_MSG = (
    "Sorry, I couldn't find any results for your query 😔"
)
