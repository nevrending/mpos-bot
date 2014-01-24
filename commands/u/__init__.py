import urllib
import logging
import json

def u_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.u')
    userNick = line.split(':')[2].split(' ')
    logger.debug(userNick)
    if len(userNick) == 2:
        userNick = userNick[1]
        url = urllib.urlopen(config['api_url'] + '&action=getuserstatus&api_key=' + config['api_key'] + '&id=' + userNick)
        if url.getcode() != 200:
            logger.error('Request failed with http error: ' + str(url.getcode()))
            return False
        jsonData = json.loads(url.read())
        strPoolLuck = str(round(jsonPublicData['shares_this_round'] / jsonData['getpoolstatus']['data']['estshares'] * 100, 2))
        strInvalidPercentage = str(round(jsonData['getuserstatus']['data']['shares']['invalid'] / jsonData['getuserstatus']['data']['shares']['valid'] * 100, 2))
        logger.info('Completed command')
        return 'PRIVMSG ' + config['channel'] + ' :' + 'Username: ' + str(jsonData['getuserstatus']['data']['username']) + ' | Hashrate: ' + str(jsonData['getuserstatus']['data']['hashrate']) + ' kh/s' + ' | Shares Valid: ' + str(jsonData['getuserstatus']['data']['shares']['valid']) + ' | Shares Invalid: ' + str(jsonData['getuserstatus']['data']['shares']['invalid']) + ' (' + strInvalidPercentage + '%)'
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' : Unable to find username'
