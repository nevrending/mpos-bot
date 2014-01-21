import logging

def slap_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.slap')
    userNick = line.split(':')[2].split(' ')
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' : Gan ' + userNick + ', dikaplok tuh~'
