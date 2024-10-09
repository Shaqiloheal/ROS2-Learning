from setuptools import find_packages, setup

package_name = 'talker_listener'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shaqiloheal',
    maintainer_email='shaqiloheal@todo.todo',
    description='Writing the publisher node (talker)',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = talker_listener.publisher_member_function:main',
            'listener = talker_listener.subscriber_member_function:main',
        ],
    },
)
