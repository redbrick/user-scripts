"""help menu"""

from .colours import blue, bright_cyan, green, red, white, yellow


def help_menu():
    return f"""
          {white('>> A quick guide on using')} {red('Redbrick')} {white('<<')}
{blue('.--------------.-------------------------------------------------------------.')}
{blue('|')} {green('What to type')} {blue('|')} {green('..and what it does!')}                                         {blue('|')}
{blue('|--------------|-------------------------------------------------------------|')}
{blue('|')} {bright_cyan('email')}        {blue('|')} Read your Redbrick email.                                   {blue('|')}
{blue('|')} {bright_cyan('news')}         {blue('|')} Read and post to the Redbrick newsgroups, 'The Boards'.     {blue('|')}
{blue('|')} {bright_cyan('chat')}         {blue('|')} Go into Redbrick's online chat rooms                        {blue('|')}
{blue('|')} {bright_cyan('hey')} user     {blue('|')} Send an instant message ('hey') to another Redbrick user.   {blue('|')}
{blue('|')} {bright_cyan('rbusers')}      {blue('|')} Show who's logged on to Redbrick right now.                 {blue('|')}
{blue('|')} {bright_cyan('passwd')}       {blue('|')} Change your password.                                       {blue('|')}
{blue('|')} {bright_cyan('chsh')}         {blue('|')} Change your user shell.                                     {blue('|')}
{blue('|')} {bright_cyan('chfn')}         {blue('|')} Change your "finger" information (your real name).          {blue('|')}
{blue('|')} {bright_cyan('motd')}         {blue('|')} Show the Message Of The Day (MOTD).                         {blue('|')}
{blue('|')} {bright_cyan('help')}         {blue('|')} Show this help again.                                       {blue('|')}
{blue('|')} {bright_cyan('help')} topic   {blue('|')} Show more help on the given topic (e.g. 'help hey')         {blue('|')}
{blue('|')} {bright_cyan('nohelp')}       {blue('|')} Don't show me this help at login again!                     {blue('|')}
{blue('|')} {bright_cyan('noforward')}    {blue('|')} Turn off forwarding of my Redbrick email.                   {blue('|')}
{blue('|')} {bright_cyan('logout')}       {blue('|')} Quit Redbrick (but why bother? It's so much fun!)           {blue('|')}
{blue("`--------------'-------------------------------------------------------------'")}
               {yellow('[ Helpdesk website - http://help.redbrick.dcu.ie ]')}"""
