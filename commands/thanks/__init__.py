import logging

def u_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.u')
    userNick = line.split(':')[2].split(' ')
    logger.debug(userNick)
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' : Your welcome, ' + str(userNick) + ' :)'
