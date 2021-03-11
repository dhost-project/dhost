class DockerBuild:

    def __init__(
        self,
        container,
        source_path,
        command=None,
        envars=None,
        *args,
        **kwargs
    ):
        self.container = container
        self.source_path = source_path
        self.command = command
        self.envars = envars

        self.is_success = None
        self.logs = None
        self.bundle_path = None

        print('Initialized DockerBuild')

    def build(self):
        """Main build function to start the process"""
        print(
            'Building source: {}, in container: {}, with command:`{}`'.format(
                str(self.source_path), str(self.container), str(self.command)
            )
        )
        if self.envars:
            print('Environment variables used:')
            for key, value in self.envars.items():
                print('{}={}'.format(key, value))

        # TODO code to generate the docker container, build the source folder
        # and retrieve the bundle
        self.prepare_docker()
        self.build_from_command()
        self.retrieve_bundle()

        # FOR TESTING ONLY
        self.is_success = True
        self.logs = '[11/Mar/2021 14:30:20] Worked\n[11/Mar/2021 14:30:20] Ok!'
        self.bundle_path = 'this/is/a/bundle/path'
        return self.is_success, self.logs, self.bundle_path

    def prepare_docker(self):
        pass

    def build_from_command(self):
        pass

    def retrieve_bundle(self):
        pass
