try:
    from setuptools import setup

    except ImportError:
        from distutils.core import setup

    config = [
        'description': 'Hacking Game',
        'author': 'David Lynch',
        'url': 'URL to get it at.',
        'download_url': 'Where to download it.',
        'author_email': 'davelynch45@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['hackrecon'],
        'scripts': [],
        'name': 'hackgame'
    ]
 
    setup(**config)
