from main import github

with github() as bot:
    bot.webpage_url()
    bot.rep_link_click()
    bot.repos_click()
    bot.repos_data()


