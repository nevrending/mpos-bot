# Convert our config file
def load(config):
    settings = {}
    settings['host'] = config.get('IRC', 'host')
    settings['port'] = config.getint('IRC', 'port')
    settings['nick'] = config.get('IRC', 'nick')
    settings['user'] = config.get('IRC', 'user')
    settings['channel'] = config.get('IRC', 'channel')
    settings['password'] = config.get('IRC', 'password')
    settings['interval'] = config.getint('Blockupdate', 'interval')
    settings['api_key'] = config.get('API', 'key')
    settings['api_url'] = config.get('API', 'url')
    return settings
