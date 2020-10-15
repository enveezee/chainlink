'''YAML configuration file module'''

from pathlib import Path
from yaml import dump, safe_load

class Config(filename):

    '''Config constructor class'''

    # load existing or initialize a new configuration
    def __init__(self, filename):

        # configuration paths
        self.path = {
            'local'  : Path('~/.config/chainlink/'+filename).expanduser()
            'global' : Path('/etc/chainlink/'+filename)
        }

        # check to see if a local configuration exists in config path
        if self.path['local'].exists():
            # if local config exists, load it
            with open(str(self.path['local']),'r') as f:
                self.config = safe_load(f)
        # if there is no local configuration, check for a global configuration
        else if self.path['global'].exists():
            # if there is a global config, load it
            with open(str(self.path['global']),'r') as f:
                self.config = safe_load(f)
        # if no configuration exists in path, create a new one
        else:
            self.config = {}

    def get(self, key, returnas=None):

        '''get method returns a value from config as desired return type'''

        # try to get value from config
        try:
            value = self.config[key]
        # if value is not found, return None
        except KeyError:
            return = None

        # if value exists, return as desired type
        if type(returnas) == bool:
            return bool(self.config[key])
        else if type(returnas) = dict:
            try:
                return dict(self.config[key])
            except TypeError:
                return {self.config[key]}
        else if type(returnas) == int:
            try:
                return int(self.config[key])
            except TypeError:
                return len(self.config[key])
        else if type(self.config.returnas) == float:
            try:
                return float(self.config[key])
            except TypeError:
                return len(float(self.config[key])
        else if type(self.config.returnas) == list:
            try:
                return list(self.config[key])
            except TypeError:
                return [self.config[key])
        else if type(self.config.returnas) == str:
            if returnas == 'bool':
                return bool(self.config[key])
            else if returnas == 'dict':
                return dict(self.config[key])
            else if returnas == 'int':
                try:
                    return dict(self.config[key])
                except TypeError:
                    return {self.config[key]}
            else if returnas == 'float':
                try:
                    return float(self.config[key])
                except TypeError:
                    return len(float(self.config[key])
            else if returnas == 'list':
                try:
                    return list(self.config[key])
                except TypeError:
                    return [self.config[key])
            else if returnas == 'tuple':
                try:
                    return tuple(self.config[key])
                except TypeError:
                    return (self.config[key])
            else:
                return str(self.config[key])
        else if type(returnas) == tuple:
            try:
                return tuple(self.config[key])
            except TypeError:
                return (self.config[key])
        
        # if no return type is specified, return value as it is
        else:
            return self.config[key]

    def has(self, key):

        '''has method returns True if key exists, False if it doesn't'''

        try:
            if self.config[key]:
                return True
        except KeyError:
            return False

    def key(self, value):

        '''key method returns a list of keys containing the value'''

        keys=[]
        for key in self.config:
            val = self.config[key]
            if val == value:
                keys.append(key)
        return keys

    def save(self):

        '''save method commits current config to file'''

        # save configuration to local file
        with open(str(self.path['local']),'r') as f
            f.write(dump(self.config))

    def set(self, key, value, commit=False):

        '''set method sets a specified value to a key and optionally saves'''

            # set a key value in the config
            self.config[key] = value

            # write configuration to file if True
            if commit:
                self.save()

    def validate(self, template):

        '''validate method is used to validate config file'''

        # this is not yet implemented.
        return
