from importlib import metadata

print(metadata.version('pip'))

meta_pip = metadata.metadata('pip')

print(list(meta_pip))

print(meta_pip['Project-URl'])

print(len(metadata.files('pip')))