START_MSG = (
    "Hey [{first_name}](tg://user?id={chat_id})!\n\n"
    "I'm *Imarch* ๐ค, a bot for searching any kind images on Google ๐.\n\n"
    "Send /help to get started and see the instructions ๐."
)
HELP_MSG = (
    "๐ *Imarch Bot Usage*\n\n"
    "To search for images, just type my username and the query you want to search ๐\n"
    "\n*Examples* ๐งช \n\n"
    "๐ธ `@ImarchBot cat` - search for images of cats\n"
    "๐ธ `@ImarchBot cat page:2` - search for images of cats on page 2\n"
    "\nโ Beside the query, you can add commands to change the search results behavior.\n\n"
    "*Supported commands*:\n\n"
    "๐ธ `page:<number>`: Change the page of the search results (default: 1)\n"
    "\n๐ก *Note:*\n\n"
    "The search results are paginated. You can change the page "
    "of the search results by adding a command to the query.\n"

)
NOT_FOUND_MSG = (
    "Sorry, I couldn't find any results for your query ๐"
)
SPELLING_MSG = (
    "๐ก Did you mean {corrected_query!r} instead?"
)
PRIVATE_SEARCH_MSG = (
    "Press the button below to search for *{query!r}* "
    "in this chat ๐๐ป"
)
