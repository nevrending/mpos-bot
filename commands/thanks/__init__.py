import logging

def thanks_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.thanks')
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' : Your welcome!'
