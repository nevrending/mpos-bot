import urllib
import logging
import json

def help_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.help')
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :Commands supported: !status, !u, !last, !norris, !fortune, !thanks, !slap'
