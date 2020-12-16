import threading
from six import with_metaclass
from pluggy import PluginManager



class MetaPluginManager(type):
    _storage = threading.local()


    @staticmethod
    def get_plugin_manager():
        if not hasattr(MetaPluginManager._storage, 'plugin_manager'):
            MetaPluginManager._storage.plugin_manager = PluginManager('crow')
            MetaPluginManager._storage.plugin_manager.add_hookspecs()
            MetaPluginManager._storage.plugin_manager.add_hookspecs()
    
        return MetaPluginManager._storage.plugin_manager


    def __getattr__(cls, attr):
        pm = MetaPluginManager.get_plugin_manager()
        return getattr(pm, attr)


class plugin_manager(with_metaclass(MetaPluginManager)):
    pass