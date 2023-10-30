class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_items(self, items):
        if len(items) == 0:
            return '-'
        return '\n- ' + '\n- '.join(items)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors: {self._stringify_items(self.authors)}\n"
            f"\nDependencies: {self._stringify_items(self.dependencies)}\n"
            f"\nDevelopment dependencies: {self._stringify_items(self.dev_dependencies)}"
        )
