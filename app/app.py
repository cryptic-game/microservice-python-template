from cryptic import MicroService, Config, DatabaseWrapper, get_config

config: Config = get_config()

m: MicroService = MicroService("template")

wrapper: DatabaseWrapper = m.get_wrapper()

if __name__ == "__main__":
    from resources.endpoints import *

    wrapper.Base.metadata.create_all(bind=wrapper.engine)

    m.run()
