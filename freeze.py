from py2exe import freeze

freeze(console=[{'script': 'rsl/gen_erate.py'}],
    packages=['xtuml', 'rsl'],
    compressed=1,
    optimize=2,
    bundle_files=1)
